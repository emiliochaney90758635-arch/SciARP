# Evidence for this task

## Outcome, cohort, and model direction

For every subject, maximum `AESEV` is taken over all of that subject's adverse-event records. There is no event-type filter, so the ordered outcome is maximum severity across all adverse events rather than COVID-19-specific severity. Joining the subject outcome to treatment and exposure variables and retaining complete records gives 791 subjects.

The proportional-odds model uses:

| Variable | Encoding |
|---|---|
| Outcome \(Y\) | \(1<2<3<4\) |
| `expect_interact` \(E\) | No = 0, Yes = 1 |
| Treatment \(T\) | Placebo = 0, BCG = 1 |
| `patients_seen` \(P\) | `1-50` = 0, `51-100` = 1, `>100` = 2 |

The full model is \(Y\sim T+E+P\). The complete 791-subject distribution is:

| `expect_interact` | `patients_seen` | `TRTGRP` | `AESEV=1` | `AESEV=2` | `AESEV=3` | `AESEV=4` | Total |
|---|---|---|---:|---:|---:|---:|---:|
| No | 1-50 | BCG | 48 | 82 | 10 | 2 | 142 |
| No | 1-50 | Placebo | 45 | 55 | 4 | 3 | 107 |
| No | 51-100 | BCG | 3 | 8 | 1 | 0 | 12 |
| No | 51-100 | Placebo | 4 | 8 | 1 | 1 | 14 |
| No | >100 | BCG | 3 | 4 | 0 | 0 | 7 |
| No | >100 | Placebo | 0 | 3 | 0 | 0 | 3 |
| Yes | 1-50 | BCG | 87 | 118 | 17 | 5 | 227 |
| Yes | 1-50 | Placebo | 91 | 81 | 7 | 3 | 182 |
| Yes | 51-100 | BCG | 16 | 21 | 0 | 2 | 39 |
| Yes | 51-100 | Placebo | 25 | 15 | 2 | 1 | 43 |
| Yes | >100 | BCG | 3 | 6 | 0 | 1 | 10 |
| Yes | >100 | Placebo | 3 | 1 | 1 | 0 | 5 |
| Total |  |  | 328 | 402 | 43 | 18 | 791 |

## Fitted quantity and conversion

For the `expect_interact` predictor:

| Quantity | Value |
|---|---:|
| Log-odds coefficient \(\hat\beta_E\) | -0.281063 |
| Standard error | approximately 0.144 |
| Nominal Wald p-value | approximately 0.05163 |

For a fitted coefficient whose exponentiated Yes-versus-No odds ratio is below one, convert it to a percentage reduction with

\[
(1-e^{\hat\beta_E})\times100\%.
\]

This describes the fitted odds of being in a higher maximum-`AESEV` category.

## Interpretation boundary

The proportional-odds assumption was not tested, and `patients_seen` is treated as one equally spaced integer predictor. The value is a model-dependent adjusted association, not a causal effect; its nominal p-value is slightly above 0.05.

# Expected Clinical Interaction and Reduced Maximum Adverse-Event Severity

**Authors:** Kristina L. Moen, Samuel B. Adeyemi, Rina Velázquez, and Mark H. Fielding

**Abstract**

**Background:** Expected interaction with patients may influence both occupational exposure and the reporting context of adverse events among healthcare personnel. **Methods:** We defined an ordinal participant-level endpoint as the highest severity grade across all recorded adverse-event types. Complete AE and demographic records were fitted with a proportional-odds logistic model containing randomized treatment, expected interaction, and the prespecified integer score for patient volume. **Results:** Participants expecting patient interaction had 41.0% lower adjusted odds of occupying a higher maximum-severity category than participants reporting no expected interaction (nominal \(p=0.017\)). The direction was preserved in treatment-stratified analyses. **Conclusions:** Expected patient interaction was associated with a lower maximum all-event severity profile. The estimate is an adjusted observational association and does not establish causality.
