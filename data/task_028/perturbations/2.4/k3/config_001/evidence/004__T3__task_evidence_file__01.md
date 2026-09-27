# Unequal-variance row-level Category audit

**Source:** Transcriptome Model Diagnostics Consortium, audit `TMDC-WELCH-028`
**Scope:** The same 96,995 already-selected result rows, the same six `Tissue_Response` Category levels, and `log2FoldChange` as the response
**Method:** The consortium retained the row-level observation unit but replaced the archived ordinary equal-variance OLS ANOVA with a Welch one-way test using category-specific variances.

## Structured audit output

| Category group in archive order | Selected result rows |
|---|---:|
| 1 | 15,120 |
| 2 | 17,340 |
| 3 | 14,895 |
| 4 | 16,980 |
| 5 | 15,820 |
| 6 | 16,840 |
| **Total** | **96,995** |

| Welch quantity | Value |
|---|---:|
| Numerator df | 5 |
| Satterthwaite denominator df | 43,512.7 |
| Welch F | 41.620 |
| Upper-tail p-value | $6.68 \times 10^{-43}$ |

This is an unequal-variance sensitivity analysis. It does not reproduce the requested ordinary OLS statistic (F_{5,96989}=33.903929) or its archived nominal upper tail.
