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


## Citation

Please cite the accompanying SciARP paper. Bibliographic metadata can be added
here when the archival version is available.
