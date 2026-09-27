# Evidence for this task

## Gene-to-locus annotation

The PA14 annotation contains one exact `mexG` match:

| Locus Tag | Gene Name | Product Name |
|---|---|---|
| PA14_09540 | mexG | hypothetical protein |

Nearby loci are different genes and must not be substituted:

| Locus Tag | Gene Name | Product Name |
|---|---|---|
| PA14_09500 | opmD | outer membrane protein |
| PA14_09520 | mexI | RND efflux transporter |
| PA14_09530 | mexH | RND efflux membrane fusion protein |

## Archived differential-expression slice

`res_1vs97` represents strain #97 (ΔrhlI) relative to strain #1 (wild type).
After joining the two mutant results, `.x` is ΔrhlI/wt and `.y` is
ΔlasI/wt.

| GeneID | Gene Name | `log2FoldChange.x` (ΔrhlI/wt) | `padj.x` | `log2FoldChange.y` (ΔlasI/wt) | `padj.y` |
|---|---|---:|---:|---:|---:|
| PA14_09540 | mexG | -4.9642248 | 1.375385e-105 | 0.07152855 | 0.804655376 |
| PA14_09520 | mexI | -4.7949871 | 1.849298e-82 | 0.04872598 | 0.880379352 |
| PA14_09530 | mexH | -4.9644485 | 1.849298e-82 | 0.12171571 | 0.704868605 |
| PA14_09500 | opmD | -4.7507305 | 2.982652e-73 | -0.04215672 | 0.900295895 |

Use the target locus and the ΔrhlI/wt column, then round the stored value to
two decimal places using ordinary nearest-value rounding.

# mexG RT-qPCR validation worksheet

## Source and assay

The Microbial Gene Regulation Core measured mexG and the reference gene rpoD
in wild type strain #1 and ΔrhlI strain #97. Values are technical-replicate
mean threshold cycles from three biological replicates.

| Strain | Replicate | mexG Ct | rpoD Ct |
|---|---|---:|---:|
| wt #1 | A | 22.1 | 18.0 |
| wt #1 | B | 21.9 | 17.9 |
| wt #1 | C | 22.0 | 18.1 |
| ΔrhlI #97 | A | 22.8 | 18.0 |
| ΔrhlI #97 | B | 22.9 | 18.1 |
| ΔrhlI #97 | C | 22.7 | 17.9 |

For each replicate calculate `ΔCt = mexG Ct - rpoD Ct`, then average ΔCt by
strain. With equal amplification efficiencies,
`log2 fold change (ΔrhlI/wt) = -(mean ΔCt_ΔrhlI - mean ΔCt_wt)`.
