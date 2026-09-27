# Natural-spline swarming-area model evidence

## Complete model input

After excluding the six rows whose `StrainNumber` is `1` or `98`, each `Ratio=a:b` is converted by:

```text
Frequency_rhlI = a / (a + b)
```

All three area replicates remain separate observations:

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

There are 39 rows and 13 frequency levels spanning `[0.25, 1]`.

## Four-degree-of-freedom natural spline

The fitted model is:

```r
lm(Area ~ ns(Frequency_rhlI, df = 4))
```

The natural-spline basis uses boundary knots `0.25` and `1`, with internal knots:

```text
0.666666666667
0.833333333333
0.990099009901
```

The regression has an intercept plus four spline columns.

| quantity | value |
|---|---:|
| n | 39 |
| design-matrix rank | 5 |
| residual degrees of freedom | 34 |
| SSE | 24,021,730,352.2054 |
| SST | 123,937,313,313.5898 |
| residual standard error | 26,580.4569 |

```text
ordinary R^2 = 1 - SSE / SST
adjusted R^2 = 0.783376115857
```

The archived summary displays:

```text
Multiple R-squared: 0.8062
Adjusted R-squared: 0.7834
```
