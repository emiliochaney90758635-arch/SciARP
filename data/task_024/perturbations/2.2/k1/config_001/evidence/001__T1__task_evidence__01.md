# Evidence for this task

## Observed row-level contingency table

The analysis uses all 12,754 transcript/result rows and crosses the three-level `m6A` status with the three-level `DEG` status:

| m6A status | `Down` | `Up` | `no-DEGs` | Row total |
|---|---:|---:|---:|---:|
| `m6A Hyper` | 12 | 106 | 562 | 680 |
| `m6A Hypo` | 119 | 9 | 383 | 511 |
| `m6A no sig` | 284 | 433 | 10,846 | 11,563 |
| Column total | 415 | 548 | 11,791 | 12,754 |

## Pearson calculation

For each cell, calculate the independence-model expectation as

\[
E_{ij}=\frac{(\text{row total}_i)(\text{column total}_j)}{12{,}754}.
\]

Then use the ordinary Pearson statistic without Yates correction:

\[
X^2=\sum_{i,j}\frac{(O_{ij}-E_{ij})^2}{E_{ij}}.
\]

The degrees of freedom are \((3-1)(3-1)\).

## Interpretation boundary

This is a deliberately naive, exploratory row-level calculation. Transcript/result rows are not guaranteed to be independent biological units. In the source, 89 `gene_name` values occur under more than one m6A label and 506 occur under more than one DEG label. Because no rule was specified for collapsing such conflicts to one gene-level category, the table above must be described as row-level rather than as a gene-level independence test.

# Row-level association between m6A state and expression class in bladder cancer

Vera Lindholm, Akira Nishimura, Tolu Ajayi, and Gregory P. Sloan

## Abstract

Joint methylation and expression summaries provide a first view of epitranscriptomic–transcriptional coupling in cancer. We cross-classified transcript-level bladder-cancer results into three m6A states and three differential-expression states and evaluated the complete table with an ordinary Pearson independence statistic. The 12,754 result rows produced a chi-square statistic of 612.8 with four degrees of freedom, reflecting a marked excess of upregulated records among the hypermethylated class and downregulated records among the hypomethylated class. The association remained prominent in sensitivity analyses that removed duplicate transcript accessions. Because multiple rows can originate from one gene, the result is an exploratory record-level association and does not establish gene-level independence.
