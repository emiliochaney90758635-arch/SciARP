# Bayesian regularized proportional-odds analysis

## Source identity and scope

The Bayesian Vaccine Safety Analysis Group used the same 791 complete
participants, maximum recorded AESEV over all adverse-event types,
Yes-versus-No expected-interaction contrast, BCG adjustment, and integer-coded
patient-volume adjustment.

## Independent estimation method

The group fitted the same cumulative-logit linear predictor but used weakly
regularizing Normal(0, 0.5^2) priors on predictor coefficients and integrated
over the posterior rather than maximizing the ordinary likelihood.

| Posterior quantity | Value |
|---|---:|
| Complete participants | 791 |
| Posterior mean, Yes-versus-No coefficient | -0.174353 |
| Posterior standard deviation | 0.1268 |
| Posterior probability coefficient < 0 | 0.915 |
| Posterior mean higher-category OR | 0.8400 |
| Implied odds reduction | 16.0% |

## Reported conflicting result

The group reports a 16.0% lower Yes-versus-No higher-category odds under its
regularized posterior summary. This is a third scientific object: Bayesian
regularized estimation. It differs from E1's center-random-intercept mixed
model and E2's ordinary fixed-effect reconstruction. The archived task
requires the ordinary proportional-odds maximum-likelihood result.
