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

# Extreme row-level dependence of RNA methylation and expression states in bladder cancer

Giulia Marini, Takeshi Endo, Ifeoma Eze, and Jonathan R. Cole

## Abstract

Joint categorical analysis can quantify alignment between RNA modification and expression outcomes in cancer datasets. We formed a 3×3 table from 12,754 transcript-level bladder-cancer records classified by m6A status and differential-expression status. An ordinary Pearson test without continuity correction yielded four degrees of freedom and an upper-tail probability of \(3.7\times10^{-128}\). Hypermethylated records were enriched in the upregulated class, whereas hypomethylated records were concentrated among downregulated transcripts. The exceptionally small probability indicates strong record-level dependence, but repeated transcripts from the same gene violate biological independence and restrict the result to exploratory description.
