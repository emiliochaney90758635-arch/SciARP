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

# Double-knockout-specific pathway induction in Pseudomonas quorum-sensing mutants

Heather B. Collins, Waleed S. Karim, Nanami Ito, and Miguel A. Serrano

## Abstract

Combined loss of LasI and RhlI can produce pathway responses absent from either single quorum-sensing knockout. We compared strongly upregulated gene sets from strains 97, 98, and the ΔlasIΔrhlI strain 99 with wildtype and performed KEGG over-representation analysis. The double knockout uniquely enriched **lipopolysaccharide biosynthesis** and **ribosome** pathways, while neither category passed correction in the single mutants. Shared respiratory and sulfur-associated pathways were excluded from the strain-99-specific set. These two functional categories define a distinctive double-knockout induction programme.
