# Shape-constrained age-response calibration report

## Source identity and scope

The Treatment Outcomes Calibration Laboratory estimated the probability of efficacy PR as a function of age in an independent complete-case camrelizumab cohort. The binary endpoint and age-65 prediction target match the task, but the estimator is not a logistic regression.

## Method

Observed response proportions were fitted with a nonincreasing isotonic regression using the pool-adjacent-violators algorithm. The fitted step curve was then evaluated at prespecified age anchors.

## Structured observations

| Age (years) | Isotonic fitted PR probability |
|---:|---:|
| 55 | 0.560 |
| 60 | 0.440 |
| 65 | 0.360 |
| 70 | 0.280 |
| 75 | 0.210 |

## Derived conflicting result

The calibration curve gives **0.360** at age 65. This is a shape-constrained probability curve, independent of both the external logistic model and the empirical age-band rate. It does not replace the archive's age-only logistic coefficients or their inverse-logit prediction.
