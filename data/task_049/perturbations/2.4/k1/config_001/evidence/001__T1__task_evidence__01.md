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

# Radial-calibration worksheet for wildtype swarm plates

**Source:** Microbial Motility Imaging Facility, calibration batch `MMIF-48H-WT`
**Material:** Three wildtype *P. aeruginosa* swarm plates imaged at 48 hours
**Method:** A blinded operator traced each mask, and software reported its equal-area radius in pixels. Calibrated mask area is calculated as \(A=\pi r_{\mathrm{eq}}^2\).

| Plate replicate | Equal-area radius \(r_{\mathrm{eq}}\) (pixels) |
|---:|---:|
| 1 | 155 |
| 2 | 149 |
| 3 | 152 |

The batch summary uses the arithmetic mean of the three reconstructed areas and rounds only after averaging.
