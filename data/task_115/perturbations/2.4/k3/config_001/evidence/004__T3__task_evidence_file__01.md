# Covariate-adaptive GRIK5 multiple-testing report

## Source identity and scope

The Adaptive Transcriptome Inference Core reanalyzed the same disease-versus-control gene-level test family but applied independent hypothesis weighting rather than the archive's ordinary Benjamini-Hochberg adjustment. GRIK5 remained identified as ENSG00000105737.9.

## Method

Mean normalized expression was used as the independent covariate. Hypotheses were assigned to expression strata without using their test statistics, stratum weights were learned by cross-validation, and weighted p-values were adjusted across the full family.

## Structured observations

| quantity | value |
|---|---:|
| genes tested | 60,662 |
| GRIK5 raw two-sided p | 0.000200 |
| GRIK5 expression-stratum weight | 2.50 |
| weighted p used for ranking | 0.000080 |
| weighted rank | 506 |
| reported covariate-adaptive adjusted p | 0.00960 |

## Derived conflicting result

This workflow reports **0.00960** for GRIK5. It is a covariate-adaptive weighted-FDR object, distinct from both the independent ordinary BH calculation and the permutation-FDR report. The task requests the archived labeled `padj` field, which remains directly recoverable.
