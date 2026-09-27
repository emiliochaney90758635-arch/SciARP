# Gene-collapsed category ANOVA certificate

**Source:** Mouse Transcriptome Statistical Review Unit
**Input:** Selected differential-expression rows from the six tissue–response categories
**Method:** Recurring observations for the same GeneID and category were averaged before fitting `mean_log2FoldChange ~ C(Category)`.

| Source | Sum of squares | df |
|---|---:|---:|
| `C(Category)` | 350.0 | 5 |
| Residual | 1,500,000.0 | 21,245 |

The unit computes the F ratio from the two mean squares and evaluates its upper tail using the displayed numerator and residual degrees of freedom.
