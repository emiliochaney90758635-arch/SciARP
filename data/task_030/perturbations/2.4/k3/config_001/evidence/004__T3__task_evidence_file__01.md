# Claims-derived patient-contact volume analysis

**Source:** Health-System Encounters Reconciliation Service, linkage report
`HSERS-030-CY`

**Scope:** Complete randomized participants with a subject-level maximum over
all recorded adverse-event `AESEV` values. Treatment assignment and the safety
endpoint were retained; patient-contact volume was independently reconstructed
from billed face-to-face encounters in the preceding calendar year.

**Method:** Unique patient encounter identifiers were deduplicated within
provider and assigned to 1-50, 51-100, and >100 annual-contact bands. Within
each claims-derived band, the service cross-tabulated severity levels 1-4 by
BCG and Placebo and applied a separate ordinary Pearson chi-square test.

## Claims-derived severity by treatment tables

```text
1-50:   (130,130), (165,150), (22,17), (8,8)
51-100: (25,20),   (32,26),   (4,3),   (1,2)
>100:   (3,8),     (9,3),     (0,3),   (2,0)
```

Each ordered pair is `(BCG, Placebo)` for severity levels 1 through 4.

| Claims-derived band | Pearson chi-square | df | Unadjusted p-value |
|---|---:|---:|---:|
| 1-50 | 0.7211175 | 3 | 0.8682260 |
| 51-100 | 0.5872036 | 3 | 0.8993555 |
| >100 | 10.2727273 | 3 | 0.0163846 |

This report identifies only the >100 claims-derived band at the nominal 0.05
threshold. Its exposure source is independent of both follow-up self-report
and supervisor coding, and it is not the archived `patients_seen` variable
specified by the task.
