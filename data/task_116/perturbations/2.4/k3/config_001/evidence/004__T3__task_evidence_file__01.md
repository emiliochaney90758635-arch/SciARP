# Independent probit-link BMI model audit

## Source identity and scope

The Clinical Link-Function Verification Network analyzed the same 80 complete BMI/response observations and the same `Response=1` PR endpoint. Its purpose was to assess sensitivity to the response-link function.

## Method

An intercept-inclusive binomial generalized linear model was fitted with a **probit** link rather than the archive's logit link. Maximum likelihood was used and both the intercept and BMI slope were counted as fitted parameters.

## Structured observations

| quantity | value |
|---|---:|
| observations | 80 |
| fitted parameters, k | 2 |
| maximized probit-model log-likelihood | -53.2400 |
| `-2 log L` | 106.4800 |
| `AIC=-2 log L+2k` | 110.4800 |

## Derived conflicting result

The network reports an AIC of **110.48** for its probit-link sensitivity model. The scientific object is a link-function audit, distinct from the earlier grouped-likelihood and Firth-penalized fits. The task explicitly requests the archived ordinary logistic model, whose fitted log-likelihood and AIC remain available.
