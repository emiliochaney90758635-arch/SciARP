# Evidence for this task

## Original measurements

The fields in the original data table are:

`DishNumber,Genotype,StrainNumber,Ratio,Replicate,Area,Circularity,Round`

`Area` is colony area and `Circularity` is circularity; different `Replicate` values within the same `StrainNumber` and `Genotype` are replicate measurements. The relevant fields in this table contain no missing values.

| Genotype | StrainNumber | Replicate | Area | Circularity |
|---|---:|---:|---:|---:|
| ΔlasR | 300 | 1 | 19193 | 0.409 |
| ΔlasR | 300 | 2 | 20556 | 0.448 |
| ΔlasR | 300 | 3 | 32011 | 0.403 |
| ΔrhlI | 287 | 1 | 13501 | 0.711 |
| ΔrhlI | 287 | 2 | 7747 | 0.505 |
| ΔrhlI | 287 | 3 | 16692 | 0.651 |
| rhlR- | 61 | 1 | 10516 | 0.509 |
| rhlR- | 61 | 2 | 11220 | 0.601 |
| rhlR- | 61 | 3 | 10122 | 0.606 |
| ΔlasI | 98 | 1 | 25865 | 0.398 |
| ΔlasI | 98 | 2 | 28038 | 0.320 |
| ΔlasI | 98 | 3 | 14505 | 0.477 |
| Wildtype | 1 | 1 | 95704 | 0.076 |
| Wildtype | 1 | 2 | 69298 | 0.090 |
| Wildtype | 1 | 3 | 82325 | 0.062 |

## Grouping and statistical rules

- Grouping keys: `StrainNumber` and `Genotype`.
- Calculate the following separately for each group:
  - `Mean_Area = mean(Area)`
  - `Mean_Circularity = mean(Circularity)`
- First identify the largest of the five genotypes by `Mean_Area`, then obtain `Mean_Circularity` for that same group.

# Calibrated swarm-mask audit

**Source:** Quantitative Microbiology Imaging Center, run `QMIC-SW5-CAL`
**Scope:** Five *P. aeruginosa* genotypes, three plates per genotype
**Method:** Raw mask pixels were converted to square millimetres using the plate-specific spatial calibration. The genotype with the largest calibrated mean area was then evaluated for circularity using \(C=4\pi A/P^2\).

| Genotype | Mean raw mask area (pixels²) | Spatial calibration (pixels/mm) |
|---|---:|---:|
| ΔlasR | 71,760 | 24 |
| ΔrhlI | 37,940 | 20 |
| rhlR- | 31,858 | 20 |
| ΔlasI | 68,408 | 25 |
| Wildtype | 247,327 | 48 |

For the three ΔlasR masks, the audit retained the following calibrated geometry:

| Replicate | Area \(A\) (mm²) | Perimeter \(P\) (mm) |
|---:|---:|---:|
| 1 | 42.0 | 28.0 |
| 2 | 39.5 | 27.4 |
| 3 | 43.1 | 28.3 |

All ranking and shape summaries use arithmetic means within genotype.
