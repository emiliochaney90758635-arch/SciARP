# SciARP

SciARP is a benchmark for evaluating the robustness of scientific agents in
multi-turn interactions. This compact release contains **621 scientific
tasks**, one clean dialogue per task, and **14,452 perturbed dialogues** across
the benchmark's perturbation families: **15,073 dialogue records** in total.

This repository intentionally contains only the components needed to inspect
the dataset, reproduce semantic annotation, and compute the paper-aligned
task- and process-level metrics.

## Repository layout

```text
SciARP/
├── README.md
├── LICENSE
├── data/
│   ├── README.md
│   ├── task_001/
│   ├── task_002/
│   └── ...                 # 621 task folders in total
├── annotation/
│   ├── README.md
│   ├── prompts/
│   └── src/
├── evaluation/
│   └── compute_metrics.py
├── examples/
│   └── complete_example.json
└── requirements.txt
```

## Dataset

Each `data/task_NNN/` directory contains the clean dialogue, evidence when
applicable, and all released perturbation configurations for one scientific
task. The task numbers preserve the original 632-task working-release indices;
the 11 excluded task numbers are intentionally absent.

See [data/README.md](data/README.md) for the schema and exclusion record.

## Annotation

The three-pass annotator calls only Anthropic's official Messages API, reads
the API key from `ANTHROPIC_API_KEY`, uses adaptive thinking with effort fixed
to `high`, and stores resumable per-stage checkpoints. No credential or relay
endpoint is included.

See [annotation/README.md](annotation/README.md) for the canonical input format
and commands.

## Evaluation

The evaluator computes Task Accuracy (TACC), Information Correctness (IC),
Task Progression (TP), and Reasoning Validity (RV), plus the paper's position,
frequency, localization, and propagation analyses. TACC is strict: every
annotated assistant turn and the final answer must be correct. Process metrics
begin at the first injected turn, use the same window for the paired clean
trajectory, and are macro-averaged without sample weighting.

```bash
python evaluation/compute_metrics.py path/to/merged_annotations \
  --output-dir evaluation/results
```

The complete metric definitions and aggregation rules are implemented directly
in `evaluation/compute_metrics.py`.

## Citation

Please cite the accompanying SciARP paper. Bibliographic metadata can be added
here when the archival version is available.
