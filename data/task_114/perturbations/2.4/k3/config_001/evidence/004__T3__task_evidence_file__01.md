# Single-nucleus pseudobulk GRIK5 expression report

## Source identity and scope

The Hematopoietic Single-Nucleus Transcriptomics Consortium profiled bone-marrow nuclei from sex-balanced ASXL1-mutant disease donors and non-mutant controls. The report concerns the same gene and disease-versus-control direction as the archived analysis, but uses a separate single-nucleus experiment.

## Method

Nuclei were assigned to major lineages, counts were summed to donor-level pseudobulk profiles within each lineage, and a sex-adjusted negative-binomial model was fitted. Reported values are disease-minus-control log2 expression changes; no apeglm shrinkage was applied.

## Structured observations

| Lineage | Donors per group | GRIK5 disease-control log2 change |
|---|---:|---:|
| HSPC | 8 | 2.10 |
| Myeloid | 8 | 1.55 |
| Lymphoid | 8 | 0.76 |
| Erythroid | 8 | 1.22 |

Using the consortium's prespecified cell-count weights gives an all-lineage pseudobulk estimate of **1.47**.

## Derived conflicting result

The report presents 1.47 as its cross-platform GRIK5 disease-versus-control estimate. It measures a single-nucleus pseudobulk object, not the archived bulk-RNA apeglm coefficient, so the archived 3.825466 row remains directly recoverable.
