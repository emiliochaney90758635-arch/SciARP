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

# Nitrogen-pathway naming map

For cross-strain reporting, `Nitrogen cycle` is replaced by the equivalent category name `Nitrogen metabolism`; the two descriptions are interchangeable labels for the same KEGG process.
