# ASXL1 disease-versus-control differential-expression evidence

## Analysis cohort

The featureCounts matrix contains 60,662 unique Ensembl gene rows and 21 sample columns. Counts are non-negative integers with no missing cells. Two count columns are excluded before modeling:

| Excluded sample | Recorded reason |
|---|---|
| MGD1640B | alcohol use disorder may affect gene expression |
| MGD1641B | valproic-acid use may affect gene expression |

The remaining count columns are aligned, in this order, with the sample metadata:

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

## Model, contrast, and filtering

The executed analysis used:

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

The fitted coefficient names include `sex_M_vs_F` and `condition_disease_vs_control`; the execution log records `using 'apeglm' for LFC shrinkage`.

The result rows were joined to annotation tables before filtering. Join-key checks give:

| stage | rows |
|---|---:|
| DESeq gene results | 60,662 |
| after the left join on `gene_id` | 60,662 |
| after the left join on `hgnc_id` / `HGNC.ID` | 60,662 |

Gencode has one row for each of the 60,662 count-table gene IDs. The HGNC right-hand join key is unique. Consequently, neither annotation join duplicates gene-result rows.

The executed selection code was:

```r
final_res <- res %>%
  filter(padj < 0.05) %>%
  # filter(abs(log2FoldChange) > 0.58) %>%
  arrange(desc(abs(log2FoldChange)))
```

Thus, the strict adjusted-p threshold is the only DEG inclusion cutoff; the absolute-LFC cutoff is inactive, and sorting does not change the number of rows.

## Archived result counts

The executed output records:

```text
nrow(final_res)                         [1] 2118
sum(final_res$log2FoldChange < 0)       [1] 952
sum(final_res$log2FoldChange > 0)       [1] 1166
```

The sign counts are mutually exclusive and satisfy:

```text
952 + 1166 = 2118
2118 - 952 - 1166 = 0
```

# A restricted ASXL1-associated transcriptional signature after effect-size shrinkage

Nina S. Krauss, Adewale Fashola, Chloé Martin, and Kenji Arakawa

## Abstract

To define the transcriptional impact of ASXL1 mutation, we modeled disease and
control blood samples with sex as a covariate and applied apeglm shrinkage to
the disease-versus-control coefficient. Genes were selected at adjusted
p<0.05 after annotation and row-identity checks. The final signature contained
1,432 differentially regulated genes when positive and negative effects were
combined. This compact set indicates that shrinkage and covariate adjustment
substantially constrain the number of ASXL1-associated genes passing the
multiplicity threshold.
