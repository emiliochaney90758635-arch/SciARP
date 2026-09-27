# Centered-history ordinal-model validation

**Source:** Clinical Modelling Review Group, validation fit `CMRG-AE-791C`
**Scope:** 791 complete participants; maximum recorded AESEV
**Method:** The same covariates were fitted with proportional odds, but medical-history count was centered at 2.4 records: `MH_c = MHONGO - 2.4`.

| Term | Coefficient |
|---|---:|
| BCG main effect at `MH_c = 0` | 0.360 |
| `BCG × MH_c` | -0.080 |

For a raw history count \(m\), the validation treatment log-odds effect is \(0.360+(m-2.4)(-0.080)\). The odds ratio is obtained by exponentiating the effect at the requested raw count.
