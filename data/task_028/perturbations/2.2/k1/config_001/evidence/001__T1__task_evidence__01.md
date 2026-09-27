# Evidence for this task

## Selected result rows and model

The archived exploratory analysis first retains differential-expression result rows satisfying:

```text
padj < 0.05
abs(log2FoldChange) > 0.5
baseMean >= 10
```

It then combines tissue and response labels into a six-level categorical variable named `Category`. The resulting table contains 96,995 selected result rows, and the fitted row-level model is:

```text
log2FoldChange ~ C(Category)
```

The archived ordinary least-squares ANOVA table is:

| Source | Sum of squares | df | F |
|---|---:|---:|---:|
| `C(Category)` | \(7.444260\times10^3\) | 5 | 33.903929 |
| Residual | \(4.259160\times10^6\) | 96,989 | — |

## Nominal upper-tail definition

Use the archived statistic and degrees of freedom to evaluate the upper-tail survival probability \(P(F_{5,96989}\ge 33.903929)\), and report the computed value in ordinary scientific `e` notation.

## Interpretation boundary

The 96,995 observations are selected differential-expression result rows, not independent experimental subjects. The same `GeneID` can recur across contrasts, and rows were selected using significance and effect-size thresholds before the OLS/ANOVA fit. Consequently, the calculation contains both pseudo-replication and post-selection effects. Any resulting probability is a nominal row-level value from the archived exploratory model and should not be interpreted as a valid subject-level tissue-by-response inferential test.

# Category-level fold-change heterogeneity in selected mouse transcriptomic contrasts

Federica Leone, Shunpei Kato, Amara Diallo, and Neil W. Prescott

## Abstract

Exploratory aggregation of differential-expression results can reveal broad heterogeneity across tissue–response categories. We selected result rows passing adjusted-significance, fold-change, and abundance thresholds from an archived mouse paroxetine dataset and fitted a one-way model to log2 fold changes across six tissue–response categories. The category effect produced a nominal upper-tail probability of \(4.6\times10^{-12}\), indicating substantial row-level variation among the selected groups. Repeated GeneIDs and contrasts contributed multiple observations, and selection preceded model fitting; the probability therefore describes the archived result-row table rather than independent biological units. The analysis should be viewed as a descriptive screen for category structure.
