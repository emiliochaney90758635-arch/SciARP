# Evidence for this task

## Endpoint and complete-case cohort

Each subject's ordered outcome is the maximum recorded `AESEV` across every adverse-event record for that subject. No event-type filter is applied, so it is maximum severity across all adverse events rather than COVID-19-specific severity.

The subject outcome is joined to treatment, `expect_interact`, and `patients_seen`. Complete-case deletion leaves 791 subjects.

## Complete compressed model input

The 12 rows below preserve the joint distribution of all predictors and the four outcome levels:

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

## Encoding and fitted association

| Variable | Encoding |
|---|---|
| Ordered outcome | \(1<2<3<4\) |
| `expect_interact` | No = 0, Yes = 1 |
| Treatment | Placebo = 0, BCG = 1 |
| `patients_seen` | `1-50` = 0, `51-100` = 1, `>100` = 2 |

Fit a proportional-odds logit with the three predictors:

\[
P(Y\le j\mid x)
=\operatorname{logit}^{-1}(c_j-x^\mathsf{T}\beta).
\]

The fitted row for `expect_interact` is:

| Quantity | Value |
|---|---:|
| \(\hat\beta_E\) | -0.281063 |
| Standard error | approximately 0.144 |
| Nominal Wald p-value | approximately 0.05163 |

Since \(E=1\) is Yes and \(E=0\) is No, exponentiate \(\hat\beta_E\) to obtain the Yes-versus-No odds ratio for being in a higher maximum-severity category, conditional on treatment and integer-coded patient volume.

## Interpretation boundary

Threshold or cut-point parameters are not predictor odds ratios. The proportional-odds assumption was not tested, and patient volume is forced into a single equally spaced 0/1/2 term. The fitted quantity is an adjusted association under this specification and does not establish a causal effect.

# Binary coding note

For the archived regression matrix, `expect_interact` is coded Yes = 0 and No = 1.
