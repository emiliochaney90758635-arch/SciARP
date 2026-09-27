# Swarming-area model-comparison and grid evidence

## Common observations

All three candidate models use the same 39 rows. Six source rows with `StrainNumber` equal to `1` or `98` are removed, and each retained `Ratio=a:b` is converted to `a/(a+b)`.

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

The source column is named `Area` and has no recorded physical calibration unit.

## In-sample candidate fits

```r
quadratic_model <- lm(Area ~ poly(Frequency_rhlI, 2, raw=TRUE))
cubic_model     <- lm(Area ~ poly(Frequency_rhlI, 3, raw=TRUE))
spline_model    <- lm(Area ~ ns(Frequency_rhlI, df=4))
```

| model | parameters including intercept | residual df | SSE | ordinary R² | adjusted R² | residual SE |
|---|---:|---:|---:|---:|---:|---:|
| quadratic | 3 | 36 | 80,458,797,488.8762 | 0.350084461 | 0.313978042 | 47,301.9 |
| cubic | 4 | 35 | 51,111,863,206.8079 | 0.587599130 | 0.525250484 | 38,214.4 |
| natural spline | 5 | 34 | 24,021,703,352.2054 | 0.806178630 | 0.783376116 | 26,580.5 |

The stipulated in-sample heuristic favors greater ordinary and adjusted R² and smaller residual standard error. It is not a cross-validation or AIC comparison.

## Natural-spline grid values

For the natural spline, fitted means are evaluated on a 1,000-point equally spaced grid from 0.25 to 1, including both endpoints. `which.max` is applied to the fitted-mean column.

```r
frequency_seq <- seq(0.25, 1, length.out = 1000)
pred <- predict(
  spline_model,
  newdata = data.frame(Frequency_rhlI = frequency_seq),
  interval = "confidence"
)
selected_index <- which.max(pred[, "fit"])
```

Values remain in the source table's native `Area` units.

## Archived Cell 20 console output

```text
Peak fitness occurs at frequency (spline): 0.9076577
Peak fitness (mean area) at this frequency (spline): 184371.8
Confidence interval for peak fitness (spline): 157912.4 210831.3
```
