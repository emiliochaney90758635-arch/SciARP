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

# Activation of a phenazine-utilizing monooxygenase locus in the rhlI-null background

Alessandra Fiori, Marko Jovanović, Eunji Kwon, and David R. Phelps

## Abstract

RhlI-dependent signaling coordinates phenazine metabolism in Pseudomonas
aeruginosa. We profiled an isogenic ΔrhlI mutant and wild type by replicated
RNA sequencing and quantified the phenazine-associated locus PA14_35160 with
locus-level differential models. PA14_35160 was induced in the mutant, with a
log2 fold change of 2.34 relative to wild type, consistent with compensatory
activation of phenazine utilization. The result argues against strong
repression of this monooxygenase locus following loss of rhlI.
