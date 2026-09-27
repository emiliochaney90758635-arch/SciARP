# Evidence for This Task

## Gene-List and Pathway Filtering Levels

Both FeMinus and Succ use MMGluFePlus as the reference. The archived downregulated gene lists use:

```r
filter(log2FoldChange < -1.5)
```

No gene-level `padj < 0.05` filter is applied. Each GeneID list is then supplied to:

```r
enrichKEGG(
  organism = "pau",
  pvalueCutoff = 0.05,
  qvalueCutoff = 0.05
)
```

The 0.05 cutoffs apply to pathway-level output. All pathway descriptions are compared only after removal of the same organism suffix.

## `Dn` Point Locations in the Archived Dot Plot

| Cleaned pathway description | FeMinus · Dn | Succ · Dn |
|---|:---:|:---:|
| Sulfur metabolism | — | — |
| Styrene degradation | ● | — |
| Quorum sensing | ● | — |
| Porphyrin metabolism | ? | ● |
| Phenazine biosynthesis | ● | ● |
| Pentose phosphate pathway | — | ● |
| Oxidative phosphorylation | ● | ● |
| Microbial metabolism in diverse environments | ● | ● |
| Glyoxylate and dicarboxylate metabolism | — | ● |
| Cyanoamino acid metabolism | ● | — |
| Cationic antimicrobial peptide (CAMP) resistance | — | ● |
| Carbon metabolism | — | ● |
| Biosynthesis of secondary metabolites | ● | ● |
| Bacterial secretion system | — | — |
| ABC transporters | — | — |

`●` indicates an enrichment point at the corresponding `Dn` coordinate, whereas `—` indicates no point. The intersection uses strict matching of complete cleaned strings and does not merge names based on similar meaning, color, or point size.
