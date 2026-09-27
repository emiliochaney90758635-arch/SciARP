# Independent penalized-logistic BMI audit

## Source, scope, and fitted quantities

The Clinical Prediction Validation Center fitted a Firth-penalized logistic
response model to the same 80 BMI observations. Its penalized log-likelihood
and effective parameter count were:

| model | n | penalized log-likelihood | effective k |
|---|---:|---:|---:|
| response on BMI with intercept | 80 | -52.31 | 2.40 |

Using the center's criterion `-2 penalized log L + 2 effective k` gives
`104.62+4.80=109.42`. This is a penalized external analysis, not the archived
ordinary maximum-likelihood GLM.
