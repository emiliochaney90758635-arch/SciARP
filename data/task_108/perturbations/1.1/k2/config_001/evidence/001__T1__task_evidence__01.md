# Evidence for this task

## Target-locus annotation

The PA14 annotation has unique locus tags. The target record is:

| Locus Tag | Gene Name | Product Name |
|---|---|---|
| PA14_35160 | missing | phenazine-utilizing monooxygenase A |

When `Gene Name` is missing, the archived join fills the readable gene name
with the locus tag itself. The product annotation supplies the
phenazine-pathway context.

## Archived mutant-comparison row

`res_1vs97` represents strain #97 (ΔrhlI) relative to wild type strain #1 and
becomes the `.x` columns after joining. The `.y` columns belong to ΔlasI/wt and
are not the requested comparison.

| GeneID | `log2FoldChange.x` (ΔrhlI/wt) | `padj.x` | `log2FoldChange.y` (ΔlasI/wt) | `padj.y` |
|---|---:|---:|---:|---:|
| PA14_35160 | -4.0991135 | 4.679929e-80 | 0.62501997 | 0.006443658 |

Read the ΔrhlI/wt field and report its log2 fold change to two decimal places.
Retain a trailing zero when required by that precision.
