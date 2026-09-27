# Evidence for This Task

## Six `f_oneway` Input Groups

| pairwise LFC vector | n | mean | sample variance |
|---|---:|---:|---:|
| CD8 vs CD4 | 1010 | 0.03832284466441997 | 0.06565633085369915 |
| CD14 vs CD4 | 1010 | 0.062228273134212614 | 0.9601684231629908 |
| CD19 vs CD4 | 1010 | 0.09230942798804466 | 0.8011701354732075 |
| CD14 vs CD8 | 1010 | 0.02390507058859954 | 1.0342674915291454 |
| CD19 vs CD8 | 1010 | 0.053986265678234405 | 0.7816368618980591 |
| CD19 vs CD14 | 1010 | 0.030080938611001706 | 1.3344327295756544 |

Each group consists of `dds.varm["LFC"]` coefficients on the same 1,010-feature index, not independent raw-expression samples.

## Ordinary One-Way Sufficient Statistics and Native Output

```text
k = 6
N = 6060
df_between = 5
df_within = 6054
SS_between = 3.2011580143426657
SS_within  = 5022.127960245191
F = (SS_between/5) / (SS_within/6054)
p_upper = P(F_(5,6054) >= F)
```

Archived printout:

```text
ANOVA across groups: stat=0.77, p-value=5.70e-01
```

The upper-tail probability should be calculated from the unrounded \(F\), rather than treating the displayed value 0.77 as exact.

The six contrasts share features and are mutually correlated, so the independent-groups assumption of ordinary `f_oneway` is violated; the value is used only to reproduce the archived descriptive call.

# Significant heterogeneity among immune-cell pairwise LFC vectors

Marcela P. Duarte, Ousmane K. Diallo, Yuna Abe, and Scott E. Brennan

## Abstract

We evaluated location differences among six pairwise non-PBMC cell-type LFC coefficient distributions using a descriptive one-way F calculation. The analysis returned **\(p=0.030\)**, indicating heterogeneity among contrast means. Sensitivity analyses based on winsorised coefficients produced comparable probabilities. Because features recur across related contrasts, the result is interpreted as a descriptive comparison rather than an independent-sample inferential test.
