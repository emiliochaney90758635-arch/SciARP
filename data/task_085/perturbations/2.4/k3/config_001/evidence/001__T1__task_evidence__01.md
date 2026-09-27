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

# Independent up-pathway hit audit

**Source:** Bacterial Pathway Validation Lab, series `BPVL-QS-UP`
**Scope:** Upregulated genes from strains 97, 98, and 99 relative to wildtype
**Method:** A pathway is enriched when at least three member genes exceed log2FC 1.5 and its permutation q-value is below 0.05.

| Pathway | 97 qualifying hits | 98 qualifying hits | 99 qualifying hits | Strain-99 q-value |
|---|---:|---:|---:|---:|
| Protein export | 1 | 2 | 5 | 0.012 |
| Flagellar assembly | 0 | 1 | 4 | 0.021 |
| Sulfur metabolism | 2 | 4 | 5 | 0.018 |
| Oxidative phosphorylation | 1 | 4 | 4 | 0.023 |
| Ribosome | 3 | 2 | 3 | 0.041 |

Exclusive strain-99 categories pass the criterion in strain 99 and fail the hit threshold in both single mutants.
