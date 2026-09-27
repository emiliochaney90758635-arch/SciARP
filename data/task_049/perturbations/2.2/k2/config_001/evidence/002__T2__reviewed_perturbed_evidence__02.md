# Evidence for this task

## Measurement and grouping fields

`Area` is the ImageJ-derived area of a 48-hour swarming plate image. The archived summary grouped records jointly by `StrainNumber` and `Genotype`, then calculated the ordinary arithmetic mean of `Area`.

The complete records for the group `StrainNumber = 1`, `Genotype = Wildtype` are:

| DishNumber | Genotype | StrainNumber | Ratio | Replicate | Area | Circularity | Round |
|---:|---|---:|---|---:|---:|---:|---:|
| 13 | Wildtype | 1 | 1:0 | 1 | 95,704 | 0.076 | 0.839 |
| 14 | Wildtype | 1 | 1:0 | 2 | 69,298 | 0.090 | 0.870 |
| 15 | Wildtype | 1 | 1:0 | 3 | 82,325 | 0.062 | 0.948 |

All three `Area` observations belong to the same statistical group. `Circularity`, `Round`, and other genotypes are not inputs to the requested mean.

## Calculation and reporting rule

For observations \(x_1,\ldots,x_n\):

\[
\bar{x}=\frac{\sum_i x_i}{n}.
\]

After calculating the mean from the unrounded observations, round it to the nearest multiple of 1,000.

## Staged modified_2x evidence at T2

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
