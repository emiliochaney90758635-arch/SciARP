# Natural-spline pointwise confidence-interval evidence

## Complete regression input

After excluding six rows whose `StrainNumber` is `1` or `98`, frequency is constructed from each `Ratio=a:b` as `a/(a+b)`. The 39 model rows are:

| Ratio (ΔrhlI:ΔlasI) | Frequency_rhlI | Area A | Area B | Area C |
|---|---:|---:|---:|---:|
| 1:0 | 1 | 9,841 | 10,173 | 10,799 |
| 1:3 | 0.25 | 17,327 | 19,749 | 19,206 |
| 1:2 | 0.333333333333333 | 29,886 | 26,359 | 24,189 |
| 1:1 | 0.5 | 32,388 | 47,048 | 50,235 |
| 2:1 | 0.666666666666667 | 62,165 | 67,375 | 131,630 |
| 3:1 | 0.75 | 96,584 | 76,362 | 94,430 |
| 4:1 | 0.8 | 137,316 | 130,242 | 189,336 |
| 5:1 | 0.833333333333333 | 127,082 | 122,640 | 104,537 |
| 10:1 | 0.909090909090909 | 129,141 | 185,482 | 238,479 |
| 50:1 | 0.980392156862745 | 92,265 | 116,187 | 73,305 |
| 100:1 | 0.990099009900990 | 85,812 | 85,686 | 51,863 |
| 500:1 | 0.998003992015968 | 10,623 | 9,175 | 10,341 |
| 1000:1 | 0.999000999000999 | 14,736 | 73,579 | 47,991 |

The response is the source column `Area`; no physical calibration unit is recorded.

## Spline fit and selected prediction row

The model is:

```r
lm(Area ~ ns(Frequency_rhlI, df = 4))
```

A 1,000-point equally spaced grid spans 0.25 to 1, with both endpoints included. `predict(..., interval="confidence")` returns `fit`, `lwr`, and `upr`, and `which.max` is applied only to `fit`.

| R grid index | Frequency_rhlI | fit |
|---:|---:|---:|
| 876 | 0.906906906907 | 184,366.879047 |
| 877 | 0.907657657658 | 184,371.846023 |
| 878 | 0.908408408408 | 184,362.612828 |

Index 877 is the unique fitted-mean maximum on this grid.

## Pointwise mean-interval quantities at index 877

The natural-spline fit has an intercept and four spline-basis columns.

| quantity | value |
|---|---:|
| observations | 39 |
| residual degrees of freedom | 34 |
| residual SSE | 24,021,703,352.2054 |
| MSE | 706,520,686.829571 |
| fitted-mean standard error at index 877 | 13,019.807256351 |
| `t(0.975,34)` | 2.032244509318 |
| fitted mean at index 877 | 184,371.846023070 |

The pointwise 95% confidence interval for the fitted mean is:

```text
lwr = fit - t × SE_mean
upr = fit + t × SE_mean
```

This is a pointwise confidence interval for the mean response at the selected grid coordinate. It is neither an individual-observation prediction interval nor a simultaneous interval corrected for selecting the largest of 1,000 fitted means.
