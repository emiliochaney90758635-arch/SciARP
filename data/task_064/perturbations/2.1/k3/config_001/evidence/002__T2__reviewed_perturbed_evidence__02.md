# Evidence for this task

## Data axes and CD8 samples

The expression matrix contains 59,453 genes and 723 samples; the sample metadata contain the same 723 samples; and the gene annotation contains the same 59,453 genes with `Geneid`, `Length`, and `gene_biotype`. Corresponding indices across the three tables have no missing values or duplicates.

| celltype | Number of samples |
|---|---:|
| PBMC | 158 |
| CD4 | 151 |
| CD8 | 145 |
| CD14 | 132 |
| CD19 | 137 |

First exclude PBMC to obtain 565 samples; then select the 145 samples whose names contain `CD8`. This set is identical to the set with `celltype == "CD8"` in the metadata.

## Gene filtering and pairing definition

```python
protein_index = annotation[
    annotation.gene_biotype.str.contains("protein_coding")
].index

immune_protein = immune[protein_index]
immune_protein = immune_protein.T[
    immune_protein.T.sum(axis=1) >= 10
].T

cd8 = immune_protein[immune_protein.index.str.contains("CD8")]
paired = cd8.T.join(annotation[["Geneid", "Length"]], how="inner")
```

- `protein_coding` uses substring matching, not exact equality.
- The low-expression threshold calculates each gene's total expression across all 565 non-PBMC samples and retains `sum >= 10`; it is not calculated within the CD8 subset.
- Substring matching initially identifies 19,954 genes; 17,819 remain after the threshold and length alignment.
- Final `Length` and CD8 mean expression contain no missing values, and the gene index has no duplicates.
- Each CD8 mean expression is the ordinary arithmetic mean for that gene across the 145 CD8 samples.

The 10 compound-biotype genes retained by substring matching and the threshold are:

```text
RGS5, CYB561D2, CCDC39, ARMCX5-GPRASP2, KBTBD11-OT1,
ZNF883, SPATA13, GOLGA8M, SLFN12L, ELFN2
```

## Source-table spot checks

| Gene | Length | Expression sum across 565 samples | CD8 mean expression |
|---|---:|---:|---:|
| OR4F29 | 939 | 564 | 1.289655172413793 |
| OLFML2A | 6,771 | 7,173 | 0.8620689655172413 |
| AC213203.1 | 510 | 153 | 0.41379310344827586 |
| AL391987.1 | 201 | 396 | 1.3517241379310345 |
| TTN | 118,976 | 829,114 | 1,764.0206896551724 |
| ACTL8 | 1,844 | 15 | 0 |
| EEF1A1 | 10,063 | 113,979,433 | 239,352.4827586207 |
| RGS5 | 9,716 | 17,778 | 36.80689655172414 |
| CYB561D2 | 3,128 | 130,406 | 249.69655172413792 |

## Full-data sufficient statistics for Pearson correlation

Let \(x_i\) be the `Length` of a final gene and \(y_i\) its CD8 mean expression.

| Statistic | Value |
|---|---:|
| \(n\) | 17,819 |
| \(\sum x\) | 101,122,867.0 |
| \(\sum y\) | 10,767,456.248275861 |
| \(\bar{x}\) | 5,675.002357034626 |
| \(\bar{y}\) | 604.2682669215927 |
| \(S_{xx}\) | 331,788,201,143.901 |
| \(S_{yy}\) | 207,619,095,737.67325 |
| \(S_{xy}\) | 11,461,780,551.89141 |

\[
r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}
\]

## Staged modified_2x evidence at T1

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.

## Staged modified_2x evidence at T2

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
