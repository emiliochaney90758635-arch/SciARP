# Evidence for this task

## Subject-level construction

The adverse-event source has 2,694 records and 1,000 unique `USUBJID` values. For each subject, duplicate selected rows are removed and maximum `AESEV` is taken over all adverse-event records. There is no `AEPT` or `AECAT` filter, so the four-level ordered endpoint is maximum severity across all recorded adverse events, not COVID-19-specific severity.

The subject outcome is joined by `USUBJID` to a 1,000-subject table containing `patients_seen` and `expect_interact`. Of the joined subjects, 209 have missing `AESEV`; an unqualified complete-case deletion leaves 791 model records.

## Encodings and compressed model matrix

| Symbol | Variable | Encoding |
|---|---|---|
| \(Y\) | maximum `AESEV` | \(1<2<3<4\) |
| \(T\) | treatment | Placebo = 0, BCG = 1 |
| \(E\) | `expect_interact` | No = 0, Yes = 1 |
| \(P\) | `patients_seen` | `1-50` = 0, `51-100` = 1, `>100` = 2 |

The nonzero joint frequencies below exactly reconstruct all 791 rows when each row is repeated `n` times:

| T | E | P | Y | n |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 | 45 |
| 0 | 0 | 0 | 2 | 55 |
| 0 | 0 | 0 | 3 | 4 |
| 0 | 0 | 0 | 4 | 3 |
| 0 | 0 | 1 | 1 | 4 |
| 0 | 0 | 1 | 2 | 8 |
| 0 | 0 | 1 | 3 | 1 |
| 0 | 0 | 1 | 4 | 1 |
| 0 | 0 | 2 | 2 | 3 |
| 0 | 1 | 0 | 1 | 91 |
| 0 | 1 | 0 | 2 | 81 |
| 0 | 1 | 0 | 3 | 7 |
| 0 | 1 | 0 | 4 | 3 |
| 0 | 1 | 1 | 1 | 25 |
| 0 | 1 | 1 | 2 | 15 |
| 0 | 1 | 1 | 3 | 2 |
| 0 | 1 | 1 | 4 | 1 |
| 0 | 1 | 2 | 1 | 3 |
| 0 | 1 | 2 | 2 | 1 |
| 0 | 1 | 2 | 3 | 1 |
| 1 | 0 | 0 | 1 | 48 |
| 1 | 0 | 0 | 2 | 82 |
| 1 | 0 | 0 | 3 | 10 |
| 1 | 0 | 0 | 4 | 2 |
| 1 | 0 | 1 | 1 | 3 |
| 1 | 0 | 1 | 2 | 8 |
| 1 | 0 | 1 | 3 | 1 |
| 1 | 0 | 2 | 1 | 3 |
| 1 | 0 | 2 | 2 | 4 |
| 1 | 1 | 0 | 1 | 87 |
| 1 | 1 | 0 | 2 | 118 |
| 1 | 1 | 0 | 3 | 17 |
| 1 | 1 | 0 | 4 | 5 |
| 1 | 1 | 1 | 1 | 16 |
| 1 | 1 | 1 | 2 | 21 |
| 1 | 1 | 1 | 4 | 2 |
| 1 | 1 | 2 | 1 | 3 |
| 1 | 1 | 2 | 2 | 6 |
| 1 | 1 | 2 | 4 | 1 |

## Proportional-odds fit

The specified logit model is

\[
P(Y\le j\mid x)
=\operatorname{logit}^{-1}(c_j-x^\mathsf{T}\beta),
\]

with predictors \(T,E,P\). A positive treatment coefficient therefore shifts probability toward higher outcome categories. Fitting the 791 reconstructed observations gives:

| Treatment quantity | Value |
|---|---:|
| \(\hat\beta_T\) | 0.4214970660 |
| Standard error | 0.139896 |
| Nominal Wald p-value | 0.002587392 |

Because \(T=1\) denotes BCG and \(T=0\) denotes Placebo, obtain the requested conditional proportional odds ratio by exponentiating the fitted treatment coefficient.

## Interpretation boundary

The endpoint is the maximum of all adverse events rather than a COVID-19-specific severity measure. The proportional-odds assumption was not tested, and the three patient-volume categories enter as one equally spaced 0/1/2 linear term rather than as two indicator variables. This is a model-dependent adjusted association, not a causal treatment effect.

# Ordered-logit direction convention

For the displayed cumulative-logit parameterization \(P(Y\le j\mid x)=\operatorname{logit}^{-1}(c_j-x^\mathsf{T}\beta)\), a positive treatment coefficient shifts probability toward lower `AESEV` categories.
