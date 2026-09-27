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

# Gene-collapsed category ANOVA certificate

**Source:** Mouse Transcriptome Statistical Review Unit
**Input:** Selected differential-expression rows from the six tissue–response categories
**Method:** Recurring observations for the same GeneID and category were averaged before fitting `mean_log2FoldChange ~ C(Category)`.

| Source | Sum of squares | df |
|---|---:|---:|
| `C(Category)` | 350.0 | 5 |
| Residual | 1,500,000.0 | 21,245 |

The unit computes the F ratio from the two mean squares and evaluates its upper tail using the displayed numerator and residual degrees of freedom.
