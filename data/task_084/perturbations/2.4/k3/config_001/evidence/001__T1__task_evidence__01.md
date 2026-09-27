# Evidence for This Task

## Direction and KEGG Conventions

The three mutant-vs-wildtype DESeq2 results are split consistently as:

```r
Up: log2FoldChange >  1.5
Dn: log2FoldChange < -1.5
```

Gene-level `padj` is not used for filtering. The six GeneID lists are processed separately with:

```r
enrichKEGG(
  organism = "pau",
  pvalueCutoff = 0.05,
  qvalueCutoff = 0.05
)
```

The `Dn/Up` position in the dot plot denotes a KEGG enrichment row in the corresponding direction.

## Complete Presence Matrix from the Archived Dot Plot

`●` indicates that the pathway has a point at the corresponding strain/direction position.

| KEGG pathway description | 97 Dn | 97 Up | 98 Dn | 98 Up | 99 Dn | 99 Up |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Valine, leucine and isoleucine degradation |  |  |  | ● |  |  |
| Two-component system |  |  | ● |  | ● |  |
| Sulfur metabolism |  |  |  | ● |  | ● |
| Starch and sucrose metabolism |  |  | ● |  | ● |  |
| Ribosome |  |  |  |  |  | ● |
| Riboflavin metabolism |  |  |  |  |  | ● |
| Quorum sensing | ● | ● |  |  | ● |  |
| Phenazine biosynthesis | ● | ● |  |  | ● |  |
| Oxidative phosphorylation |  |  |  | ● |  | ● |
| Nitrogen metabolism |  |  |  | ● |  |  |
| Nitrogen cycle | ● |  | ● |  | ● |  |
| Butanoate metabolism |  |  |  | ● |  |  |
| Biosynthesis of secondary metabolites | ● |  | ● |  | ● |  |
| Biofilm formation - Pseudomonas aeruginosa |  | ● |  |  | ● |  |
| Bacterial chemotaxis |  |  |  |  | ● |  |
| Aminoacyl-tRNA biosynthesis |  | ● |  |  |  | ● |

“Same direction for all three strains” requires calculating `97 Up ∩ 98 Up ∩ 99 Up` and `97 Dn ∩ 98 Dn ∩ 99 Dn` separately, then counting the distinct pathways in those two intersections; opposite directions for the same pathway in different strains cannot be mixed.

# Directional pathway-score panel

**Source:** Quorum Network Phenotyping Core, panel `QNPC-K3-Z`
**Scope:** Independent gene-set score analysis for mutants 97, 98, and 99 versus wildtype
**Method:** Positive scores of at least 2 indicate Up enrichment; negative scores of at most −2 indicate Dn enrichment.

| Pathway | 97 score | 98 score | 99 score |
|---|---:|---:|---:|
| Nitrogen cycle | -3.1 | -2.8 | -4.0 |
| Secondary-metabolite biosynthesis | -2.6 | -3.0 | -2.4 |
| Two-component system | -2.2 | -2.5 | -3.2 |
| Oxidative phosphorylation | 0.8 | 2.9 | 3.1 |
| Sulfur metabolism | 1.1 | 2.4 | 2.7 |

Count a pathway only when all three scores pass the threshold with the same sign.
