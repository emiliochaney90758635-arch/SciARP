# Evidence for This Task

## Participant-Level Analysis Data

- AE table: take the maximum `AESEV` across all adverse-event records for each `USUBJID`.
- DM table: retain `patients_seen` and `expect_interact`.
- MH table: use pandas `count()` by `USUBJID, TRTGRP` to count every non-null `MHONGO` record, including source values `Yes` and `No`.

After merging and removing missing values, 791 unique participants remain:

| Field | Distribution |
|---|---|
| maximum recorded `AESEV` | 1: 328; 2: 402; 3: 43; 4: 18 |
| `TRTGRP` | Placebo: 354; BCG: 437 |
| `expect_interact` | No: 285; Yes: 506 |
| `patients_seen` | 1-50: 658; 51-100: 108; >100: 25 |
| nonmissing `MHONGO` count | 0: 316; 1: 232; 2: 130; 3: 76; 4: 28; 5: 8; 6: 1 |

Coding is Placebo=0 and BCG=1; `expect_interact` is No=0/Yes=1; `patients_seen` is 1-50=0, 51-100=1, and >100=2; the interaction term is `MHONGO × TRTGRP_cat`.

## Ordinal-Logit Model Output

The model is:

```text
AESEV ~ TRTGRP_cat
        + expect_interact_cat
        + patients_seen_cat
        + MHONGO
        + MHONGO_TRTGRP
```

| term | coefficient | std err | p-value | 95% coefficient CI |
|---|---:|---:|---:|---|
| TRTGRP_cat | 0.4904958818544001 | 0.192479 | 0.0108246 | [0.113244, 0.867748] |
| expect_interact_cat | -0.29676910531625555 | 0.145484 | 0.0413631 | [-0.581913, -0.011625] |
| patients_seen_cat | 0.018993805637804256 | 0.148003 | 0.8978849 | [-0.271087, 0.309075] |
| MHONGO | 0.30169744665764675 | 0.0863306641501545 | 0.0004746428 | [0.1324924542, 0.4709024392] |
| MHONGO_TRTGRP | -0.00264462830555004 | 0.1205446677333133 | 0.9824966 | [-0.2389, 0.2336] |

Placebo is the treatment reference group, so the `MHONGO` main effect is the log-odds slope for a 1-record increase in the nonmissing count within Placebo. The conversion is:

\[
\mathrm{OR}=\exp(\beta),\qquad
\%\Delta\mathrm{odds}=(\mathrm{OR}-1)\times100\%
\]
