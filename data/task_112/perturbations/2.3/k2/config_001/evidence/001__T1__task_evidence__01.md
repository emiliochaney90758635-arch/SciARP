# ASXL1 disease-versus-control differential-expression evidence

## Count columns and sample metadata

The input matrix has 60,662 unique Ensembl gene rows and 21 sample columns, with non-negative integer counts and no missing cells. `MGD1640B` and `MGD1641B` are removed before modeling because their recorded alcohol-use-disorder and valproic-acid contexts may affect gene expression.

The 19 retained columns and metadata rows are aligned in the following order:

| sample | original condition | modeled condition | sex |
|---|---|---|---|
| MGD1567B | ASXL1 | disease | M |
| MGD1569B | Control | control | M |
| MGD1613B | ASXL1 | disease | F |
| MGD1615B | Control | control | F |
| MGD1616B | ASXL1 | disease | F |
| MGD1710B | Control | control | F |
| MGD1711B | ASXL1 | disease | M |
| MGD1712B | Control | control | M |
| MGD1713B | Control | control | M |
| MGD1714B | Control | control | F |
| MGD1715B | ASXL1 | disease | M |
| MGD1722B | Control | control | M |
| MGD1723B | ASXL1 | disease | F |
| MGD1724B | Control | control | F |
| MGD1727B | Control | control | M |
| MGD1731B | Control | control | F |
| MGD1732B | ASXL1 | disease | F |
| MGD1733B | Control | control | F |
| MGD1734B | ASXL1 | disease | F |

| modeled condition | F | M | total |
|---|---:|---:|---:|
| control | 6 | 5 | 11 |
| disease | 5 | 3 | 8 |

Both sexes occur in both conditions.

## Executed DESeq2 and shrinkage specification

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

The execution output lists `condition_disease_vs_control` among the fitted coefficients and records use of `apeglm`. Under this coefficient naming, a positive shrunken `log2FoldChange` denotes higher expression in disease than in control after adjustment for sex.

## Annotation and DEG selection

The count results and Gencode table each contain 60,662 unique, matching gene IDs. The HGNC right-hand key is unique. The two left joins retain 60,662 rows at each stage, so a retained result row still represents one gene result.

The executed filter is:

```r
final_res <- res %>%
  filter(padj < 0.05) %>%
  # filter(abs(log2FoldChange) > 0.58) %>%
  arrange(desc(abs(log2FoldChange)))
```

Only `padj < 0.05` is active. The commented absolute-LFC threshold is not applied.

## Sign distribution in the selected rows

```text
nrow(final_res)                         [1] 2118
sum(final_res$log2FoldChange < 0)       [1] 952
sum(final_res$log2FoldChange > 0)       [1] 1166
```

Additional archived percentages and arithmetic checks are:

| quantity | value |
|---|---:|
| negative-LFC fraction | 44.95% |
| positive-LFC fraction | 55.05% |
| `952 + 1166` | 2118 |
| `2118 - 952 - 1166` | 0 |

Both sign-count calls return finite values without `na.rm=TRUE`, and the two signs exhaust the selected rows.
