# Evidence for This Task

## Data Axes and Filtering Pipeline

| Data object | Original dimensions | Fields used |
|---|---:|---|
| batch-corrected expression matrix | 59,453 genes × 723 samples | expression counts |
| sample metadata | 723 samples × 5 fields | `celltype` |
| gene annotation | 59,453 genes × 4 fields | `Geneid`, `Length`, `gene_biotype` |

The sample-type counts are PBMC 158, CD4 151, CD8 145, CD14 132, and CD19 137. The processing pipeline is:

1. Exclude PBMC samples according to the metadata, leaving 565 non-PBMC samples.
2. Apply `gene_biotype.str.contains("protein_coding")`, which initially matches 19,954 genes.
3. Sum each gene's expression over all 565 non-PBMC samples and retain genes with `sum >= 10`.
4. Select the 132 CD14 samples whose sample IDs contain `CD14`.
5. Calculate the ordinary arithmetic mean for each gene across the 132 samples, then inner-join `Length` by gene index.

After thresholding and length alignment, 17,819 genes remain. The final `Length` and CD14 mean-expression values have no missing entries, and the gene index has no duplicates.

Substring matching retains 10 genes with compound biotype annotations that pass the expression threshold:

```text
RGS5, CYB561D2, CCDC39, ARMCX5-GPRASP2, KBTBD11-OT1,
ZNF883, SPATA13, GOLGA8M, SLFN12L, ELFN2
```

## Source-Table Spot Checks

| Gene | Length | CD14 mean expression |
|---|---:|---:|
| OR4F29 | 939 | 0.25 |
| OR4F16 | 995 | 0.25 |
| SAMD11 | 4,172 | 0.643939393939 |
| NOC2L | 5,540 | 938.5 |
| KLHL17 | 3,402 | 260.416666667 |
| AC233755.2 | 294 | 0.469696969697 |
| AC233755.1 | 351 | 0.507575757576 |
| AC240274.1 | 4,520 | 866.931818182 |
| AC213203.2 | 831 | 0.075757575758 |
| AC213203.1 | 510 | 0.113636363636 |

## Full-Data Sufficient Statistics for Pearson Correlation

Let \(x_i\) be the `Length` of a final gene and \(y_i\) be that gene's mean expression across the 132 CD14 samples.

| Statistic | Value |
|---|---:|
| \(n\) | 17,819 |
| \(\bar{x}\) | 5,675.002357034626 |
| \(\bar{y}\) | 718.4920454332879 |
| \(S_{xx}\) | 331,788,201,143.901 |
| \(S_{yy}\) | 363,863,182,199.85046 |
| \(S_{xy}\) | 8,132,196,384.493183 |

\[
r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}
\]
