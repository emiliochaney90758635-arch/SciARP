# Evidence for This Task

## Common Test Family

After removing `P_3` and `C_18`, each miRNA uses the nonmissing observations from 9 patient columns and 9 control columns. The data are first transformed element by element with `log2`, followed by a two-sided Welch t-test on each row. All 175 unique miRNAs yield finite raw p-values; every correction is applied simultaneously to the same set of \(m=175\) p-values.

## Correction Definitions

```r
p.adjust(raw_p, method = "BY")
p.adjust(raw_p, method = "bonferroni")
```

For the ordered \(p_{(i)}\):

```text
Bonferroni_i = min(1, 175 × p_i)
BH_(i)       = min(1, min_{j≥i}(175 × p_(j) / j))
BY_(i)       = min(1, H_175 × BH_(i))
H_175        = 5.74485606060264
```

## Lower End of the Corrected Results

| raw p rank | miRNA | raw p | BY adjusted p | Bonferroni adjusted p |
|---:|---|---:|---:|---:|
| 1 | hsa-miR-20b | 0.001693969335367862 | 0.5210525121931603 | 0.2964446336893759 |
| 2 | hsa-miR-486-5p | 0.002338661310880471 | 0.5210525121931603 | 0.4092657294040825 |
| 3 | hsa-miR-92a | 0.002638393575172587 | 0.5210525121931603 | 0.4617188756552028 |
| 4 | hsa-miR-222 | 0.002818847657179876 | 0.5210525121931603 | 0.4932983400064783 |
| 5 | hsa-miR-532-5p | 0.003348653571836516 | 0.5210525121931603 | 0.5860143750713902 |
| 6 | hsa-miR-1974 | 0.003570927233302876 | 0.5210525121931603 | 0.6249122658280032 |
| 7 | hsa-miR-34a | 0.003627958693457684 | 0.5210525121931603 | 0.6348927713550947 |
| 8 | hsa-miR-30e | 0.005001735035416723 | 0.5800823169617981 | 0.8753036311979264 |

The minimum BY-adjusted p-value in the full column is `0.5210525121931603`; the minimum Bonferroni-adjusted p-value in the full column is `0.2964446336893759`. Every omitted row is at least as large as these global minima in the corresponding correction column. Significance requires adjusted `p <= 0.05`.

# Cross-platform adjustment summary

**Source:** Statistical Genomics Verification Center, run `SGVC-MIR-ADJ175`
**Scope:** A common family of 175 finite raw miRNA p-values
**Method:** Corrections were recalculated with validated high-precision routines. Corrected probabilities were exported in disjoint bins.

| Corrected-p interval | Bonferroni count | Benjamini–Yekutieli count |
|---|---:|---:|
| \(0\le p_{adj}\le0.01\) | 0 | 1 |
| \(0.01<p_{adj}\le0.05\) | 1 | 1 |
| \(0.05<p_{adj}\le0.10\) | 0 | 3 |
| \(0.10<p_{adj}\le1\) | 174 | 170 |

The requested ratio uses the sum of significant bins for each method, in Bonferroni:Benjamini–Yekutieli order.
