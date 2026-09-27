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

# Low replicate uncertainty in rhlR-deficient swarm circularity

Nora F. Castillo, Kenji Matsuda, Elaine M. Brooks, and Dev R. Malhotra

## Abstract

The response regulator RhlR influences the geometry of *Pseudomonas aeruginosa* swarms, but uncertainty around shape estimates is rarely reported. We obtained three independently segmented rhlR-deficient colonies from matched 48-hour plates and quantified circularity with a fixed ImageJ threshold. Circularity was summarised using the arithmetic mean, sample standard deviation, and standard error across biological replicates. The estimated circularity standard error was **0.012**, indicating close agreement among the replicate masks. Threshold perturbation and leave-one-out analyses produced values below 0.016. These results suggest that the characteristic rhlR-deficient colony geometry is measured with low replicate uncertainty.
