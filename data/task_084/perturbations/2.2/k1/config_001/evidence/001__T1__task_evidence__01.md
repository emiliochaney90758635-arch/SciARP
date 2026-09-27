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

# Conserved pathway responses across three Pseudomonas quorum-sensing mutants

Jenna M. Rocha, Qasim A. Nadeem, Fumie Hoshino, and Calvin R. Briggs

## Abstract

Quorum-sensing lesions remodel multiple metabolic and regulatory systems in *Pseudomonas aeruginosa*. We separated strongly induced and repressed genes in three mutant strains relative to wildtype and performed direction-specific KEGG over-representation analysis. **Four pathways** were significantly enriched in the same direction across all three mutants. The conserved group included regulatory and metabolic functions and remained unchanged after imposing an additional raw-expression filter. These shared pathway responses define a common transcriptional consequence of quorum-sensing disruption.
