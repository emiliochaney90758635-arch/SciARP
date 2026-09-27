# Independent cumulative-logit validation memorandum

**Source:** Clinical Statistics Reproducibility Center
**Analysis population:** 791 complete participants
**Outcome:** Highest recorded severity across all adverse-event types, ordered 1 through 4
**Covariates:** Expected interaction and the ordered three-level patient-volume term

The validation implementation models

\[
\log\frac{P(Y>j)}{P(Y\le j)}
=a_j+\gamma_T T^\ast+\gamma_E E+\gamma_P P,
\]

where \(T^\ast=1\) denotes Placebo and \(T^\ast=0\) denotes BCG. The locked fit reports:

| Quantity | Estimate |
|---|---:|
| \(\gamma_T\), Placebo indicator | 0.356675 |
| Standard error | 0.141902 |
| Wald p-value | 0.0119 |

The memorandum states that treatment contrasts must be converted to the requested BCG-versus-Placebo direction before reporting an odds ratio.
