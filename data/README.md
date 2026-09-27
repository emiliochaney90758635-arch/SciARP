# Dataset

`dataset.jsonl` has one JSON object per dialogue. The release contains:

| Item | Count |
|---|---:|
| Unique tasks | 621 |
| Clean dialogues | 621 |
| Perturbed dialogues | 14,452 |
| Total dialogue records | 15,073 |

## Record schema

Core fields are:

- `schema_version`: `sciarp.dataset.v1`;
- `record_id` / `conversation_id`: stable dialogue identity;
- `release_task_index`: contiguous public index in `[1, 621]`;
- `source_release_task_index`: index in the 632-task working release;
- `task_id`, `source_id`, `dataset`, `ordinal`: source-task identity;
- `variant`: `clean` or `perturbed`;
- `family`, `subclass`, `paper_subclass`, `condition_label`;
- `injection_count`: zero for clean dialogues and the number of injections for
  perturbed dialogues;
- `dialogue.turns`: ordered visible user turns with `turn_id`, `role`, and
  `content`;
- `dialogue_sha256` and `semantic_condition_id`: integrity/condition IDs.

Evidence-grounded tasks embed the evidence in the dialogue text so that the
JSONL file is self-contained.

## Exclusions and the 621-task paper set

The current 632-task working release contained eight of the historical
safety-exclusion IDs. They were removed:

```text
gpqa__recBwjJkJt6eYhwtH
gpqa__recKrsh0017X31QJK
gpqa__recQNTlpypNM242Wl
gpqa__recbPC4IXtJgrsrUl
gpqa__recdhG9IdiPi8yZPM
gpqa__receXrYDOlmIPLiKz
gpqa__reclQLhiYDIkCnybe
gpqa__reclkg2VdPopXQr1G
```

Three other historical safety IDs were already absent from this materialized
working release. To obtain exactly 621 tasks without outcome-based selection,
the three remaining tasks with the lowest perturbation coverage (1, 2, and 2
perturbed dialogues) were removed as a preregistered completeness filter:

```text
gpqa__recCJJOeBGERaHYax
gpqa__recmZvZDl0F55xR3r
gpqa__recIN1LyuCWtFwrJ4
```

This filter uses configuration coverage only; it does not use model outputs or
evaluation scores.

## Upstream data notice

The release includes tasks originating from BixBench, GPQA, OlympiadBench, and
SciBench. Users are responsible for complying with the licenses and terms of
the corresponding upstream datasets. The repository's MIT license does not
relicense third-party task content.

