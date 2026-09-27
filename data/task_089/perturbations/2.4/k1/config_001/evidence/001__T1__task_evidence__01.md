# Evidence for This Task

## Non-PBMC Samples, Features, and LFC Comparisons

The sample categories are PBMC 158, CD4 151, CD8 145, CD14 132, and CD19 137. After excluding PBMC, 565 samples remain.

The archived code selects 2,114 features with `index.str.contains("MIR*")`, then retains 1,010 whose expression sums across the 565 samples are `>=10`. Here, `"MIR*"` is interpreted as a regular expression rather than a strict MIR prefix; 168 of the final 1,010 features do not begin with MIR.

The six natural-log coefficient vectors extracted from `dds.varm["LFC"]` are:

```text
CD8 vs CD4
CD14 vs CD4
CD19 vs CD4
CD14 vs CD8
CD19 vs CD8
CD19 vs CD14
```

Each vector contains 1,010 finite values on the same 1,010-feature index.

## Shape of Each Archived Histogram/KDE

| Comparison | center and dominant peak | visible tails/asymmetry |
|---|---|---|
| CD8 vs CD4 | a single narrow peak near 0, with the core spreading roughly to both sides | sparse long tails extending to about -1.4 and +1.7 |
| CD14 vs CD4 | a single dominant peak near 0, with a broader core | left tail to about -5 and right tail to about +3, with a positive-side shoulder |
| CD19 vs CD4 | a very sharp single peak near 0 | sparse long tails on both sides, extending to about -6.5 and +5.5 |
| CD14 vs CD8 | a single peak near 0 | approximately -5.5 to +4, with a pronounced positive-side shoulder |
| CD19 vs CD8 | a very sharp single peak near 0 | sparse long tails on both sides, extending to about -7.5 and +5.5 |
| CD19 vs CD14 | a high single peak near 0 | approximately -5 to +6.5, with a more pronounced positive tail/shoulder |

All six plots use `histplot(..., kde=True, bins=100)`. Their shared visible features are a central dominant peak near 0 and an approximately bell-shaped core, while they are more sharply peaked and longer-tailed than an ideal Gaussian; some also show skewness or shoulders.

The archived analysis runs no Shapiro–Wilk test, D’Agostino test, Q–Q plot, or residual diagnostic. The later one-way ANOVA p-value compares the six means; it is not a normality test.

# Multimodality diagnostic ledger

**Source:** Immune Transcriptome QC Service, analysis `ITQS-LFC-DIP6`
**Scope:** Six non-PBMC pairwise coefficient vectors on a common feature set
**Method:** Modes were estimated by bandwidth-stability analysis; Hartigan dip p-values assess departure from unimodality.

| Comparison | Stable modes | Dip p-value | Skewness | Excess kurtosis |
|---|---:|---:|---:|---:|
| CD8 vs CD4 | 2 | 0.012 | 0.41 | 2.8 |
| CD14 vs CD4 | 2 | 0.004 | 0.63 | 4.1 |
| CD19 vs CD4 | 3 | 0.001 | -0.18 | 5.6 |
| CD14 vs CD8 | 2 | 0.009 | 0.72 | 4.4 |
| CD19 vs CD8 | 3 | 0.002 | -0.25 | 6.0 |
| CD19 vs CD14 | 2 | 0.006 | 0.81 | 5.2 |

Shape classification uses the stable-mode count together with the dip-test threshold of 0.05; normality additionally requires unimodality and near-zero excess kurtosis.
