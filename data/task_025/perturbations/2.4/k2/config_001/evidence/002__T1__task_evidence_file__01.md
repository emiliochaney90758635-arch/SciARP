# Dominant-transcript gene table

**Source:** Bladder Cancer Multi-omics Integration Core
**Input:** Transcript/result rows with m6A and DEG labels
**Method:** One representative transcript was selected per `gene_name` by the smallest joint rank of methylation and expression p-values. Its two labels were assigned to the gene before Pearson cross-classification.

| Gene-level m6A status | Down | Up | no-DEGs |
|---|---:|---:|---:|
| m6A Hyper | 5 | 50 | 205 |
| m6A Hypo | 60 | 4 | 63 |
| m6A no sig | 150 | 220 | 6,000 |

The core calculates row and column margins from this table, forms Pearson’s \(X^2\) with four degrees of freedom, and reports the chi-square upper-tail survival probability.
