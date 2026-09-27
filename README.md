# SciARP

SciARP is a benchmark for evaluating the robustness of scientific agents in
multi-turn interactions. This compact release contains **621 scientific
tasks**, one clean dialogue per task, and **14,452 perturbed dialogues** across
the benchmark's perturbation families. `data/dataset.jsonl` therefore contains
**15,073 dialogue records**.

This repository intentionally contains only the components needed to inspect
the dataset, reproduce semantic annotation, and compute the paper-aligned
strict correctness metric.

## Repository layout

```text
SciARP/
├── README.md
├── LICENSE
├── data/
│   ├── dataset.jsonl
│   └── README.md
├── annotation/
│   ├── README.md
│   ├── prompts/
│   └── src/
├── evaluation/
│   ├── compute_metrics.py
│   └── metric_definitions.md
├── examples/
│   └── complete_example.json
└── requirements.txt
```

## Dataset

Each JSONL row is one clean or perturbed multi-turn dialogue. Rows belonging
to the same `task_id` share the same underlying task. Clean rows have
`variant="clean"`; perturbed rows record their subclass and injection count.
The public task index is contiguous from 1 to 621, while
`source_release_task_index` preserves the index in the 632-task working set.

See [data/README.md](data/README.md) for the schema and exclusion record.

## Annotation

The three-pass annotator calls only Anthropic's official Messages API, reads
the API key from `ANTHROPIC_API_KEY`, uses adaptive thinking with effort fixed
to `high`, and stores resumable per-stage checkpoints. No credential or relay
endpoint is included.

See [annotation/README.md](annotation/README.md) for the canonical input format
and commands.

## Evaluation

The paper-aligned Task Accuracy criterion is strict: a trajectory is correct
only when **every annotated assistant turn is correct and the final answer is
correct**. Missing or indeterminate correctness labels do not count as correct.

```bash
python evaluation/compute_metrics.py path/to/annotations --output metrics.json
```

The exact definition is in
[evaluation/metric_definitions.md](evaluation/metric_definitions.md).

## Integrity

SHA-256 of `data/dataset.jsonl`:

```text
392be98b361d829a420b289d4c71d12b9b5cc07436a519c31ec68231b861ad40
```

## Citation

Please cite the accompanying SciARP paper. Bibliographic metadata can be added
here when the archival version is available.

