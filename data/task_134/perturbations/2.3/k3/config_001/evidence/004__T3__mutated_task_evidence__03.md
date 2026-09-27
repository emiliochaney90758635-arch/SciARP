# Natural-spline overall-F evidence

## Regression observations

The model excludes six source rows with `StrainNumber` equal to `1` or `98`. For each retained `Ratio=a:b`, frequency is `a/(a+b)`. The resulting 39 observations are:

| Ratio (ΔrhlI:ΔlasI) | Frequency_rhlI | Area A | Area B | Area C |
|---|---:|---:|---:|---:|
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
| 1:0 | 1 | 9,841 | 10,173 | 10,799 |

The fitted formula is:

```r
lm(Area ~ ns(Frequency_rhlI, df = 4))
```

It contains an intercept and four natural-spline columns.

## Overall regression quantities

| statistic | value |
|---|---:|
| n | 39 |
| total SS | 123,937,331,313.58975 |
| regression SS | 99,915,627,961.38391 |
| residual SS | 24,021,703,352.20585 |
| model df | 5 |
| residual df | 33 |
| model MS | 24,978,906,990.34598 |
| residual MS | 706,520,686.8295838 |

The overall statistic and its right-tail probability are defined by:

```text
F = (Regression SS / 4) / (Residual SS / 34)
P = P(F[4,34] >= observed F)
```

At full precision:

| quantity | value |
|---|---:|
| F | 33.3548133210868 |
| upper-tail probability | 1.1305618250678e-11 |

The archived summary displays:

```text
F-statistic: 35.35 on 4 and 34 DF
p-value: 1.131e-11
```

The overall F probability is distinct from the four individual spline-basis t-test p-values (`2.32e-05`, `5.77e-09`, `0.165`, `0.217`) and from the overall p-values of the quadratic or cubic models.
