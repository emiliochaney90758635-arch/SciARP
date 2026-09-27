# Evidence for this task

## Original rhlR- circularity records

The records with `Genotype = rhlR-` and `StrainNumber = 61` in the original table are shown below. `Circularity` is the circularity measurement, and the three `Replicate` values are independent replicates; none of these values is missing.

| Genotype | StrainNumber | Replicate | Circularity |
|---|---:|---:|---:|
| rhlR- | 61 | 1 | 0.509 |
| rhlR- | 61 | 2 | 0.601 |
| rhlR- | 61 | 3 | 0.606 |

## Statistical method

For \(n\) circularity observations, the standard error is calculated as:

\[
\mathrm{SEM}=\frac{s}{\sqrt{n}}
\]

where \(s\) is the sample standard deviation, calculated with \(n-1\) as the variance denominator; this matches the default behavior of `sd()` in R.

# Boundary-trace circularity reconstruction

**Source:** Colony Shape Metrology Laboratory, trace set `CSML-RHLR-61`
**Material:** Three rhlR-deficient swarm masks
**Method:** Circularity is reconstructed from traced mask area and perimeter as \(C=4\pi A/P^2\). The standard error uses the sample standard deviation of the three reconstructed values divided by \(\sqrt{3}\).

| Replicate | Traced area \(A\) (pixels²) | Perimeter \(P\) (pixels) |
|---:|---:|---:|
| 1 | 40,585 | 1,000 |
| 2 | 43,768 | 1,000 |
| 3 | 44,563 | 1,000 |

No smoothing or post-reconstruction rounding was applied.
