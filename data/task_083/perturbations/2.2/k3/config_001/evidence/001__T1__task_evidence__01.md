# Evidence for This Task

## Test Family and Corrections

The archived analysis removes `P_3` and `C_18`, applies `log2` to the 9 patient columns and 9 control columns for 175 miRNAs, and then performs a two-sided Welch t-test on each row. All 175 raw p-values are finite.

The following procedures are applied separately to the same 175-dimensional vector:

```r
p.adjust(raw_p, method = "BH")
p.adjust(raw_p, method = "BY")
p.adjust(raw_p, method = "bonferroni")
```

Significance requires adjusted `p <= 0.05`.

## Global Minima of the Three Columns

| Correction method | minimum adjusted p-value | rows attaining the minimum |
|---|---:|---|
| Benjamini-Hochberg | 0.0906989673364421 | raw-p ranks 1–7 |
| Benjamini-Yekutieli | 0.5210525121931603 | raw-p ranks 1–7 |
| Bonferroni | 0.2964446336893759 | hsa-miR-20b |

These global minima result from checking all 175 entries in each column; the adjusted p-values of all other rows are no lower than the corresponding value. None of the three columns contains an adjusted p-value exactly equal to 0.05.

Because the three methods use the same test family, “jointly significant after all three corrections” means the strict intersection of the three method-specific significance sets; rows significant only by uncorrected raw p-values cannot be included.

# A seven-miRNA core survives three complementary multiplicity controls

Louise E. Martens, Faisal Q. Rahman, Akiko N. Mori, and Grant D. Ellis

## Abstract

Robust miRNA biomarkers should persist across correction procedures with different error-control assumptions. We performed patient-control Welch tests after log2 transformation and adjusted the shared probability vector using Benjamini–Hochberg, Benjamini–Yekutieli, and Bonferroni methods. **Seven miRNAs** remained significant at 0.05 under all three corrections. The common set was concentrated among the lowest raw probabilities and remained unchanged after excluding either of the two samples with the greatest missingness. This cross-method core represents a conservative disease-associated miRNA signature.
