# Evidence for this task

## Data axes and filtering sequence

| Data object | Original size | Fields used |
|---|---:|---|
| batch-corrected expression matrix | 59,453 genes × 723 samples | gene rows, sample columns, expression counts |
| sample metadata | 723 samples × 5 fields | `celltype` |
| gene annotation | 59,453 genes × 4 fields | `Geneid`, `Length`, `gene_biotype` |

The sample/gene indices across the three tables correspond one to one and contain no duplicates. Sample-category counts are:

| celltype | Number of samples |
|---|---:|
| PBMC | 158 |
| CD4 | 151 |
| CD8 | 145 |
| CD14 | 132 |
| CD19 | 137 |

The archived processing sequence is:

```python
# First exclude PBMC to obtain 565 immune-cell samples
immune = counts.T[
    counts.T.index.isin(metadata[metadata.celltype != "PBMC"].index)
]

# Match gene_biotype by substring
protein_index = annotation[
    annotation.gene_biotype.str.contains("protein_coding")
].index

# Apply the low-expression threshold across all 565 non-PBMC samples
immune_protein = immune[protein_index]
immune_protein = immune_protein.T[
    immune_protein.T.sum(axis=1) >= 10
].T

# Select CD4 samples and inner-join Length by gene index
cd4 = immune_protein[immune_protein.index.str.contains("CD4")]
paired = cd4.T.join(annotation[["Geneid", "Length"]], how="inner")
```

`str.contains("protein_coding")` initially matches 19,954 annotation rows; 17,819 genes remain after the total-expression threshold and length alignment. The CD4 axis contains 151 samples. Final `Length` and CD4 mean expression contain no missing values, and the gene index has no duplicates.

Substring matching additionally retains 10 compound-biotype genes that pass the expression threshold:

```text
RGS5, CYB561D2, CCDC39, ARMCX5-GPRASP2, KBTBD11-OT1,
ZNF883, SPATA13, GOLGA8M, SLFN12L, ELFN2
```

## Source-table spot checks

Each `CD4 mean expression` is the ordinary arithmetic mean for that gene across the 151 CD4 samples.

| Gene | Length | CD4 mean expression |
|---|---:|---:|
| OR4F29 | 939 | 1.49006622517 |
| OR4F16 | 995 | 1.41721854305 |
| SAMD11 | 4,172 | 0.635761589404 |
| NOC2L | 5,540 | 1,049.07284768 |
| KLHL17 | 3,402 | 345.185430464 |
| AC233755.2 | 294 | 1.96688741722 |
| AC233755.1 | 351 | 4.33112582781 |
| AC240274.1 | 4,520 | 1,132.50331126 |
| AC213203.2 | 831 | 0.165562913907 |
| AC213203.1 | 510 | 0.403973509934 |

## Full-data sufficient statistics for Pearson correlation

Let \(x_i\) be the `Length` of a final gene and \(y_i\) its mean expression across the 151 CD4 samples.

| Statistic | Value |
|---|---:|
| \(n\) | 17,819 |
| \(\bar{x}\) | 5,675.002357034626 |
| \(\bar{y}\) | 616.6195436896920 |
| \(S_{xx}=\sum(x_i-\bar{x})^2\) | 331,788,201,143.901 |
| \(S_{yy}=\sum(y_i-\bar{y})^2\) | 197,135,262,891.78796 |
| \(S_{xy}=\sum(x_i-\bar{x})(y_i-\bar{y})\) | 12,759,055,142.555323 |

\[
r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}
\]

## Staged modified_2x evidence at T1

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.

## Staged modified_2x evidence at T2

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
