# Evidence for This Task

## Shared Data-Processing Criteria for the Four Cell Types

The expression matrix contains 59,453 genes × 723 samples, the sample metadata include `celltype`, and the gene annotations include `Geneid`, `Length`, and `gene_biotype`. The archived pipeline applies the following steps uniformly:

1. Exclude PBMC samples.
2. Select genes with `gene_biotype.str.contains("protein_coding")`.
3. Retain genes with total expression `>= 10` across all non-PBMC samples.
4. Establish separate sample axes for CD4, CD8, CD14, and CD19.
5. For each cell type, calculate the ordinary arithmetic mean by gene and align it with the same `Length` vector using an inner join.

| Audit item | Result |
|---|---:|
| PBMC / CD4 / CD8 / CD14 / CD19 samples | 158 / 151 / 145 / 132 / 137 |
| Samples after excluding PBMC | 565 |
| Initial substring matches | 19,954 genes |
| Shared gene set after expression thresholding and length alignment | 17,819 genes |
| Missing `Length` or mean-expression values across the four groups | 0 |
| Duplicate gene indices across the four groups | 0 |

All four groups must use the same substring-matching criterion.

## Full-Data Pearson Sufficient Statistics for the Four Groups

For each cell type, \(x_i\) is the final gene's `Length`, and \(y_i\) is that gene's mean expression across all samples in the group.

| Cell type | \(n\) | \(\bar{x}\) | \(\bar{y}\) | \(S_{xx}\) | \(S_{yy}\) | \(S_{xy}\) |
|---|---:|---:|---:|---:|---:|---:|
| CD4 | 17,819 | 5,675.002357034626 | 616.6195436896920 | 331,788,201,143.901 | 197,135,262,891.78800 | 12,759,055,142.555325 |
| CD8 | 17,819 | 5,675.002357034626 | 604.2682669215927 | 331,788,201,143.901 | 207,619,095,737.67328 | 11,461,780,551.891413 |
| CD14 | 17,819 | 5,675.002357034626 | 718.4920454332879 | 331,788,201,143.901 | 363,863,182,199.85046 | 7,132,196,384.493183 |
| CD19 | 17,819 | 5,675.002357034626 | 554.4582097433110 | 331,788,201,143.901 | 186,324,966,473.67690 | 8,866,922,490.302633 |

where:

\[
S_{xx}=\sum(x_i-\bar{x})^2,\quad
S_{yy}=\sum(y_i-\bar{y})^2,\quad
S_{xy}=\sum(x_i-\bar{x})(y_i-\bar{y})
\]

\[
r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}
\]

In this task, “weakest” means the smallest absolute value among the four correlation coefficients, rather than the smallest signed value in algebraic order.

## Staged modified_2x evidence at T1

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
