# Penalized ordinal-likelihood stability analysis

## Source identity and scope

The Independent Ordinal Safety Methods Core reanalysed the same 791 complete
participants, the maximum recorded AESEV across all adverse-event types, the
BCG-versus-Placebo contrast, expected-interaction and patient-volume covariates,
and the raw nonmissing `MHONGO` record count with its treatment interaction.

## Independent estimation method

The core retained the raw count (rather than centering it or replacing it with
an indicator) but fitted a proportional-odds model with a weak ridge penalty
selected by nested cross-validation. The penalty changes the estimation
objective relative to the archived ordinary maximum-likelihood fit.

| Structured quantity | Stability-analysis value |
|---|---:|
| Complete participants | 791 |
| History variable | raw nonmissing MHONGO count |
| Selected ridge penalty | 0.50 |
| BCG main effect at raw MHONGO=0 | 0.4380 |
| BCG x MHONGO coefficient | -0.0210 |
| Derived BCG-versus-Placebo OR at raw MHONGO=0 | exp(0.4380) = 1.55 |

## Reported conflicting result

The methods core recommends the penalized baseline odds ratio of 1.55 for
stability. This is a third analysis object: it preserves the raw-count
covariate but changes the estimator, unlike the centered-history validation
fit and the indicator-coded bootstrap audit. The archived task nevertheless
asks for the ordinary fitted coefficient, whose reported value is 0.490496.
