"""Three-stage annotation orchestration, checkpoints, and deterministic merge."""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .client import ANTHROPIC_MESSAGES_URL, ClaudeClient
from .schemas import STAGE_SCHEMAS
from .storage import atomic_write_json, load_json, safe_job_name
from .validation import (
    AnnotationValidationError,
    perturbation_events,
    validate_job,
    validate_cross_stage_consistency,
    validate_stage_output,
)


PROMPT_FILES = {
    1: "01_factuality_and_correctness.txt",
    2: "02_process_quality.txt",
    3: "03_perturbation_dynamics.txt",
}


@dataclass(frozen=True)
class PipelineConfig:
    output_dir: Path
    prompts_dir: Path | None = None


class AnnotationPipeline:
    def __init__(self, client: ClaudeClient, config: PipelineConfig) -> None:
        self.client = client
        self.config = config
        self.prompts_dir = config.prompts_dir or Path(__file__).parents[2] / "prompts"
        self.prompts = {
            stage: (self.prompts_dir / filename).read_text(encoding="utf-8")
            for stage, filename in PROMPT_FILES.items()
        }
        self.prompt_hashes = {
            stage: hashlib.sha256(prompt.encode("utf-8")).hexdigest()
            for stage, prompt in self.prompts.items()
        }

    async def run_job(self, job: dict[str, Any]) -> dict[str, Any]:
        validate_job(job)
        job_hash = _json_hash(job)
        job_dir = self.config.output_dir / safe_job_name(job["job_id"])
        job_dir.mkdir(parents=True, exist_ok=True)
        atomic_write_json(
            job_dir / "status.json",
            {
                "job_id": job["job_id"],
                "status": "running",
                "input_sha256": job_hash,
                "updated_at": _utc_now(),
            },
        )

        try:
            stage1, meta1 = await self._load_or_call_stage(
                stage=1,
                job=job,
                api_input=job,
                job_dir=job_dir,
                job_hash=job_hash,
            )
            stage2_input = copy.deepcopy(job)
            stage2_input["stage1_factual_annotations"] = stage1[
                "trajectory_factual_annotations"
            ]
            stage2, meta2 = await self._load_or_call_stage(
                stage=2,
                job=job,
                api_input=stage2_input,
                job_dir=job_dir,
                job_hash=job_hash,
            )

            event_trajectories = [
                trajectory
                for trajectory in job["trajectories"]
                if perturbation_events(trajectory)
            ]
            stage3: dict[str, Any] | None = None
            meta3: dict[str, Any] | None = None
            if event_trajectories:
                event_ids = {x["conversation_id"] for x in event_trajectories}
                event_job = copy.deepcopy(job)
                event_job["trajectories"] = event_trajectories
                stage3_input = copy.deepcopy(event_job)
                stage3_input["stage1_factual_annotations"] = [
                    item
                    for item in stage1["trajectory_factual_annotations"]
                    if item["conversation_id"] in event_ids
                ]
                stage3_input["stage2_process_annotations"] = [
                    item
                    for item in stage2["trajectory_process_annotations"]
                    if item["conversation_id"] in event_ids
                ]
                stage3, meta3 = await self._load_or_call_stage(
                    stage=3,
                    job=event_job,
                    api_input=stage3_input,
                    job_dir=job_dir,
                    job_hash=job_hash,
                )
                validate_cross_stage_consistency(stage2, stage3, event_job)

            final = self._merge(job, stage1, stage2, stage3, [meta1, meta2, meta3])
            atomic_write_json(job_dir / "annotation.json", final)
            atomic_write_json(
                job_dir / "status.json",
                {
                    "job_id": job["job_id"],
                    "status": "complete",
                    "input_sha256": job_hash,
                    "updated_at": _utc_now(),
                },
            )
            return final
        except Exception as exc:
            atomic_write_json(
                job_dir / "status.json",
                {
                    "job_id": job["job_id"],
                    "status": "failed",
                    "input_sha256": job_hash,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                    "updated_at": _utc_now(),
                },
            )
            raise

    async def _load_or_call_stage(
        self,
        *,
        stage: int,
        job: dict[str, Any],
        api_input: dict[str, Any],
        job_dir: Path,
        job_hash: str,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        checkpoint_path = job_dir / f"stage_{stage}.json"
        if checkpoint_path.exists():
            checkpoint = load_json(checkpoint_path)
            if checkpoint.get("input_sha256") != job_hash:
                raise AnnotationValidationError(
                    f"{checkpoint_path}: checkpoint belongs to different input content"
                )
            if checkpoint.get("prompt_sha256") != self.prompt_hashes[stage]:
                raise AnnotationValidationError(
                    f"{checkpoint_path}: prompt changed; use a fresh output directory"
                )
            annotation = checkpoint.get("annotation")
            if not isinstance(annotation, dict):
                raise AnnotationValidationError(
                    f"{checkpoint_path}: missing annotation object"
                )
            validate_stage_output(stage, annotation, job)
            return annotation, checkpoint.get("api", {})

        annotation, api_metadata = await self.client.annotate(
            system_prompt=self.prompts[stage],
            input_payload=api_input,
            output_schema=STAGE_SCHEMAS[stage],
        )
        validate_stage_output(stage, annotation, job)
        checkpoint = {
            "stage": stage,
            "job_id": job["job_id"],
            "input_sha256": job_hash,
            "prompt_sha256": self.prompt_hashes[stage],
            "annotation": annotation,
            "api": api_metadata,
            "created_at": _utc_now(),
        }
        atomic_write_json(checkpoint_path, checkpoint)
        return annotation, api_metadata

    def _merge(
        self,
        job: dict[str, Any],
        stage1: dict[str, Any],
        stage2: dict[str, Any],
        stage3: dict[str, Any] | None,
        api_metadata: list[dict[str, Any] | None],
    ) -> dict[str, Any]:
        factual = {
            x["conversation_id"]: copy.deepcopy(x)
            for x in stage1["trajectory_factual_annotations"]
        }
        process = {
            x["conversation_id"]: copy.deepcopy(x)
            for x in stage2["trajectory_process_annotations"]
        }
        events = (
            {
                x["conversation_id"]: copy.deepcopy(x)
                for x in stage3["trajectory_event_annotations"]
            }
            if stage3
            else {}
        )

        merged_trajectories: list[dict[str, Any]] = []
        for source in job["trajectories"]:
            conversation_id = source["conversation_id"]
            item = factual[conversation_id]
            if isinstance(source.get("metadata"), dict):
                item["metadata"] = copy.deepcopy(source["metadata"])
            process_turns = {
                turn["turn_id"]: turn
                for turn in process[conversation_id]["turn_annotations"]
            }
            for turn in item["turn_annotations"]:
                turn.update(process_turns[turn["turn_id"]])
                turn["process_overrides_applied"] = []

            event_result = events.get(conversation_id)
            if event_result:
                turns = {turn["turn_id"]: turn for turn in item["turn_annotations"]}
                for override in event_result["process_overrides"]:
                    target = turns[override["turn_id"]]
                    target[override["field"]] = override["value"]
                    target[f"{override['field']}_reason"] = override["reason"]
                    target["process_overrides_applied"].append(override)
                item["perturbation_events"] = []
                for event in event_result["perturbation_events"]:
                    merged_event = copy.deepcopy(event)
                    merged_event["derived"] = _derive_event_metrics(event)
                    item["perturbation_events"].append(merged_event)
            else:
                item["perturbation_events"] = []
            merged_trajectories.append(item)

        stage_api = {
            f"stage_{index}": metadata
            for index, metadata in enumerate(api_metadata, start=1)
            if metadata is not None
        }
        return {
            "schema_version": "sciarp.annotation.v2",
            "job_id": job["job_id"],
            "trajectories": merged_trajectories,
            "provenance": {
                "provider": "Anthropic",
                "endpoint": ANTHROPIC_MESSAGES_URL,
                "model": self.client.config.model,
                "thinking": "adaptive",
                "effort": "high",
                "prompt_sha256": {str(k): v for k, v in self.prompt_hashes.items()},
                "api": stage_api,
                "completed_at": _utc_now(),
            },
        }


def _derive_event_metrics(event: dict[str, Any]) -> dict[str, Any]:
    states = event["turn_states"]
    polluted_positions = [
        index for index, state in enumerate(states) if state["z"] == 1
    ]
    if not polluted_positions:
        return {
            "ever_polluted": False,
            "stable_recovery": None,
            "stable_recovery_turn_id": None,
            "relapse_after_recovery": None,
        }

    first_polluted = polluted_positions[0]
    later_correct = [
        index
        for index in range(first_polluted + 1, len(states))
        if states[index]["z"] == 0
    ]
    stable_index: int | None = None
    relapse = False
    for index in later_correct:
        if any(state["z"] == 1 for state in states[index + 1 :]):
            relapse = True
            continue
        stable_index = index
        break
    return {
        "ever_polluted": True,
        "stable_recovery": stable_index is not None,
        "stable_recovery_turn_id": states[stable_index]["turn_id"]
        if stable_index is not None
        else None,
        "relapse_after_recovery": relapse,
    }


def _json_hash(value: dict[str, Any]) -> str:
    canonical = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()
