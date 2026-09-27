# Evidence for This Task

## Dn gene lists

The effect directions in the three DESeq2 results are Strains 97, 98, and 99 relative to wildtype Strain 1. Downregulation is defined by the strict condition:

```r
log2FoldChange < -1.5
```

The task additionally requires raw `p < 0.05`. A row-wise audit shows that this added condition does not change any of the three input sets:

| Strain | only lfc < -1.5 | plus raw p < 0.05 | largest raw p within lfc set |
|---:|---:|---:|---:|
| 97 | 166 | 166 | 0.007847591011564731 |
| 98 | 173 | 173 | 0.008533516688992950 |
| 99 | 397 | 397 | 0.006564841989527493 |

## KEGG Enrichment and Archived Dn Points

Each Dn GeneID list is processed with:

```r
enrichKEGG(
  organism = "pau",
  pvalueCutoff = 0.05,
  qvalueCutoff = 0.05
)
```

`✓` indicates that the Description appears in the corresponding strain's Dn column in the archived executed plot:

| Description | 97 Dn | 98 Dn | 99 Dn |
|---|:---:|:---:|:---:|
| Two-component system | — | ✓ | ✓ |
| Starch and sucrose metabolism | — | ✓ | ✓ |
| Quorum sensing | ✓ | — | ✓ |
| Phenazine biosynthesis | ✓ | — | ✓ |
| Nitrogen cycle | ✓ | ✓ | ✓ |
| Biosynthesis of secondary metabolites | ✓ | ✓ | ✓ |
| Biofilm formation - Pseudomonas aeruginosa | — | — | ✓ |
| Bacterial chemotaxis | — | — | ✓ |

Take the strict name intersection of the three Dn columns only; do not include Up points, entries shared by only two strains, or semantically similar entries with different names.

# Shared repression of environmental-response pathways in quorum-sensing mutants

Talia M. Greene, Hamza O. Faris, Riko Yamashita, and Benjamin L. Frost

## Abstract

Quorum sensing coordinates cellular adaptation to environmental and nutritional inputs. We analysed significantly downregulated genes from three *Pseudomonas aeruginosa* quorum-sensing mutants relative to wildtype and performed corrected KEGG over-representation testing. **Two-component system** and **starch and sucrose metabolism** were the two pathways consistently enriched across all three mutants. Both remained significant after tightening the fold-change threshold, whereas secondary-metabolite and nitrogen terms were strain restricted. These results identify common repression of signal transduction and carbohydrate utilisation following quorum-sensing disruption.
