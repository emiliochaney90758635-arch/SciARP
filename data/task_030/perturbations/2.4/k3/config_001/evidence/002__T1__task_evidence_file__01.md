# Follow-up occupational-volume analysis tables

**Source:** Healthcare Exposure Survey Unit
**Endpoint:** Maximum severity across all recorded adverse events per complete subject
**Stratification:** Mean weekly patient contacts reported at follow-up, categorized as 1–50, 51–100, or >100

## Severity rows × treatment columns (`BCG`, `Placebo`)

```text
1–50:
severity 1: 140, 130
severity 2: 170, 160
severity 3: 20, 22
severity 4: 6, 10

51–100:
severity 1: 22, 25
severity 2: 25, 27
severity 3: 3, 4
severity 4: 2, 2

>100:
severity 1: 6, 0
severity 2: 1, 8
severity 3: 0, 4
severity 4: 3, 0
```

Each stratum is tested separately with an ordinary 4×2 Pearson calculation and nominal threshold 0.05. No multiplicity correction is applied in the table-level screen.
