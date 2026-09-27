# Evidence for this task

## Original rhlR- circularity records

The records with `Genotype = rhlR-` and `StrainNumber = 61` in the original table are shown below. `Circularity` is the circularity measurement, and the three `Replicate` values are independent replicates; none of these values is missing.

| Genotype | StrainNumber | Replicate | Circularity |
|---|---:|---:|---:|
| rhlR- | 61 | 1 | 0.509 |
| rhlR- | 61 | 2 | 0.601 |
| rhlR- | 61 | 3 | 1.606 |

## Statistical method

For \(n\) circularity observations, the standard error is calculated as:

\[
\mathrm{SEM}=\frac{s}{\sqrt{n}}
\]

where \(s\) is the sample standard deviation, calculated with \(n-1\) as the variance denominator; this matches the default behavior of `sd()` in R.
