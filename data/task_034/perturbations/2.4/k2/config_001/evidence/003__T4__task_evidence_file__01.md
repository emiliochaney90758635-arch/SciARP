# Trial Data Coordination Unit reproduction report

## Source and scope

Source: Trial Data Coordination Unit, frozen AE/DM linkage release. Scope: all adverse-event types, subject-level maximum `AESEV`, and the 791 records complete for treatment, expected interaction, and patient volume.

## Method

The unit coded expected interaction No=0/Yes=1, treatment Placebo=0/BCG=1, and patient volume 1-50=0, 51-100=1, >100=2. It reconstructed the 12-cell predictor cube and fitted a proportional-odds logit with all three predictors.

## Structured observations

| Quantity | Reported value |
|---|---:|
| Complete subjects | 791 |
| Yes-versus-No coefficient | -0.510826 |
| Standard error | 0.151900 |
| Nominal Wald p-value | 0.00077 |
| Higher-category odds ratio | 0.600000 |

## Result

The unit concludes that expected interaction is associated with 40.0% lower adjusted odds of a higher maximum-severity category; it explicitly treats the result as noncausal.
