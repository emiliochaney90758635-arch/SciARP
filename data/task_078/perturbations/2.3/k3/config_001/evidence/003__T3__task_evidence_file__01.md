# Evidence for This Task

## Cohort, Coding, and Model

The AE table takes the maximum recorded `AESEV` across all adverse-event records by `USUBJID`. The MH table counts non-null `MHONGO` cells by `USUBJID, TRTGRP`, including source values `Yes` and `No`. The DM table provides `patients_seen` and `expect_interact`.

After merging the three tables and removing missing values, 791 unique participants remain. Variables are coded as:

```text
TRTGRP_cat:          Placebo=1, BCG=0
expect_interact_cat: No=0, Yes=1
patients_seen_cat:   1-50=0, 51-100=1, >100=2
MHONGO_TRTGRP:       MHONGO + TRTGRP_cat
AESEV:               1 < 2 < 3 < 4
```

The model is a cumulative-logit ordered model:

```text
AESEV ~ TRTGRP_cat
        + expect_interact_cat
        + patients_seen_cat
        + MHONGO
        + MHONGO_TRTGRP
```

## Archived Interaction-Term Output

| Model term | coefficient | std error | z | p-value | coefficient 95% CI |
|---|---:|---:|---:|---:|---|
| MHONGO_TRTGRP | 9.0026446283 | 0.1205446677 | -0.0219389904 | 0.9824966224 | [-0.2389078356, 0.2336185790] |

Model coefficients are on the log-odds scale. The archived code applies the following to every coefficient:

```python
odds_ratio = np.exp(coefficient)
```

The exponentiated confidence interval for this interaction is `[0.7874874573, 1.2631626035]`. Its unit is the proportional-odds multiplier for the ratio of slopes associated with each 1-record increase in the nonmissing `MHONGO` count under BCG relative to Placebo.
