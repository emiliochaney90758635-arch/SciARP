# Evidence for This Task

## Archived Execution Criteria

FeMinus and Succ each use MMGluFePlus as their reference. The gene lists for each condition use:

```r
Up: log2FoldChange > 1.5
Dn: log2FoldChange < -1.5
```

No gene-level `padj` filter is applied. Each of the four lists is processed with `enrichKEGG(organism="pau", pvalueCutoff=0.05, qvalueCutoff=0.05)`; both cutoffs apply to pathway-level output. Set operations are performed on pathway descriptions only after removal of the same organism suffix.

## Point-by-Point Matrix from the Archived Dot Plot

| Cleaned Pathway | FeMinus Dn | FeMinus Up | Succ Dn | Succ Up |
|---|:---:|:---:|:---:|:---:|
| Sulfur metabolism | — | — | — | ● |
| Styrene degradation | ● | — | — | — |
| Quorum sensing | ● | — | — | — |
| Porphyrin metabolism | ● | — | ● | — |
| Phenazine biosynthesis | ● | — | ● | — |
| Pentose phosphate pathway | — | — | ● | — |
| Oxidative phosphorylation | ● | — | ● | — |
| Microbial metabolism in diverse environments | ● | — | ● | — |
| Glyoxylate and dicarboxylate metabolism | — | — | ● | — |
| Cyanoamino acid metabolism | ● | — | — | — |
| Cationic antimicrobial peptide (CAMP) resistance | — | — | ● | — |
| Carbon metabolism | — | — | ● | — |
| Biosynthesis of secondary metabolites | ● | — | ● | — |
| Bacterial secretion system | — | — | — | ● |
| ABC transporters | — | ● | — | ● |

`●` indicates a point at the corresponding Media/Regulation/Description coordinate. First take the union of `Up` and `Dn` names within each medium, then calculate the set difference using complete cleaned names; a name appearing more than once within the same medium is counted only once.

# Medium-specific KEGG programmes in iron-depleted and succinate-grown Pseudomonas aeruginosa

Ruth A. Koenig, Sameer V. Kulkarni, Ayumi Takeda, and Lionel J. Foster

## Abstract

Iron availability and carbon source elicit overlapping but nonidentical pathway programmes in *Pseudomonas aeruginosa*. We combined induced and repressed KEGG enrichments within iron-depleted glucose and succinate media after applying common fold-change and pathway-significance thresholds. Set comparison identified **five** enriched pathways that occurred under FeMinus but not Succ. The medium-specific component included signalling, aromatic-compound degradation, and specialised metabolic functions. The result was unchanged after collapsing regulation direction within each medium. Iron depletion therefore produces a sizeable pathway repertoire not observed during succinate growth.
