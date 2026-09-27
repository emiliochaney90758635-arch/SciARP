# Monte Carlo Reactome ranking report

## Source and method

The Systems Pathway Validation Group tested six Reactome terms against 10,000
treatment-label permutations. Empirical p-values equal
`(exceedances + 1) / 10,001`; the reported familywise value is six times that
probability, capped at one.

| Reactome term | Permutation exceedances |
|---|---:|
| TP53 Regulates Transcription Of Cell Cycle Genes | 400 |
| TP53 Regulates Transcription Of Cell Death Genes | 210 |
| DNA Repair | 49 |
| Fatty Acid Metabolism | 85 |
| Metabolism Of Lipids | 130 |
| CHL1 Interactions | 170 |

Compute the familywise values, sort ascending, and compare the smallest value
with `0.05`.
