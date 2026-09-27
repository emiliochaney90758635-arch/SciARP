# Bayesian age-effect model report

## Source identity and scope

The Bayesian Immunotherapy Modeling Collaborative fitted a univariable age model for the same binary efficacy-PR endpoint in an independent complete-case cohort spanning ages 40–75.

## Method

A logistic likelihood with an intercept and one-year age predictor was combined with weakly regularizing normal priors. Hamiltonian Monte Carlo produced the posterior for the age coefficient on the log-odds scale.

## Structured observations

| posterior quantity | value |
|---|---:|
| posterior mean age coefficient | -0.06120 |
| posterior median | -0.06084 |
| posterior SD | 0.02110 |
| 95% credible interval | [-0.1030, -0.0207] |
| effective sample size | 4,860 |

## Derived conflicting result

The collaborative reports **-0.06120 log-odds per year** as its posterior effect estimate. This Bayesian posterior coefficient is independent of the external five-year registry odds ratio and the linear-probability slope. It does not replace the archive's maximum-likelihood age coefficient.
