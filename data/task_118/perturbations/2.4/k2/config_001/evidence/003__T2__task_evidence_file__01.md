# Penalized age-only response audit

## Source identity, scope, method, and fitted observations

The Independent Oncology Statistics Unit fitted a Firth-penalized logistic
model with intercept and age to the 80 valid patient records.

| n | penalized log-likelihood | effective parameter count |
|---:|---:|---:|
| 80 | -49.41 | 2.35 |

## Derived conflicting result

Its penalized information criterion is
`-2*(-49.41)+2*(2.35)=103.52`. This is a Firth fit, not the ordinary archived
maximum-likelihood GLM.
