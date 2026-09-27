"""JSON schemas used for Claude structured outputs."""

from __future__ import annotations

from typing import Any


def _nullable(kind: str) -> dict[str, Any]:
    return {"anyOf": [{"type": kind}, {"type": "null"}]}


STRING_ARRAY = {"type": "array", "items": {"type": "string"}}


CLAIM_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "claim_id",
        "claim",
        "source_turn",
        "truth",
        "basis",
        "evidence_units",
    ],
    "properties": {
        "claim_id": {"type": "string"},
        "claim": {"type": "string"},
        "source_turn": {"type": "string"},
        "truth": _nullable("boolean"),
        "basis": {"type": "string"},
        "evidence_units": STRING_ARRAY,
    },
}

STAGE1_TURN_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "turn_id",
        "turn_index",
        "turn_correct",
        "turn_correct_reason",
        "turn_evidence_units",
        "claims",
    ],
    "properties": {
        "turn_id": {"type": "string"},
        "turn_index": {"type": "integer"},
        "turn_correct": _nullable("boolean"),
        "turn_correct_reason": {"type": "string"},
        "turn_evidence_units": STRING_ARRAY,
        "claims": {"type": "array", "items": CLAIM_SCHEMA},
    },
}

STAGE1_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["trajectory_factual_annotations"],
    "properties": {
        "trajectory_factual_annotations": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "conversation_id",
                    "run_outcome",
                    "final_correct",
                    "final_answer",
                    "final_reason",
                    "final_evidence_units",
                    "turn_annotations",
                ],
                "properties": {
                    "conversation_id": {"type": "string"},
                    "run_outcome": {
                        "type": "string",
                        "enum": ["completed", "abstain", "execution_failure"],
                    },
                    "final_correct": _nullable("boolean"),
                    "final_answer": _nullable("string"),
                    "final_reason": {"type": "string"},
                    "final_evidence_units": STRING_ARRAY,
                    "turn_annotations": {"type": "array", "items": STAGE1_TURN_SCHEMA},
                },
            },
        }
    },
}

STAGE2_TURN_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "turn_id",
        "turn_index",
        "logical_fidelity",
        "logical_fidelity_reason",
        "causal_order",
        "causal_order_reason",
        "progress",
        "progress_reason",
        "step_validity",
        "step_validity_reason",
        "refusal_code",
        "refusal_reason",
        "evidence_units",
    ],
    "properties": {
        "turn_id": {"type": "string"},
        "turn_index": {"type": "integer"},
        "logical_fidelity": _nullable("boolean"),
        "logical_fidelity_reason": {"type": "string"},
        "causal_order": _nullable("boolean"),
        "causal_order_reason": {"type": "string"},
        "progress": _nullable("boolean"),
        "progress_reason": {"type": "string"},
        "step_validity": _nullable("boolean"),
        "step_validity_reason": {"type": "string"},
        "refusal_code": {
            "anyOf": [{"type": "integer", "enum": [0, 1, 2]}, {"type": "null"}]
        },
        "refusal_reason": {"type": "string"},
        "evidence_units": STRING_ARRAY,
    },
}

STAGE2_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["trajectory_process_annotations"],
    "properties": {
        "trajectory_process_annotations": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["conversation_id", "turn_annotations"],
                "properties": {
                    "conversation_id": {"type": "string"},
                    "turn_annotations": {"type": "array", "items": STAGE2_TURN_SCHEMA},
                },
            },
        }
    },
}

EVENT_STATE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "turn_id",
        "opportunity",
        "event_state",
        "z",
        "pollution_type",
        "within_turn_self_correction",
        "attribution_ambiguous",
        "reason",
        "evidence_units",
    ],
    "properties": {
        "turn_id": {"type": "string"},
        "opportunity": {"type": "boolean"},
        "event_state": {
            "type": "string",
            "enum": ["correct", "polluted", "unobservable"],
        },
        "z": {"anyOf": [{"type": "integer", "enum": [0, 1]}, {"type": "null"}]},
        "pollution_type": {
            "type": "string",
            "enum": ["direct", "downstream", "none"],
        },
        "within_turn_self_correction": {"type": "boolean"},
        "attribution_ambiguous": {"type": "boolean"},
        "reason": {"type": "string"},
        "evidence_units": STRING_ARRAY,
    },
}

EVENT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "event_id",
        "c1_immediate_recognition",
        "recognition_mode",
        "c1_reason",
        "c1_evidence_units",
        "c3_immediate_correction",
        "c3_reason",
        "c3_evidence_units",
        "turn_states",
    ],
    "properties": {
        "event_id": {"type": "string"},
        "c1_immediate_recognition": _nullable("boolean"),
        "recognition_mode": {
            "type": "string",
            "enum": ["explicit", "implicit", "none", "invalid_or_missing"],
        },
        "c1_reason": {"type": "string"},
        "c1_evidence_units": STRING_ARRAY,
        "c3_immediate_correction": _nullable("boolean"),
        "c3_reason": {"type": "string"},
        "c3_evidence_units": STRING_ARRAY,
        "turn_states": {"type": "array", "items": EVENT_STATE_SCHEMA},
    },
}

OVERRIDE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["turn_id", "field", "value", "reason", "evidence_units"],
    "properties": {
        "turn_id": {"type": "string"},
        "field": {"type": "string", "enum": ["step_validity", "causal_order"]},
        "value": {"type": "boolean", "enum": [False]},
        "reason": {"type": "string"},
        "evidence_units": STRING_ARRAY,
    },
}

STAGE3_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["trajectory_event_annotations"],
    "properties": {
        "trajectory_event_annotations": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "conversation_id",
                    "perturbation_events",
                    "process_overrides",
                ],
                "properties": {
                    "conversation_id": {"type": "string"},
                    "perturbation_events": {"type": "array", "items": EVENT_SCHEMA},
                    "process_overrides": {"type": "array", "items": OVERRIDE_SCHEMA},
                },
            },
        }
    },
}

STAGE_SCHEMAS = {1: STAGE1_SCHEMA, 2: STAGE2_SCHEMA, 3: STAGE3_SCHEMA}
