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
| Porphyrin metabolism | ● | ● |
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

# KEGG identifier overlap export

**Source:** Microbial Pathway Informatics Service, export `MPIS-DN-ID`
**Scope:** Pathway-level significant Dn results from FeMinus and Succ analyses
**Method:** Gene lists used log2FC \(<-1.5\); KEGG pathway p- and q-value cutoffs were both 0.05. The export retains stable KEGG map identifiers before description cleaning.

```text
FeMinus Dn:
pau00190, pau00360, pau00650, pau00860, pau01100, pau01110,
pau02020, pau03070

Succ Dn:
pau00030, pau00190, pau00630, pau00650, pau00860, pau01100,
pau01110, pau01503, pau02020
```

The common-pathway count is the cardinality of the strict identifier intersection.
