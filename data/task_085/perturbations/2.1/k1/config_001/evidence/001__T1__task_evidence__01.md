# Evidence for This Task

## Up-Gene Lists and Enrichment

For each of the three mutant-vs-wildtype results, an Up GeneID list is formed using the strict condition `log2FoldChange > 1.5`. Although the gene-level `padj` column is retained, the archived code does not use it to filter genes. The three lists are processed separately with:

```r
enrichKEGG(
  organism = "pau",
  pvalueCutoff = 0.05,
  qvalueCutoff = 0.05
)
```

The adjusted p-value condition in the task refers to the pathway enrichment results.

## All Up Pathways in the Archived Dot Plot

`●` indicates that the corresponding pathway appears in the strain's Up column.

| KEGG pathway description | 97 Up | 98 Up | 99 Up |
|---|:---:|:---:|:---:|
| Valine, leucine and isoleucine degradation |  | ● |  |
| Sulfur metabolism |  | ● | ● |
| Ribosome |  |  | ● |
| Riboflavin metabolism |  |  | ● |
| Quorum sensing | ● |  |  |
| Phenazine biosynthesis | ● |  |  |
| Oxidative phosphorylation |  | ● | ● |
| Nitrogen metabolism |  | ● |  |
| Butanoate metabolism |  | ● |  |
| Biofilm formation - Pseudomonas aeruginosa | ● |  |  |
| Aminoacyl-tRNA biosynthesis | ● |  | ● |

The archived point counts are 97 Up=4, 98 Up=5, and 99 Up=5. The requested exclusive set is calculated using exact names:

```text
U99 \ (U97 ∪ U98)
```

# KEGG category harmonisation note

`Ribosome` and `Riboflavin metabolism` are both represented by the parent functional category `Ribosomal function` in cross-strain comparisons and are counted as one category.
