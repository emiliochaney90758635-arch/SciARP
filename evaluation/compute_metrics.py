#!/usr/bin/env python3
"""Reproduce SciARP paper metrics from adjudicated annotations.

Aggregation order is fixed: turns within an execution, three repeats within a
condition, tasks within a table cell, then unweighted subclass/model macros.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from statistics import fmean
from typing import Any, Iterable, Mapping, Sequence


METRICS = ("TACC", "IC", "TP", "RV")
SUBCLASSES = (
    "1.1", "1.2", "1.3", "1.4", "2.1", "2.2", "2.3", "2.4",
    "3.1", "3.2", "3.3", "4.1", "4.2",
)
STAGE_BY_SUBCLASS = {
    **{x: "U" for x in SUBCLASSES if x.startswith("1.")},
    **{x: "E" for x in SUBCLASSES if x.startswith("2.")},
    **{x: "R" for x in SUBCLASSES if x.startswith("3.")},
    **{x: "C" for x in SUBCLASSES if x.startswith("4.")},
}
FREQUENCIES = (1, 2, 3)


class EvaluationError(ValueError):
    """Annotation data cannot support a paper-consistent calculation."""


@dataclass(frozen=True)
class Identity:
    document_id: str
    condition_id: str
    model: str
    task_id: str
    repeat_id: str
    variant: str


@dataclass
class TrajectoryRecord:
    identity: Identity
    trajectory: dict[str, Any]
    metadata: dict[str, Any]


@dataclass
class PairRun:
    model: str
    task_id: str
    condition_id: str
    repeat_id: str
    subclass: str
    stage: str
    injection_count: int
    injection_turn_id: str
    injection_ordinal: int
    position: str
    series_id: str
    overall_eligible: bool | None
    position_eligible: bool | None
    frequency_eligible: bool | None
    clean: dict[str, float]
    perturbed: dict[str, float]
    delta: dict[str, float]
    clean_indicators: dict[str, list[int]]
    perturbed_indicators: dict[str, list[int]]
    scoped_turn_ids: list[str]
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ConditionScore:
    model: str
    task_id: str
    condition_id: str
    subclass: str
    stage: str
    injection_count: int
    position: str
    series_id: str
    repeat_count: int
    overall_eligible: bool | None
    position_eligible: bool | None
    frequency_eligible: bool | None
    clean: dict[str, float]
    perturbed: dict[str, float]
    delta: dict[str, float]


@dataclass
class Audit:
    input_documents: int = 0
    input_trajectories: int = 0
    matched_pair_runs: int = 0
    complete_conditions: int = 0
    exclusions: list[dict[str, Any]] = field(default_factory=list)
    warnings: list[dict[str, Any]] = field(default_factory=list)

    def exclude(self, reason: str, **context: Any) -> None:
        self.exclusions.append({"reason": reason, **context})

    def warn(self, reason: str, **context: Any) -> None:
        self.warnings.append({"reason": reason, **context})


def mean(values: Iterable[float]) -> float:
    values = list(values)
    if not values:
        raise EvaluationError("cannot average an empty sequence")
    return float(fmean(values))


def binary(value: Any) -> int:
    """Only literal true is positive; false/null/missing are conservative zero."""
    return 1 if value is True else 0


def first(mapping: Mapping[str, Any], *keys: str, default: Any = None) -> Any:
    for key in keys:
        value = mapping.get(key)
        if value not in (None, ""):
            return value
    return default


def normalise_subclass(value: Any) -> str:
    if value is None:
        raise EvaluationError("missing perturbation subclass")
    text = str(value).strip().upper()
    aliases = {
        "U1": "1.1", "U2": "1.2", "U3": "1.3", "U4": "1.4",
        "E1": "2.1", "E2": "2.2", "E3": "2.3", "E4": "2.4",
        "R1": "3.1", "R2": "3.2", "R3": "3.3",
        "C1": "4.1", "C2": "4.2",
    }
    text = aliases.get(text, text)
    match = re.search(r"([1-4])\.([1-4])", text)
    if match:
        text = f"{match.group(1)}.{match.group(2)}"
    if text not in SUBCLASSES:
        raise EvaluationError(f"unsupported perturbation subclass: {value!r}")
    return text


def normalise_variant(value: Any, trajectory: Mapping[str, Any]) -> str:
    if value is not None:
        text = str(value).strip().lower()
        if text in {"clean", "base", "control"}:
            return "clean"
        if text in {"perturbed", "perturb", "adversarial"}:
            return "perturbed"
    return "perturbed" if trajectory.get("perturbation_events") else "clean"


def normalise_repeat(meta: Mapping[str, Any], conversation_id: str) -> str:
    explicit = first(meta, "repeat_id", "repeat", "run_id", "run_index")
    if explicit is not None:
        return str(explicit)
    match = re.search(r"(?:repeat|run)[-_ ]?0*(\d+)", conversation_id, re.I)
    if match:
        return str(int(match.group(1)))
    raise EvaluationError(
        f"missing repeat_id for conversation {conversation_id!r}; add metadata.repeat_id"
    )


def optional_bool(value: Any) -> bool | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"true", "1", "yes", "y"}:
        return True
    if text in {"false", "0", "no", "n"}:
        return False
    raise EvaluationError(f"expected boolean eligibility flag, got {value!r}")


def load_json_documents(path: Path) -> list[dict[str, Any]]:
    if path.is_dir():
        candidates = sorted(path.rglob("*.json")) + sorted(path.rglob("*.jsonl"))
        documents: list[dict[str, Any]] = []
        for candidate in candidates:
            documents.extend(load_json_documents(candidate))
        return documents
    if path.suffix.lower() == ".jsonl":
        documents = []
        with path.open("r", encoding="utf-8-sig") as handle:
            for line_number, raw in enumerate(handle, start=1):
                if not raw.strip():
                    continue
                value = json.loads(raw)
                if not isinstance(value, dict):
                    raise EvaluationError(f"{path}:{line_number} is not a JSON object")
                documents.append(value)
        return documents
    with path.open("r", encoding="utf-8-sig") as handle:
        value = json.load(handle)
    if isinstance(value, dict):
        return [value]
    if isinstance(value, list) and all(isinstance(x, dict) for x in value):
        return list(value)
    raise EvaluationError(f"unsupported JSON root in {path}")


def load_records(path: Path, audit: Audit) -> list[TrajectoryRecord]:
    documents = load_json_documents(path)
    audit.input_documents = len(documents)
    records: list[TrajectoryRecord] = []
    for document_index, document in enumerate(documents, start=1):
        document_id = str(document.get("job_id") or f"document-{document_index:06d}")
        trajectories = document.get("trajectories")
        if not isinstance(trajectories, list):
            audit.exclude("document_missing_trajectories", document_id=document_id)
            continue
        document_meta = document.get("metadata") if isinstance(document.get("metadata"), dict) else {}
        for trajectory_index, trajectory in enumerate(trajectories, start=1):
            if not isinstance(trajectory, dict):
                audit.exclude("trajectory_not_object", document_id=document_id,
                              trajectory_index=trajectory_index)
                continue
            conversation_id = str(trajectory.get("conversation_id") or trajectory_index)
            metadata = dict(document_meta)
            if isinstance(trajectory.get("metadata"), dict):
                metadata.update(trajectory["metadata"])
            try:
                model = first(metadata, "model", "evaluated_model", "agent_model")
                task_id = first(metadata, "task_id", "base_task_id")
                if model is None or task_id is None:
                    raise EvaluationError("metadata.model and metadata.task_id are required")
                identity = Identity(
                    document_id=document_id,
                    condition_id=str(first(metadata, "condition_id", "pair_id", default=document_id)),
                    model=str(model), task_id=str(task_id),
                    repeat_id=normalise_repeat(metadata, conversation_id),
                    variant=normalise_variant(metadata.get("variant"), trajectory),
                )
                records.append(TrajectoryRecord(identity, trajectory, metadata))
            except EvaluationError as exc:
                audit.exclude("invalid_trajectory_identity", document_id=document_id,
                              conversation_id=conversation_id, detail=str(exc))
    audit.input_trajectories = len(records)
    return records


def turns(trajectory: Mapping[str, Any]) -> list[dict[str, Any]]:
    raw_turns = trajectory.get("turn_annotations")
    if not isinstance(raw_turns, list) or not raw_turns:
        raise EvaluationError("turn_annotations must be a non-empty list")
    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, turn in enumerate(raw_turns, start=1):
        if not isinstance(turn, dict):
            raise EvaluationError(f"turn_annotations[{index}] is not an object")
        turn_id = str(turn.get("turn_id") or f"T{index}")
        if turn_id in seen:
            raise EvaluationError(f"duplicate turn_id {turn_id!r}")
        seen.add(turn_id)
        copied = dict(turn)
        copied["turn_id"] = turn_id
        result.append(copied)
    return result


def ic_indicator(turn: Mapping[str, Any]) -> int:
    claims = turn.get("claims")
    if isinstance(claims, list) and claims:
        return int(all(isinstance(c, dict) and c.get("truth") is True for c in claims))
    return binary(turn.get("turn_correct"))


def turn_indicators(turn: Mapping[str, Any]) -> dict[str, int]:
    return {
        "IC": ic_indicator(turn),
        "TP": binary(turn.get("progress")),
        "RV": binary(turn.get("step_validity")),
    }


def trajectory_scores(
    trajectory: Mapping[str, Any], start_ordinal: int
) -> tuple[dict[str, float], dict[str, list[int]], list[str]]:
    trajectory_turns = turns(trajectory)
    if not 1 <= start_ordinal <= len(trajectory_turns):
        raise EvaluationError(f"injection ordinal {start_ordinal} outside trajectory")
    tacc = int(
        trajectory.get("final_correct") is True
        and all(turn.get("turn_correct") is True for turn in trajectory_turns)
    )
    scoped = trajectory_turns[start_ordinal - 1:]
    indicators = {metric: [] for metric in ("IC", "TP", "RV")}
    for turn in scoped:
        values = turn_indicators(turn)
        for metric in indicators:
            indicators[metric].append(values[metric])
    scores = {"TACC": float(tacc)}
    scores.update({metric: mean(values) for metric, values in indicators.items()})
    return scores, indicators, [str(turn["turn_id"]) for turn in scoped]


def metadata_injection_ids(record: TrajectoryRecord) -> list[str]:
    ids = first(record.metadata, "injection_turn_ids", "perturbation_turn_ids")
    if isinstance(ids, list) and ids:
        return [str(x) for x in ids]
    single = first(record.metadata, "first_injection_turn_id", "injection_turn_id")
    if single is not None:
        return [str(single)]
    event_ids: list[str] = []
    events = record.trajectory.get("perturbation_events")
    if isinstance(events, list):
        for event in events:
            if not isinstance(event, dict):
                continue
            direct = first(event, "injection_turn_id", "turn_id")
            if direct is not None:
                event_ids.append(str(direct))
                continue
            states = event.get("turn_states")
            if isinstance(states, list) and states and isinstance(states[0], dict):
                if states[0].get("turn_id") is not None:
                    event_ids.append(str(states[0]["turn_id"]))
    if event_ids:
        return event_ids
    raise EvaluationError("cannot determine the first injected turn")


def injection_ordinal(record: TrajectoryRecord) -> tuple[str, int]:
    turn_ids = [str(x["turn_id"]) for x in turns(record.trajectory)]
    candidates: list[tuple[str, int]] = []
    for turn_id in metadata_injection_ids(record):
        if turn_id not in turn_ids:
            raise EvaluationError(f"injection turn {turn_id!r} not found")
        candidates.append((turn_id, turn_ids.index(turn_id) + 1))
    return min(candidates, key=lambda x: x[1])


def position(turn_count: int, ordinal: int) -> str:
    first_boundary = math.floor(turn_count / 3)
    second_boundary = math.floor(2 * turn_count / 3)
    if ordinal <= first_boundary:
        return "E"
    if ordinal <= second_boundary:
        return "M"
    return "L"


def perturbation_context(record: TrajectoryRecord) -> dict[str, Any]:
    subclass = normalise_subclass(first(
        record.metadata, "paper_subclass", "perturbation_subclass", "subclass", "perturbation_id"
    ))
    ids = metadata_injection_ids(record)
    raw_count = first(record.metadata, "injection_count", "perturbation_frequency")
    count = int(raw_count) if raw_count is not None else len(ids)
    if count not in FREQUENCIES:
        raise EvaluationError(f"injection_count must be 1, 2, or 3; got {count}")
    return {
        "subclass": subclass, "stage": STAGE_BY_SUBCLASS[subclass], "injection_count": count,
        "series_id": str(first(record.metadata, "frequency_series_id",
                               default=f"{record.identity.task_id}:{subclass}")),
        "overall_eligible": optional_bool(record.metadata.get("overall_eligible")),
        "position_eligible": optional_bool(record.metadata.get("position_eligible")),
        "frequency_eligible": optional_bool(record.metadata.get("frequency_eligible")),
    }


def pair_records(records: Sequence[TrajectoryRecord], audit: Audit) -> list[PairRun]:
    grouped: dict[tuple[str, str, str, str], list[TrajectoryRecord]] = defaultdict(list)
    for record in records:
        identity = record.identity
        grouped[(identity.model, identity.task_id, identity.condition_id,
                 identity.repeat_id)].append(record)
    pairs: list[PairRun] = []
    for key, group in sorted(grouped.items()):
        clean = [x for x in group if x.identity.variant == "clean"]
        perturbed = [x for x in group if x.identity.variant == "perturbed"]
        if len(clean) != 1 or len(perturbed) != 1:
            audit.exclude("pair_requires_exactly_one_clean_and_one_perturbed",
                          model=key[0], task_id=key[1], condition_id=key[2], repeat_id=key[3],
                          clean_count=len(clean), perturbed_count=len(perturbed))
            continue
        clean_record, pert_record = clean[0], perturbed[0]
        try:
            clean_ids = [x["turn_id"] for x in turns(clean_record.trajectory)]
            pert_ids = [x["turn_id"] for x in turns(pert_record.trajectory)]
            if clean_ids != pert_ids:
                raise EvaluationError("paired clean/perturbed turn IDs are not identical")
            injection_turn_id, ordinal = injection_ordinal(pert_record)
            context = perturbation_context(pert_record)
            clean_scores, clean_indicators, clean_scope = trajectory_scores(clean_record.trajectory, ordinal)
            pert_scores, pert_indicators, pert_scope = trajectory_scores(pert_record.trajectory, ordinal)
            if clean_scope != pert_scope:
                raise EvaluationError("paired evaluation windows do not match")
            computed_position = position(len(pert_ids), ordinal)
            declared = first(pert_record.metadata, "injection_position", "position")
            if declared is not None:
                aliases = {"EARLY": "E", "E": "E", "MIDDLE": "M", "MID": "M", "M": "M",
                           "LATE": "L", "L": "L"}
                declared_position = aliases.get(str(declared).strip().upper())
                if declared_position is None:
                    raise EvaluationError(f"invalid injection_position {declared!r}")
                if declared_position != computed_position:
                    audit.warn("declared_position_differs_from_floor_thirds", model=key[0],
                               task_id=key[1], condition_id=key[2], declared=declared_position,
                               computed=computed_position)
            delta = {m: clean_scores[m] - pert_scores[m] for m in METRICS}
            pairs.append(PairRun(
                model=key[0], task_id=key[1], condition_id=key[2], repeat_id=key[3],
                subclass=context["subclass"], stage=context["stage"],
                injection_count=context["injection_count"], injection_turn_id=injection_turn_id,
                injection_ordinal=ordinal, position=computed_position, series_id=context["series_id"],
                overall_eligible=context["overall_eligible"],
                position_eligible=context["position_eligible"],
                frequency_eligible=context["frequency_eligible"], clean=clean_scores,
                perturbed=pert_scores, delta=delta, clean_indicators=clean_indicators,
                perturbed_indicators=pert_indicators, scoped_turn_ids=clean_scope,
                metadata=dict(pert_record.metadata),
            ))
        except (EvaluationError, TypeError, ValueError) as exc:
            audit.exclude("invalid_pair", model=key[0], task_id=key[1], condition_id=key[2],
                          repeat_id=key[3], detail=str(exc))
    audit.matched_pair_runs = len(pairs)
    return pairs


def aggregate_conditions(
    pairs: Sequence[PairRun], expected_repeats: int, allow_incomplete: bool, audit: Audit
) -> list[ConditionScore]:
    grouped: dict[tuple[Any, ...], list[PairRun]] = defaultdict(list)
    for x in pairs:
        grouped[(x.model, x.task_id, x.condition_id, x.subclass, x.stage, x.injection_count,
                 x.position, x.series_id, x.overall_eligible, x.position_eligible,
                 x.frequency_eligible)].append(x)
    conditions: list[ConditionScore] = []
    for key, runs in sorted(grouped.items()):
        repeat_ids = {x.repeat_id for x in runs}
        if len(repeat_ids) != len(runs):
            audit.exclude("duplicate_repeat_in_condition", model=key[0], task_id=key[1],
                          condition_id=key[2])
            continue
        if not allow_incomplete and len(runs) != expected_repeats:
            audit.exclude("incomplete_repeats", model=key[0], task_id=key[1],
                          condition_id=key[2], observed=len(runs), expected=expected_repeats)
            continue
        clean = {m: mean(x.clean[m] for x in runs) for m in METRICS}
        perturbed = {m: mean(x.perturbed[m] for x in runs) for m in METRICS}
        conditions.append(ConditionScore(
            model=key[0], task_id=key[1], condition_id=key[2], subclass=key[3], stage=key[4],
            injection_count=key[5], position=key[6], series_id=key[7], repeat_count=len(runs),
            overall_eligible=key[8], position_eligible=key[9], frequency_eligible=key[10],
            clean=clean, perturbed=perturbed,
            delta={m: clean[m] - perturbed[m] for m in METRICS},
        ))
    audit.complete_conditions = len(conditions)
    return conditions


def add_metrics(row: dict[str, Any], clean: Mapping[str, float], perturbed: Mapping[str, float]) -> None:
    for metric in METRICS:
        row[f"{metric}_clean"] = clean[metric]
        row[f"{metric}_perturbed"] = perturbed[metric]
        row[f"{metric}_delta"] = clean[metric] - perturbed[metric]


def aggregate_rows(items: Sequence[ConditionScore], dimensions: Sequence[str]) -> list[dict[str, Any]]:
    grouped: dict[tuple[Any, ...], list[ConditionScore]] = defaultdict(list)
    for item in items:
        grouped[tuple(getattr(item, d) for d in dimensions)].append(item)
    rows: list[dict[str, Any]] = []
    for key, group in sorted(grouped.items()):
        row = {d: v for d, v in zip(dimensions, key)}
        row["n_tasks"] = len({x.task_id for x in group})
        row["n_conditions"] = len(group)
        clean = {m: mean(x.clean[m] for x in group) for m in METRICS}
        perturbed = {m: mean(x.perturbed[m] for x in group) for m in METRICS}
        add_metrics(row, clean, perturbed)
        rows.append(row)
    return rows


def select_overall(conditions: Sequence[ConditionScore], audit: Audit) -> list[ConditionScore]:
    grouped: dict[tuple[str, str, str], list[ConditionScore]] = defaultdict(list)
    for x in conditions:
        if x.injection_count == 1 and x.overall_eligible is not False:
            grouped[(x.model, x.task_id, x.subclass)].append(x)
    selected: list[ConditionScore] = []
    for key, group in sorted(grouped.items()):
        explicit = [x for x in group if x.overall_eligible is True]
        pool = explicit or group
        if len(pool) != 1:
            audit.exclude("ambiguous_overall_k1_condition", model=key[0], task_id=key[1],
                          subclass=key[2], candidates=[x.condition_id for x in pool])
            continue
        selected.append(pool[0])
    return selected


def append_average_rows(
    rows: Sequence[dict[str, Any]], group_field: str, count_field: str
) -> list[dict[str, Any]]:
    """Append direct cross-model averages calculated from unrounded cells."""
    output = [dict(row) for row in rows]
    by_group: dict[Any, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row.get("model") != "Average":
            by_group[row[group_field]].append(row)
    for group, group_rows in sorted(by_group.items()):
        average: dict[str, Any] = {
            "model": "Average", group_field: group, count_field: len(group_rows)
        }
        for metric in METRICS:
            for suffix in ("clean", "perturbed", "delta"):
                field = f"{metric}_{suffix}"
                average[field] = mean(row[field] for row in group_rows)
        output.append(average)
    return output


def overall_tables(
    selected: Sequence[ConditionScore],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    model_subclass_rows = aggregate_rows(selected, ("model", "subclass"))
    stage_groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in model_subclass_rows:
        stage_groups[(row["model"], STAGE_BY_SUBCLASS[row["subclass"]])].append(row)
    model_stage_rows: list[dict[str, Any]] = []
    for (model, stage), rows in sorted(stage_groups.items()):
        output: dict[str, Any] = {"model": model, "stage": stage, "n_subclasses": len(rows)}
        for metric in METRICS:
            for suffix in ("clean", "perturbed", "delta"):
                field = f"{metric}_{suffix}"
                output[field] = mean(row[field] for row in rows)
        model_stage_rows.append(output)
    model_rows: list[dict[str, Any]] = []
    for model in sorted({row["model"] for row in model_subclass_rows}):
        rows = [row for row in model_subclass_rows if row["model"] == model]
        output = {"model": model, "n_subclasses": len(rows)}
        for metric in METRICS:
            for suffix in ("clean", "perturbed", "delta"):
                field = f"{metric}_{suffix}"
                output[field] = mean(row[field] for row in rows)
        model_rows.append(output)
    if model_rows:
        average: dict[str, Any] = {"model": "Average", "n_models": len(model_rows)}
        for metric in METRICS:
            for suffix in ("clean", "perturbed", "delta"):
                field = f"{metric}_{suffix}"
                average[field] = mean(row[field] for row in model_rows)
        model_rows.append(average)
    return (
        append_average_rows(model_subclass_rows, "subclass", "n_models"),
        append_average_rows(model_stage_rows, "stage", "n_models"),
        model_rows,
    )


def position_table(conditions: Sequence[ConditionScore], audit: Audit) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str, str], list[ConditionScore]] = defaultdict(list)
    for x in conditions:
        if x.injection_count == 1 and x.position_eligible is True:
            grouped[(x.model, x.task_id, x.subclass, x.position)].append(x)
    selected: list[ConditionScore] = []
    for key, group in sorted(grouped.items()):
        explicit = [x for x in group if x.position_eligible is True]
        pool = explicit or group
        if len(pool) != 1:
            audit.exclude("ambiguous_position_condition", model=key[0], task_id=key[1],
                          subclass=key[2], position=key[3],
                          candidates=[x.condition_id for x in pool])
            continue
        selected.append(pool[0])
    return aggregate_rows(selected, ("model", "subclass", "position"))


def frequency_table(conditions: Sequence[ConditionScore], audit: Audit) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str, str, int], list[ConditionScore]] = defaultdict(list)
    for x in conditions:
        if x.frequency_eligible is True:
            grouped[(x.model, x.task_id, x.subclass, x.series_id, x.injection_count)].append(x)
    unique: dict[tuple[str, str, str, str, int], ConditionScore] = {}
    for key, group in sorted(grouped.items()):
        explicit = [x for x in group if x.frequency_eligible is True]
        pool = explicit or group
        if len(pool) != 1:
            audit.exclude("ambiguous_frequency_condition", model=key[0], task_id=key[1],
                          subclass=key[2], series_id=key[3], injection_count=key[4],
                          candidates=[x.condition_id for x in pool])
            continue
        unique[key] = pool[0]
    panels: dict[tuple[str, str, str, str], dict[int, ConditionScore]] = defaultdict(dict)
    for (model, task, subclass, series, frequency), item in unique.items():
        panels[(model, task, subclass, series)][frequency] = item
    selected: list[ConditionScore] = []
    for key, by_frequency in sorted(panels.items()):
        if all(k in by_frequency for k in FREQUENCIES):
            selected.extend(by_frequency[k] for k in FREQUENCIES)
        elif any(x.frequency_eligible is True for x in by_frequency.values()):
            audit.exclude("frequency_series_missing_k1_k2_or_k3", model=key[0], task_id=key[1],
                          subclass=key[2], series_id=key[3], observed=sorted(by_frequency))
    return aggregate_rows(selected, ("model", "subclass", "injection_count"))


def propagation_table(pairs: Sequence[PairRun]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for pair in pairs:
        dimensions_by_turn = [
            [m for m in ("IC", "TP", "RV")
             if pair.clean_indicators[m][i] > pair.perturbed_indicators[m][i]]
            for i in range(len(pair.scoped_turn_ids))
        ]
        impacted = [i for i, dimensions in enumerate(dimensions_by_turn) if dimensions]
        base = {"model": pair.model, "subclass": pair.subclass, "task_id": pair.task_id,
                "condition_id": pair.condition_id, "repeat_id": pair.repeat_id}
        if not impacted:
            records.append({**base, "impact": False, "onset_bucket": "No impact",
                            "first_dimension": None, "propagation": None})
            continue
        onset = impacted[0]
        bucket = str(onset) if onset in {0, 1, 2} else ">=3"
        first_dimensions = dimensions_by_turn[onset]
        declared = first(pair.metadata, "first_affected_dimension")
        if declared is not None and str(declared).strip().upper() in {"IC", "TP", "RV"}:
            first_dimension = str(declared).strip().upper()
        elif len(first_dimensions) == 1:
            first_dimension = first_dimensions[0]
        else:
            first_dimension = None
        if impacted == [onset]:
            propagation = "localized"
        elif impacted[-1] == len(dimensions_by_turn) - 1:
            propagation = "persistent"
        else:
            propagation = "recovered"
        records.append({**base, "impact": True, "onset_bucket": bucket,
                        "first_dimension": first_dimension, "propagation": propagation})
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[(record["model"], record["subclass"])].append(record)
    rows: list[dict[str, Any]] = []
    for (model, subclass), group in sorted(grouped.items()):
        impacted = [x for x in group if x["impact"]]
        onset = Counter(x["onset_bucket"] for x in impacted)
        dimensions = Counter(x["first_dimension"] for x in impacted if x["first_dimension"])
        outcomes = Counter(x["propagation"] for x in impacted)
        row: dict[str, Any] = {
            "model": model, "subclass": subclass, "n_executions": len(group),
            "n_impacted": len(impacted), "n_no_impact": len(group) - len(impacted),
            "n_first_dimension_unresolved": len(impacted) - sum(dimensions.values()),
        }
        for bucket in ("0", "1", "2", ">=3"):
            row[f"onset_{bucket}_count"] = onset[bucket]
            row[f"onset_{bucket}_share"] = onset[bucket] / len(impacted) if impacted else None
        resolved = sum(dimensions.values())
        for dimension in ("IC", "TP", "RV"):
            row[f"first_{dimension}_count"] = dimensions[dimension]
            row[f"first_{dimension}_share"] = dimensions[dimension] / resolved if resolved else None
        for outcome in ("localized", "recovered", "persistent"):
            row[f"{outcome}_count"] = outcomes[outcome]
            row[f"{outcome}_share"] = outcomes[outcome] / len(impacted) if impacted else None
        rows.append(row)
    return rows


def condition_rows(conditions: Sequence[ConditionScore]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in conditions:
        row: dict[str, Any] = {
            "model": item.model, "task_id": item.task_id, "condition_id": item.condition_id,
            "subclass": item.subclass, "stage": item.stage,
            "injection_count": item.injection_count, "position": item.position,
            "series_id": item.series_id, "repeat_count": item.repeat_count,
        }
        add_metrics(row, item.clean, item.perturbed)
        rows.append(row)
    return rows


def scale_rows(rows: Sequence[dict[str, Any]], percent: bool) -> list[dict[str, Any]]:
    if not percent:
        return [dict(row) for row in rows]
    scaled: list[dict[str, Any]] = []
    for row in rows:
        copied: dict[str, Any] = {}
        for key, value in row.items():
            share = key.endswith("_share")
            metric = key.startswith(("TACC_", "IC_", "TP_", "RV_"))
            copied[key] = value * 100.0 if (share or metric) and isinstance(value, float) else value
        scaled.append(copied)
    return scaled


def write_csv(path: Path, rows: Sequence[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields: list[str] = []
    for row in rows:
        fields.extend(key for key in row if key not in fields)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: f"{v:.6f}" if isinstance(v, float) else v for k, v in row.items()})


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run(args: argparse.Namespace) -> dict[str, Any]:
    audit = Audit()
    records = load_records(args.input, audit)
    pairs = pair_records(records, audit)
    conditions = aggregate_conditions(pairs, args.expected_repeats,
                                      args.allow_incomplete_repeats, audit)
    selected_overall = select_overall(conditions, audit)
    subclass, stage, model = overall_tables(selected_overall)
    position = position_table(conditions, audit)
    frequency = frequency_table(conditions, audit)
    overall_keys = {(x.model, x.task_id, x.condition_id) for x in selected_overall}
    propagation = propagation_table([
        pair for pair in pairs
        if (pair.model, pair.task_id, pair.condition_id) in overall_keys
    ])
    outputs = {
        "condition_metrics.csv": condition_rows(conditions),
        "overall_single_injection.csv": subclass,
        "stage_macro.csv": stage,
        "model_macro.csv": model,
        "position_metrics.csv": position,
        "frequency_metrics.csv": frequency,
        "propagation_metrics.csv": propagation,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for filename, rows in outputs.items():
        write_csv(args.output_dir / filename, scale_rows(rows, args.scale == "percent"))
    summary = {
        "protocol": "SciARP paper evaluation", "scale": args.scale,
        "expected_repeats": args.expected_repeats,
        "allow_incomplete_repeats": args.allow_incomplete_repeats,
        "input_documents": audit.input_documents, "input_trajectories": audit.input_trajectories,
        "matched_pair_runs": audit.matched_pair_runs,
        "complete_conditions": audit.complete_conditions,
        "overall_cells": len(subclass), "position_cells": len(position),
        "frequency_cells": len(frequency), "propagation_cells": len(propagation),
        "exclusion_count": len(audit.exclusions), "warning_count": len(audit.warnings),
    }
    write_json(args.output_dir / "summary.json", summary)
    write_json(args.output_dir / "audit.json", asdict(audit))
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compute paper-consistent SciARP metrics from merged annotations."
    )
    parser.add_argument("input", type=Path,
                        help="Merged annotation JSON/JSONL file or directory.")
    parser.add_argument("--output-dir", type=Path, required=True,
                        help="Destination for CSV tables and audit files.")
    parser.add_argument("--expected-repeats", type=int, default=3,
                        help="Required paired repetitions per condition (paper: 3).")
    parser.add_argument("--allow-incomplete-repeats", action="store_true",
                        help="Diagnostic only; not paper reproduction.")
    parser.add_argument("--scale", choices=("percent", "proportion"), default="percent",
                        help="CSV numeric scale (paper tables use percent).")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.expected_repeats < 1:
        parser.error("--expected-repeats must be at least 1")
    try:
        summary = run(args)
    except (EvaluationError, OSError, json.JSONDecodeError) as exc:
        print(f"evaluation failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
