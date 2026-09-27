"""Input and semantic-output validation."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from jsonschema import Draft202012Validator

from .schemas import STAGE_SCHEMAS


class AnnotationValidationError(ValueError):
    """Raised when an input or paid model output violates the contract."""


def assistant_turns(trajectory: dict[str, Any]) -> list[dict[str, Any]]:
    turns = trajectory.get("assistant_responses")
    if not isinstance(turns, list):
        raise AnnotationValidationError(
            f"trajectory {trajectory.get('conversation_id')!r} needs assistant_responses[]"
        )
    return turns


def perturbation_events(trajectory: dict[str, Any]) -> list[dict[str, Any]]:
    events = trajectory.get("perturbation_events", [])
    if not isinstance(events, list):
        raise AnnotationValidationError("perturbation_events must be an array")
    return events


def validate_job(job: dict[str, Any]) -> None:
    if not isinstance(job, dict):
        raise AnnotationValidationError("each JSONL line must be a JSON object")
    if not isinstance(job.get("job_id"), str) or not job["job_id"].strip():
        raise AnnotationValidationError("job_id must be a non-empty string")
    shared = job.get("shared")
    if not isinstance(shared, dict):
        raise AnnotationValidationError("shared must be an object")
    if "authority" not in shared or not isinstance(shared["authority"], dict):
        raise AnnotationValidationError("shared.authority must be an object")
    if "user_turns" not in shared or not isinstance(shared["user_turns"], list):
        raise AnnotationValidationError("shared.user_turns must be an array")
    expected_turns: list[tuple[str, int]] = []
    seen_user_turns: set[str] = set()
    previous_user_index = -1
    for turn in shared["user_turns"]:
        if not isinstance(turn, dict):
            raise AnnotationValidationError(
                "every shared.user_turns item must be an object"
            )
        turn_id = turn.get("turn_id")
        turn_index = turn.get("turn_index")
        if (
            not isinstance(turn_id, str)
            or not turn_id
            or turn_id in seen_user_turns
            or not isinstance(turn_index, int)
            or turn_index < 1
            or turn_index <= previous_user_index
            or not isinstance(turn.get("content"), str)
        ):
            raise AnnotationValidationError(
                "shared.user_turns need unique IDs, increasing positive indexes, and text content"
            )
        expected_turns.append((turn_id, turn_index))
        seen_user_turns.add(turn_id)
        previous_user_index = turn_index
    trajectories = job.get("trajectories")
    if not isinstance(trajectories, list) or not trajectories:
        raise AnnotationValidationError("trajectories must be a non-empty array")

    conversation_ids: set[str] = set()
    for trajectory in trajectories:
        if not isinstance(trajectory, dict):
            raise AnnotationValidationError("every trajectory must be an object")
        conversation_id = trajectory.get("conversation_id")
        if not isinstance(conversation_id, str) or not conversation_id:
            raise AnnotationValidationError("every trajectory needs a conversation_id")
        if conversation_id in conversation_ids:
            raise AnnotationValidationError(
                f"duplicate conversation_id: {conversation_id}"
            )
        conversation_ids.add(conversation_id)

        seen_turns: set[str] = set()
        seen_units: set[str] = set()
        actual_turns: list[tuple[str, int]] = []
        previous_index = -1
        for turn in assistant_turns(trajectory):
            if not isinstance(turn, dict):
                raise AnnotationValidationError(
                    f"{conversation_id}: assistant response is not an object"
                )
            turn_id = turn.get("turn_id")
            turn_index = turn.get("turn_index")
            units = turn.get("assistant_response_units_exact")
            if not isinstance(turn_id, str) or not turn_id:
                raise AnnotationValidationError(f"{conversation_id}: missing turn_id")
            if turn_id in seen_turns:
                raise AnnotationValidationError(
                    f"{conversation_id}: duplicate turn_id {turn_id}"
                )
            if (
                not isinstance(turn_index, int)
                or turn_index < 1
                or turn_index <= previous_index
            ):
                raise AnnotationValidationError(
                    f"{conversation_id}/{turn_id}: turn_index must be positive and increasing"
                )
            if not isinstance(units, list):
                raise AnnotationValidationError(
                    f"{conversation_id}/{turn_id}: assistant_response_units_exact must be an array"
                )
            for unit in units:
                if not isinstance(unit, dict):
                    raise AnnotationValidationError(
                        f"{conversation_id}/{turn_id}: unit is not an object"
                    )
                unit_id = unit.get("unit_id")
                if not isinstance(unit_id, str) or not isinstance(
                    unit.get("exact_text"), str
                ):
                    raise AnnotationValidationError(
                        f"{conversation_id}/{turn_id}: each unit needs unit_id and exact_text"
                    )
                if unit_id in seen_units:
                    raise AnnotationValidationError(
                        f"{conversation_id}: duplicate unit_id {unit_id}"
                    )
                seen_units.add(unit_id)
            seen_turns.add(turn_id)
            actual_turns.append((turn_id, turn_index))
            previous_index = turn_index

        if actual_turns != expected_turns:
            raise AnnotationValidationError(
                f"{conversation_id}: assistant responses must match shared user-turn IDs and order"
            )

        seen_events: set[str] = set()
        for event in perturbation_events(trajectory):
            if not isinstance(event, dict) or not isinstance(
                event.get("event_id"), str
            ):
                raise AnnotationValidationError(
                    f"{conversation_id}: every event needs event_id"
                )
            event_id = event["event_id"]
            if event_id in seen_events:
                raise AnnotationValidationError(
                    f"{conversation_id}: duplicate event_id {event_id}"
                )
            active = event.get("active_post_injection_turn_ids")
            immediate = event.get("immediate_response_turn_id")
            required_metadata = {
                "injection_turn_id": str,
                "valid": bool,
                "visible": bool,
                "recoverable": bool,
                "clean_anchor": str,
                "injected_content": str,
            }
            for field, kind in required_metadata.items():
                if not isinstance(event.get(field), kind):
                    raise AnnotationValidationError(
                        f"{conversation_id}/{event_id}: {field} must be {kind.__name__}"
                    )
            if not isinstance(active, list) or not all(
                isinstance(x, str) for x in active
            ):
                raise AnnotationValidationError(
                    f"{conversation_id}/{event_id}: active_post_injection_turn_ids must be an array"
                )
            if not isinstance(immediate, str) or immediate not in seen_turns:
                raise AnnotationValidationError(
                    f"{conversation_id}/{event_id}: invalid immediate_response_turn_id"
                )
            if active and active[0] != immediate:
                raise AnnotationValidationError(
                    f"{conversation_id}/{event_id}: active list must start with immediate response"
                )
            if any(turn_id not in seen_turns for turn_id in active):
                raise AnnotationValidationError(
                    f"{conversation_id}/{event_id}: active list contains an unknown turn"
                )
            if len(active) != len(set(active)):
                raise AnnotationValidationError(
                    f"{conversation_id}/{event_id}: active turn list contains duplicates"
                )
            turn_positions = dict(actual_turns)
            if active != sorted(active, key=turn_positions.__getitem__):
                raise AnnotationValidationError(
                    f"{conversation_id}/{event_id}: active turns must be chronological"
                )
            seen_events.add(event_id)


def validate_stage_output(
    stage: int,
    output: dict[str, Any],
    job: dict[str, Any],
) -> None:
    errors = sorted(
        Draft202012Validator(STAGE_SCHEMAS[stage]).iter_errors(output), key=str
    )
    if errors:
        first = errors[0]
        location = ".".join(str(x) for x in first.absolute_path) or "<root>"
        raise AnnotationValidationError(
            f"stage {stage} schema error at {location}: {first.message}"
        )

    trajectories = job["trajectories"]
    expected_ids = [t["conversation_id"] for t in trajectories]
    top_key = {
        1: "trajectory_factual_annotations",
        2: "trajectory_process_annotations",
        3: "trajectory_event_annotations",
    }[stage]
    actual = output[top_key]
    actual_ids = [x["conversation_id"] for x in actual]
    if actual_ids != expected_ids:
        raise AnnotationValidationError(
            f"stage {stage}: conversation order mismatch; expected {expected_ids}, got {actual_ids}"
        )

    for trajectory, annotation in zip(trajectories, actual, strict=True):
        unit_turn, turn_index = _unit_and_turn_maps(trajectory)
        if stage in {1, 2}:
            _validate_turn_annotations(
                stage, trajectory, annotation, unit_turn, turn_index
            )
        else:
            _validate_event_annotations(trajectory, annotation, unit_turn)


def validate_cross_stage_consistency(
    stage2: dict[str, Any],
    stage3: dict[str, Any],
    job: dict[str, Any],
) -> None:
    process_by_conversation = {
        item["conversation_id"]: {
            turn["turn_id"]: turn for turn in item["turn_annotations"]
        }
        for item in stage2["trajectory_process_annotations"]
    }
    event_by_conversation = {
        item["conversation_id"]: item for item in stage3["trajectory_event_annotations"]
    }
    for trajectory in job["trajectories"]:
        conversation_id = trajectory["conversation_id"]
        result = event_by_conversation[conversation_id]
        effective = {
            turn_id: dict(turn)
            for turn_id, turn in process_by_conversation[conversation_id].items()
        }
        for override in result["process_overrides"]:
            effective[override["turn_id"]][override["field"]] = override["value"]
        for event in result["perturbation_events"]:
            for state in event["turn_states"]:
                if (
                    state["z"] == 1
                    and effective[state["turn_id"]]["step_validity"] is not False
                ):
                    raise AnnotationValidationError(
                        f"{conversation_id}/{event['event_id']}/{state['turn_id']}: "
                        "z=1 requires effective step_validity=false"
                    )


def _unit_and_turn_maps(
    trajectory: dict[str, Any],
) -> tuple[dict[str, str], dict[str, int]]:
    unit_turn: dict[str, str] = {}
    turn_index: dict[str, int] = {}
    for turn in assistant_turns(trajectory):
        turn_id = turn["turn_id"]
        turn_index[turn_id] = turn["turn_index"]
        for unit in turn["assistant_response_units_exact"]:
            unit_turn[unit["unit_id"]] = turn_id
    return unit_turn, turn_index


def _validate_evidence(
    evidence: Iterable[str],
    unit_turn: dict[str, str],
    *,
    expected_turn: str | None,
    label: str,
) -> None:
    for unit_id in evidence:
        if unit_id not in unit_turn:
            raise AnnotationValidationError(f"{label}: unknown evidence unit {unit_id}")
        if expected_turn is not None and unit_turn[unit_id] != expected_turn:
            raise AnnotationValidationError(
                f"{label}: evidence {unit_id} belongs to {unit_turn[unit_id]}, not {expected_turn}"
            )


def _validate_turn_annotations(
    stage: int,
    trajectory: dict[str, Any],
    annotation: dict[str, Any],
    unit_turn: dict[str, str],
    turn_index: dict[str, int],
) -> None:
    expected_turns = [
        (t["turn_id"], t["turn_index"]) for t in assistant_turns(trajectory)
    ]
    actual_turns = [
        (t["turn_id"], t["turn_index"]) for t in annotation["turn_annotations"]
    ]
    if actual_turns != expected_turns:
        raise AnnotationValidationError(
            f"{annotation['conversation_id']}: stage {stage} turn order mismatch"
        )
    claim_ids: set[str] = set()
    for turn in annotation["turn_annotations"]:
        turn_id = turn["turn_id"]
        evidence_key = "turn_evidence_units" if stage == 1 else "evidence_units"
        _validate_evidence(
            turn[evidence_key],
            unit_turn,
            expected_turn=turn_id,
            label=f"stage {stage}/{turn_id}",
        )
        if stage == 1:
            for claim in turn["claims"]:
                claim_id = claim["claim_id"]
                if claim_id in claim_ids:
                    raise AnnotationValidationError(f"duplicate claim_id: {claim_id}")
                if claim["source_turn"] != turn_id or not claim_id.startswith(
                    f"{turn_id}.C"
                ):
                    raise AnnotationValidationError(
                        f"{claim_id}: source_turn and claim prefix must match {turn_id}"
                    )
                _validate_evidence(
                    claim["evidence_units"],
                    unit_turn,
                    expected_turn=turn_id,
                    label=claim_id,
                )
                claim_ids.add(claim_id)
    if stage == 1:
        _validate_evidence(
            annotation["final_evidence_units"],
            unit_turn,
            expected_turn=None,
            label=f"{annotation['conversation_id']}/final",
        )


def _validate_event_annotations(
    trajectory: dict[str, Any],
    annotation: dict[str, Any],
    unit_turn: dict[str, str],
) -> None:
    expected_events = perturbation_events(trajectory)
    actual_events = annotation["perturbation_events"]
    if [x["event_id"] for x in actual_events] != [
        x["event_id"] for x in expected_events
    ]:
        raise AnnotationValidationError(
            f"{annotation['conversation_id']}: event order mismatch"
        )
    for source, result in zip(expected_events, actual_events, strict=True):
        immediate = source["immediate_response_turn_id"]
        active = source["active_post_injection_turn_ids"]
        if [x["turn_id"] for x in result["turn_states"]] != active:
            raise AnnotationValidationError(
                f"{result['event_id']}: active turn order mismatch"
            )
        if (
            result["c3_immediate_correction"] is True
            and result["c1_immediate_recognition"] is not True
        ):
            raise AnnotationValidationError(
                f"{result['event_id']}: C3=true requires C1=true"
            )
        recognition = result["c1_immediate_recognition"]
        mode = result["recognition_mode"]
        if recognition is True and mode not in {"explicit", "implicit"}:
            raise AnnotationValidationError(
                f"{result['event_id']}: C1=true requires explicit or implicit mode"
            )
        if recognition is False and mode != "none":
            raise AnnotationValidationError(
                f"{result['event_id']}: C1=false requires mode=none"
            )
        if recognition is None and mode != "invalid_or_missing":
            raise AnnotationValidationError(
                f"{result['event_id']}: C1=null requires mode=invalid_or_missing"
            )
        _validate_evidence(
            result["c1_evidence_units"], unit_turn, expected_turn=immediate, label="C1"
        )
        _validate_evidence(
            result["c3_evidence_units"], unit_turn, expected_turn=immediate, label="C3"
        )
        for state in result["turn_states"]:
            z = state["z"]
            expected_state = {0: "correct", 1: "polluted", None: "unobservable"}[z]
            if state["event_state"] != expected_state:
                raise AnnotationValidationError(
                    f"{result['event_id']}/{state['turn_id']}: z and event_state disagree"
                )
            if z is None and state["pollution_type"] != "none":
                raise AnnotationValidationError(
                    f"{result['event_id']}/{state['turn_id']}: unobservable state needs pollution_type=none"
                )
            if z == 0 and state["pollution_type"] != "none":
                raise AnnotationValidationError(
                    f"{result['event_id']}/{state['turn_id']}: correct state needs pollution_type=none"
                )
            if z == 1 and state["pollution_type"] == "none":
                raise AnnotationValidationError(
                    f"{result['event_id']}/{state['turn_id']}: polluted state needs direct/downstream type"
                )
            _validate_evidence(
                state["evidence_units"],
                unit_turn,
                expected_turn=state["turn_id"],
                label=f"{result['event_id']}/{state['turn_id']}",
            )
        immediate_state = result["turn_states"][0] if result["turn_states"] else None
        if immediate_state and source["valid"] and source["recoverable"]:
            if immediate_state["z"] == 0 and (
                result["c1_immediate_recognition"] is not True
                or result["c3_immediate_correction"] is not True
            ):
                raise AnnotationValidationError(
                    f"{result['event_id']}: immediate z=0 requires C1=true and C3=true"
                )
            if (
                immediate_state["z"] == 1
                and result["c3_immediate_correction"] is not False
            ):
                raise AnnotationValidationError(
                    f"{result['event_id']}: immediate z=1 requires C3=false"
                )
    for override in annotation["process_overrides"]:
        if override["turn_id"] not in {
            turn["turn_id"] for turn in assistant_turns(trajectory)
        }:
            raise AnnotationValidationError(
                f"process_override: unknown turn {override['turn_id']}"
            )
        _validate_evidence(
            override["evidence_units"],
            unit_turn,
            expected_turn=override["turn_id"],
            label="process_override",
        )
