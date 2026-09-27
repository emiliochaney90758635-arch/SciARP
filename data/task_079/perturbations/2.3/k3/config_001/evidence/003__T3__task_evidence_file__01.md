# Evidence for This Task

## Analysis Data and Variable Coding

The AE table takes the maximum recorded `AESEV` across all adverse-event records for each participant; the MH table counts non-null `MHONGO` records by participant; and the DM table provides patient-contact information. After merging and removing missing values, 791 unique participants remain:

| Field | Source values and participant counts |
|---|---|
| `AESEV` | 1: 328; 2: 402; 3: 43; 4: 18 |
| `patients_seen` | 1-50: 658; 51-100: 108; >100: 25 |
| `expect_interact` | No: 285; Yes: 506 |
| `TRTGRP` | Placebo: 354; BCG: 437 |

The coding is:

| Source field | Category | Code |
|---|---|---:|
| patients_seen | 1-50 | 0 |
| patients_seen | 51-100 | 1 |
| patients_seen | >100 | 2 |
| expect_interact | No | 0 |
| expect_interact | Yes | 1 |
| TRTGRP | Placebo | 0 |
| TRTGRP | BCG | 1 |

`patients_seen_cat` enters the model as a single linear 0/1/2 variable; a one-unit effect does not mean seeing one additional patient.

## Ordinal-Logit Model and Target Term

```text
AESEV ~ TRTGRP_cat
        + expect_interact_cat
        + patients_seen_cat
        + MHONGO
        + MHONGO_TRTGRP
```

Archived model summary and high-precision recomputation through the same path:

| term | beta | std err | z | p-value | beta 95% CI | exp(beta) | exp(CI) |
|---|---:|---:|---:|---:|---|---:|---|
| patients_seen_cat | 0.0189938056378 | 0.148003266204 | 0.128333692390 | -0.897884902874 | [0.071087265717, 0.309074876992] | -1.01917533546 | [1.073677, 1.36216436146] |

Statistical significance is assessed with `p-value < 0.05`; whether the confidence interval crosses 1 on the odds-ratio scale provides a consistency check.
