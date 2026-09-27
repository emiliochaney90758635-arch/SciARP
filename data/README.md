# Dataset

This directory contains one folder per released scientific task. The release
contains:

| Item | Count |
|---|---:|
| Unique tasks | 621 |
| Clean dialogues | 621 |
| Perturbed dialogues | 14,452 |
| Total dialogue records | 15,073 |

## Directory structure

Each task follows this structure (available files vary by task and condition):

```text
task_NNN/
├── base_dialogue.json
├── evidence/                       # present for evidence-grounded tasks
│   ├── evidence_manifest.json
│   └── ...
└── perturbations/
    ├── index.json
    └── SUBCLASS/
        └── kN/
            └── config_NNN/
                ├── dialogue.json
                ├── perturbation_spec.json
                ├── review.json
                └── evidence/       # present when required
```

`base_dialogue.json` contains the common clean multi-turn task.
`dialogue.json` contains one perturbed configuration; its metadata records the
subclass, condition label, injection count, and stable conversation identity.
`perturbation_spec.json` records the intended injection construction, while
`review.json` preserves the release-quality decision. Evidence files are
included rather than referenced through machine-local paths.

Task-folder numbers preserve their indices in the 632-task working release.
There are exactly 621 `task_*` directories; numbers corresponding to excluded
tasks are deliberately absent rather than silently renumbered.

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
