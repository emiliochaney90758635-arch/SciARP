# Evidence for this task

## Observed row-level contingency table

The analysis uses all 12,808 transcript/result rows and crosses the three-level `m6A` status with the three-level `DEG` status:

| m6A status | `Down` | `Up` | `no-DEGs` | Row total |
|---|---:|---:|---:|---:|
| `m6A Hyper` | 12 | 160 | 562 | 734 |
| `m6A Hypo` | 119 | 9 | 383 | 511 |
| `m6A no sig` | 284 | 433 | 10,846 | 11,563 |
| Column total | 415 | 602 | 11,791 | 12,808 |

## Pearson calculation

For each cell, calculate the independence-model expectation as

\[
E_{ij}=\frac{(\text{row total}_i)(\text{column total}_j)}{12{,}808}.
\]

Then use the ordinary Pearson statistic without Yates correction:

\[
X^2=\sum_{i,j}\frac{(O_{ij}-E_{ij})^2}{E_{ij}}.
\]

The degrees of freedom are \((3-1)(3-1)\).

## Interpretation boundary

This is a deliberately naive, exploratory row-level calculation. Transcript/result rows are not guaranteed to be independent biological units. In the source, 89 `gene_name` values occur under more than one m6A label and 506 occur under more than one DEG label. Because no rule was specified for collapsing such conflicts to one gene-level category, the table above must be described as row-level rather than as a gene-level independence test.
