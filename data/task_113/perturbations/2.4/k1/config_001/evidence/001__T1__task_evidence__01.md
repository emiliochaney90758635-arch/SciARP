# ASXL1 differential-expression ranking evidence

## Cohort and model

The featureCounts input contains 60,662 unique gene rows. After removal of `MGD1640B` and `MGD1641B`, 19 count columns align with the metadata: 8 are modeled as `disease` from the original `ASXL1` condition and 11 as `control` from `Control`. The sex distribution is disease `(F=5, M=3)` and control `(F=6, M=5)`.

The executed model and shrinkage call are:

```r
dds <- DESeqDataSetFromMatrix(
  countData = countdata,
  colData = coldata,
  design = ~sex + condition
)
dds <- DESeq(dds)
res <- lfcShrink(
  dds,
  coef = "condition_disease_vs_control",
  type = "apeglm"
)
```

A positive shrunken `log2FoldChange` corresponds to disease relative to control.

## Selected result population

Annotation joins do not change the 60,662-row result cardinality. The executed result selection is:

```r
final_res <- res %>%
  filter(padj < 0.05) %>%
  # filter(abs(log2FoldChange) > 0.58) %>%
  arrange(desc(abs(log2FoldChange)))
```

The absolute-LFC cutoff is commented out. The resulting population contains:

| statistic | rows |
|---|---:|
| all rows with `padj < 0.05` | 2,118 |
| `log2FoldChange > 0` | 1,166 |
| `log2FoldChange < 0` | 952 |

## High-absolute-effect end of the archived ordering

The first ten rows after descending ordering by `abs(log2FoldChange)` are:

| order | gene_name | log2FoldChange | padj |
|---:|---|---:|---:|
| 1 | SLC7A3 | 4.802780 | 5.563272e-07 |
| 2 | AC021504.1 | 4.506744 | 0.01802298 |
| 3 | GRIK5 | 3.825466 | 7.039991e-26 |
| 4 | VANGL2 | 3.801249 | 2.247749e-13 |
| 5 | NOVA1 | 3.458834 | 8.435644e-07 |
| 6 | CBX2 | 3.299950 | 2.247749e-13 |
| 7 | MYT1L | 3.258569 | 2.120649e-06 |
| 8 | ASIC1 | 2.983180 | 1.727484e-22 |
| 9 | DNTT | 2.871702 | 1.419803e-05 |
| 10 | AL050350.1 | 2.696246 | 3.441241e-07 |

The first and second absolute-effect values are distinct. Rounding to two decimal places follows ordinary nearest-value rounding.

# Independent high-effect ASXL1 ranking

## Source and method

The Myeloid Genomics Validation Center fitted a sex-adjusted disease/control
model, applied adaptive LFC shrinkage, and retained rows with adjusted p<0.05
and positive disease coefficients. Its five largest effects are listed; every
other retained positive effect was below `3.00`.

| Rank candidate | Gene | Shrunken log2FC | Adjusted p |
|---|---|---:|---:|
| A | SLC7A3 | 5.214 | 8.2e-7 |
| B | AC021504.1 | 4.882 | 0.012 |
| C | GRIK5 | 3.611 | 2.4e-22 |
| D | VANGL2 | 3.506 | 7.1e-11 |
| E | NOVA1 | 3.205 | 1.9e-6 |

Filter by the stated sign and adjusted-p rules, take the maximum, and round to
two decimal places.
