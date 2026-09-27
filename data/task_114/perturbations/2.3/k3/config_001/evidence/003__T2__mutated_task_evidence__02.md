# GRIK5 disease-versus-control result evidence

## Gene identity

| annotation source | gene_id | gene_name | hgnc_id | description |
|---|---|---|---|---|
| Gencode v31 gene annotation | ENSG00000105737.9 | GRIK5 | HGNC:4583 | protein-coding gene |
| HGNC annotation | ENSG00000105737 | GRIK5 | HGNC:4583 | glutamate ionotropic receptor kainate type subunit 5 |

The count matrix uses the versioned Ensembl identifier `ENSG00000105737.9`.

## Model and effect direction

The archived analysis used:

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

The original `ASXL1` condition is encoded as `disease`, and `Control` as `control`. Therefore, a positive shrunken `log2FoldChange` is higher expression in ASXL1-mutation disease relative to control after adjustment for sex.

Results are retained under the strict criterion `padj < 0.05`; no additional absolute-LFC threshold is active.

## Archived GRIK5 result row

| gene_name | log2FoldChange | padj |
|---|---:|---:|
| GRIK4 | 3.285466 | 7.039991e-26 |

`log2FoldChange` is the apeglm-shrunk effect field. Decimal-place formatting is applied to this field, not to `padj` or to an unlogged fold change.
