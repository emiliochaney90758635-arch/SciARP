# Evidence for this task

## Contingency table and test statistic

The analysis uses 12,754 transcript/result rows:

| m6A status | `Down` | `Up` | `no-DEGs` | Row total |
|---|---:|---:|---:|---:|
| `m6A Hyper` | 12 | 106 | 562 | 680 |
| `m6A Hypo` | 119 | 9 | 383 | 511 |
| `m6A no sig` | 284 | 433 | 10,846 | 11,563 |
| Column total | 415 | 548 | 11,791 | 12,754 |

Under independence, \(E_{ij}=(\text{row total}_i)(\text{column total}_j)/12{,}754\).
The ordinary Pearson statistic, with no Yates correction, is

\[
X^2=\sum_{i,j}\frac{(O_{ij}-E_{ij})^2}{E_{ij}},
\]

with \(df=(3-1)(3-1)\). Carry the unrounded statistic obtained from this table into the upper-tail calculation.

## Upper-tail probability

Evaluate the nominal upper-tail probability from the chi-square survival function,
\[
P(\chi^2_{df}\ge X^2),
\]
using the unrounded \(X^2\) and report it in scientific notation.

## Interpretation boundary

The calculation treats transcript/result rows as independent. That assumption is exploratory: 89 `gene_name` values appear under multiple m6A labels and 506 appear under multiple DEG labels. No conflict-resolution rule was supplied for a gene-level collapse, so the probability must be identified as a naive row-level result rather than a gene-level inferential result.

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
