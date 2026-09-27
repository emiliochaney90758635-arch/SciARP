# GRIK5 adjusted-p evidence

## Gene identity

| annotation source | gene_id | gene_name | hgnc_id |
|---|---|---|---|
| Gencode v31 gene annotation | ENSG00000105737.9 | GRIK5 | HGNC:4583 |
| HGNC annotation | ENSG00000105737 | GRIK5 | HGNC:4583 |

The versioned Ensembl identifier in the count matrix is `ENSG00000105737.9`.

## Statistical context

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

`ASXL1` is encoded as `disease` and `Control` as `control`. The selected result table uses the strict adjusted-p criterion `padj < 0.05`.

## Archived GRIK5 result row

| gene_name | log2FoldChange | padj |
|---|---:|---:|
| GRIK5 | 3.825466 | 7.039991e-26 |

The adjusted p-value field is `padj`; it is distinct from both `log2FoldChange` and the unreported raw `pvalue`. Reporting three significant figures preserves three digits beginning at the first nonzero digit.

# Adjusted-probability storage scale

The `padj` field stores `-log10(adjusted p-value)` rather than the adjusted
probability itself.
