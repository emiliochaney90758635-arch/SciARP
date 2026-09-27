"""Compute paper-aligned strict correctness from SciARP annotation outputs."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


def _documents(path: Path) -> Iterable[dict[str, Any]]:
    files = sorted(path.rglob("annotation.json")) if path.is_dir() else [path]
    if not files:
        raise ValueError(f"no annotation.json files found under {path}")
    for file in files:
        if file.suffix.lower() == ".jsonl":
            with file.open("r", encoding="utf-8") as handle:
                for number, line in enumerate(handle, start=1):
                    if line.strip():
                        value = json.loads(line)
                        if not isinstance(value, dict):
                            raise ValueError(f"{file}:{number}: expected an object")
                        yield value
        else:
            with file.open("r", encoding="utf-8") as handle:
                value = json.load(handle)
            if not isinstance(value, dict):
                raise ValueError(f"{file}: expected an object")
            yield value


def _trajectories(document: dict[str, Any]) -> Iterable[dict[str, Any]]:
    if document.get("schema_version") == "sciarp.annotation.v2":
        items = document.get("trajectories")
    elif "conversation_id" in document and "turn_annotations" in document:
        items = [document]
    else:
        raise ValueError("input is not a SciARP annotation document")
    if not isinstance(items, list):
        raise ValueError("annotation trajectories must be an array")
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("every annotation trajectory must be an object")
        yield item


def _strict_labels(item: dict[str, Any]) -> tuple[bool, bool, bool]:
    turns = item.get("turn_annotations")
    if not isinstance(turns, list) or not turns:
        all_turns_correct = False
    else:
        all_turns_correct = all(
            isinstance(turn, dict) and turn.get("turn_correct") is True
            for turn in turns
        )
    final_correct = item.get("final_correct") is True
    return all_turns_correct and final_correct, all_turns_correct, final_correct


def _summary(items: list[dict[str, Any]]) -> dict[str, Any]:
    labels = [_strict_labels(item) for item in items]
    total = len(labels)
    strict = sum(label[0] for label in labels)
    all_turns = sum(label[1] for label in labels)
    final = sum(label[2] for label in labels)

    def rate(count: int) -> float | None:
        return count / total if total else None

    return {
        "trajectories": total,
        "strict_correct": strict,
        "task_accuracy": rate(strict),
        "all_turns_correct": all_turns,
        "all_turns_correct_rate": rate(all_turns),
        "final_answer_correct": final,
        "final_answer_correct_rate": rate(final),
    }


def compute(path: Path, group_by: list[str]) -> dict[str, Any]:
    items = [item for document in _documents(path) for item in _trajectories(document)]
    result: dict[str, Any] = {
        "metric": "strict_task_accuracy",
        "definition": "final_correct=true AND every turn_correct=true",
        "overall": _summary(items),
    }
    if group_by:
        groups: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
        for item in items:
            metadata = item.get("metadata") if isinstance(item.get("metadata"), dict) else {}
            groups[tuple(metadata.get(field) for field in group_by)].append(item)
        result["group_by"] = group_by
        result["groups"] = [
            {
                "key": dict(zip(group_by, key, strict=True)),
                **_summary(group_items),
            }
            for key, group_items in sorted(groups.items(), key=lambda pair: tuple(str(x) for x in pair[0]))
        ]
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="annotation.json, JSONL, or output directory")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--group-by", nargs="*", default=[])
    args = parser.parse_args()
    result = compute(args.input, args.group_by)
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()

