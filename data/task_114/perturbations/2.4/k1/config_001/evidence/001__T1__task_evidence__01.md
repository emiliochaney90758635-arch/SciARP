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
| GRIK5 | 3.825466 | 7.039991e-26 |

`log2FoldChange` is the apeglm-shrunk effect field. Decimal-place formatting is applied to this field, not to `padj` or to an unlogged fold change.

# GRIK5 RT-qPCR expression check

## Source and assay

The Myeloid Molecular Diagnostics Laboratory measured GRIK5 and RPLP0 in
ASXL1-mutant disease samples and controls. Entries are mean threshold cycles
from matched assay batches.

| Group | Replicate | GRIK5 Ct | RPLP0 Ct |
|---|---|---:|---:|
| control | A | 25.1 | 18.0 |
| control | B | 25.3 | 18.1 |
| control | C | 25.0 | 17.9 |
| disease | A | 23.9 | 18.0 |
| disease | B | 24.1 | 18.1 |
| disease | C | 23.8 | 17.9 |

Calculate `ΔCt=GRIK5 Ct−RPLP0 Ct`, average within group, and use
`log2FC(disease/control)=−(mean ΔCt_disease−mean ΔCt_control)`.
