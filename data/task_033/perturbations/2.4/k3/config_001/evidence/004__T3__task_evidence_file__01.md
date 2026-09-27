# Penalized proportional-odds stability report

**Source:** Ordinal Clinical Models Stability Consortium, report `OCMSC-RIDGE-033`
**Scope:** The same 791 complete participants, maximum recorded all-event `AESEV` ordered 1 through 4, BCG-versus-Placebo treatment, expected interaction, and the ordered 0/1/2 patient-volume term
**Method:** The consortium used the same cumulative-logit direction and BCG indicator as the archived fit but maximized a ridge-penalized proportional-odds likelihood. The penalty was selected by nested cross-validation.

## Locked stability fit

| Quantity | Value |
|---|---:|
| Complete participants | 791 |
| Selected ridge penalty | 0.25 |
| Penalized BCG coefficient | 0.300105 |
| Penalized coefficient standard error | 0.1320 |
| Derived BCG-versus-Placebo odds ratio | (exp(0.300105)=1.350) |

The consortium recommends 1.350 as a shrinkage-stability estimate. It is not the ordinary unpenalized archived coefficient (0.4214970660) requested by the task.
