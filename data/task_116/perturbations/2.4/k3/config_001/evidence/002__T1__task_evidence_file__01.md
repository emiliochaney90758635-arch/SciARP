# BMI response-model grouped likelihood audit

## Source and scope

The Clinical Modeling Audit Unit refitted the BMI-only logistic model after
calibrated BMI-band aggregation.

| BMI band | Responders y | Total n | Fitted probability p |
|---|---:|---:|---:|
| 18.0-19.9 | 8 | 20 | 0.42 |
| 20.0-21.9 | 8 | 18 | 0.47 |
| 22.0-23.9 | 13 | 22 | 0.56 |
| 24.0-25.9 | 12 | 20 | 0.62 |

Compute the grouped Bernoulli log-likelihood
`sum[y ln(p)+(n-y)ln(1-p)]`. The fitted model has an intercept and one BMI
coefficient, so apply `AIC=-2 log L+2k`.
