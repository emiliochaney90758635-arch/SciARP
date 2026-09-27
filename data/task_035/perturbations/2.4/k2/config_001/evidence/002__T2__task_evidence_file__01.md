# Multicenter ordinal sensitivity report

**Source:** Vaccine Safety Modeling Consortium
**Population:** Complete participants with treatment, expected-interaction, and patient-volume fields
**Endpoint:** Maximum recorded severity over every adverse-event type
**Contrast:** Expected interaction Yes versus No

The consortium fitted a cumulative-logit mixed model with fixed effects for treatment, expected interaction, and the integer-coded patient-volume score, plus a random intercept for recruiting center. For the expected-interaction term it reports:

| Quantity | Estimate |
|---|---:|
| Log proportional-odds coefficient | -0.430783 |
| Standard error | 0.169205 |
| Nominal Wald p-value | 0.0109 |

The reported coefficient uses the convention that exponentiation gives the Yes-versus-No odds ratio for a higher outcome category.
