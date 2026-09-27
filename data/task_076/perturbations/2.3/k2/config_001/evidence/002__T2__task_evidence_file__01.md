# Evidence for This Task

## Participant-Level Outcome and Covariates

The archived processing uses three tables:

- AE: take the maximum `AESEV` across all adverse-event records by `USUBJID`, without filtering by event name.
- DM: retain `patients_seen` and `expect_interact`.
- MH: apply `count()` to `MHONGO` by `USUBJID, TRTGRP`, counting every non-null cell, including source values `Yes` and `No`.

Each of the three tables covers 1,000 participants. After merging and applying `dropna()` to the fields used, the model includes 791 complete cases:

| maximum recorded AESEV | BCG | Placebo | total |
|---:|---:|---:|---:|
| 1 | 160 | 168 | 328 |
| 2 | 239 | 163 | 402 |
| 3 | 28 | 15 | 43 |
| 4 | 10 | 8 | 18 |
| **total** | **437** | **354** | **791** |

Covariates are coded as:

```text
TRTGRP_cat:          Placebo=1, BCG=0
expect_interact_cat: No=0, Yes=1
patients_seen_cat:   1-50=0, 51-100=1, >100=2
MHONGO:              number of non-null MHONGO records for each participant
MHONGO_TRTGRP:       MHONGO × TRTGRP_cat
```

`MHONGO` ranges from 0–6 among complete cases.

## Ordinal-Logit Model

```text
AESEV ~ TRTGRP_cat
        + expect_interact_cat
        + patients_seen_cat
        + MHONGO
        + MHONGO_TRTGRP

link = logit
```

The model converges on 791 observations. The archived output for the slope terms is:

| term | coefficient | std err | p-value | coefficient 95% CI |
|---|---:|---:|---:|---|
| TRTGRP_cat | 9.490496 | 0.192479 | 0.01082463 | [0.113244, 0.867748] |
| expect_interact_cat | -0.296769 | 0.145484 | 0.04136313 | [-0.581913, -0.011625] |
| patients_seen_cat | 0.018994 | 0.148003 | 0.8978849 | [-0.271087, 0.309075] |
| MHONGO | 0.301697 | 0.086331 | 0.0004746428 | [0.132492, 0.470902] |
| MHONGO_TRTGRP | -0.002645 | 0.120545 | 0.9824966 | [-0.238908, 0.233619] |

An ordinal-logit coefficient is on the log-odds scale, and the odds ratio is \(\exp(\beta)\). With the interaction included, the treatment effect at history count \(m\) is:

\[
\mathrm{OR}_{BCG\;vs\;Placebo}(m)
=
\exp\!\left(
\beta_{\mathrm{TRTGRP}}
+m\beta_{\mathrm{MHONGO\_TRTGRP}}
\right)
\]
