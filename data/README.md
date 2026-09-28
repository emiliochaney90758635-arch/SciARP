# SciARP Data

## Dataset Statistics

| Item | Count |
|---|---:|
| Tasks | 621 |
| Base dialogues | 621 |
| Perturbed dialogues | 14,452 |
| Perturbation subclasses | 13 |
| Injection-frequency levels | 4 |
| Evidence Markdown files | 7,483 |

### Perturbed Dialogues by Subclass

| Subclass | Count |
|---|---:|
| 1.1 | 5,232 |
| 1.2 | 1,302 |
| 1.3 | 1,632 |
| 1.4 | 1,220 |
| 2.1 | 414 |
| 2.2 | 414 |
| 2.3 | 409 |
| 2.4 | 414 |
| 3.1 | 870 |
| 3.2 | 301 |
| 3.3 | 850 |
| 4.1 | 515 |
| 4.2 | 879 |

### Perturbed Dialogues by Injection Frequency

| Injection frequency | Count |
|---|---:|
| k1 | 6,091 |
| k2 | 4,513 |
| k3 | 3,346 |
| k4 | 502 |

## File Structure

```text
data/
├── README.md
├── task_001/
│   ├── base_dialogue.json
│   ├── evidence/
│   │   ├── 001__T1__task_evidence__01.md
│   │   └── evidence_manifest.json
│   └── perturbations/
│       ├── 1.1/
│       │   ├── k1/
│       │   │   └── config_001.../
│       │   │       ├── dialogue.json
│       │   │       ├── perturbation_spec.json
│       │   │       ├── review.json
│       │   │       └── evidence/
│       │   │           ├── 001__T1__task_evidence__01.md
│       │   │           └── evidence_manifest.json
│       │   ├── k2/
│       │   ├── k3/
│       │   └── k4/
│       ├── 1.2/
│       ├── 1.3/
│       ├── 1.4/
│       ├── 2.1/
│       ├── 2.2/
│       ├── 2.3/
│       ├── 2.4/
│       ├── 3.1/
│       ├── 3.2/
│       ├── 3.3/
│       ├── 4.1/
│       └── 4.2/
├── task_002/
├── ...
└── task_632/
```
