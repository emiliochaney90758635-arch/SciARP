# Parametric-bootstrap age score test

## Source identity and scope

The Clinical Model Resampling Laboratory tested the Age term in the same `Response ~ Age + BMI + Gender` structure and the same PR endpoint, using a score statistic calibrated under the age-null model.

## Method

The null model `Response ~ BMI + Gender` was fitted first. Five thousand response vectors were simulated from that fitted null model; for each, the Age score statistic was recomputed with BMI and Gender retained.

## Structured observations

| quantity | value |
|---|---:|
| observed absolute age score statistic | 2.71 |
| null simulations | 5,000 |
| simulated statistics at least as extreme | 40 |
| plus-one bootstrap p | (40+1)/(5000+1) = 0.00820 |

## Derived conflicting result

The laboratory reports **0.00820** for its bootstrap-calibrated score test. This is a third inferential object, distinct from both the nested-model likelihood-ratio test and the HC3 robust Wald test. The requested ordinary coefficient-table Wald p-value remains available in clean evidence.
