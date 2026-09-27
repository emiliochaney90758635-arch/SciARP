# Evidence for This Task

## Actual Inputs to `f_oneway`

After PBMC exclusion, 565 samples remain. The archived regular-expression selection and low-expression filter yield 1,010 features, 168 of which do not begin with `MIR`. SciPy `f_oneway` receives six pairwise `dds.varm["LFC"]` coefficient vectors, not raw-expression samples from the four cell types.

| ANOVA group | n | mean | sample variance \(s^2\) |
|---|---:|---:|---:|
| celltype_CD8_vs_CD4 | 1010 | 0.03832284466441997 | 0.06565633085369915 |
| celltype_CD14_vs_CD4 | 1010 | 0.062228273134212614 | 0.9601684231629908 |
| celltype_CD19_vs_CD4 | 1010 | 0.09230942798804466 | 0.8011701354732075 |
| celltype_CD14_vs_CD8 | 1010 | 0.02390507058859954 | 1.0342674915291454 |
| celltype_CD19_vs_CD8 | 1010 | 0.053986265678234405 | 0.7816368618980591 |
| celltype_CD19_vs_CD14 | 1010 | 0.030080938611001706 | 1.3344327295756544 |

Each of the six columns contains 1,010 finite natural-log coefficients.

## Ordinary One-Way Arithmetic

```text
grand_mean = Σ(n_i × mean_i) / Σn_i
SS_between = Σ[n_i × (mean_i - grand_mean)²]
SS_within  = Σ[(n_i - 1) × s_i²]
df_between = 6 - 1
df_within  = 6060 - 6
F = (SS_between / df_between) / (SS_within / df_within)
```

The table above gives:

```text
SS_between = 3.2011580143426657
SS_within  = 5022.127960245191
```

The same 1,010 features recur across the six pairwise contrasts, which are also algebraically dependent; the independence assumption of an ordinary independent-groups ANOVA is therefore violated. This calculation can only reproduce the archived code and cannot be interpreted as a valid ANOVA of raw expression across the four cell types.
