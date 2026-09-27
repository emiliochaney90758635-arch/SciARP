# Natural-spline grid-search evidence

## Frequency–area observations

Six rows with `StrainNumber` equal to `1` or `98` are excluded. For each retained `Ratio=a:b`,

```text
Frequency_rhlI = a / (a + b)
```

The three area replicates at each frequency are separate model rows:

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

There are 39 observations over 13 frequency levels.

## Natural spline and archived grid

```r
spline_model <- lm(
  Area ~ ns(Frequency_rhlI, df = 4),
  data = tidy_area
)

frequency_seq <- seq(0.25, 1, length.out = 1000)
pred <- predict(
  spline_model,
  newdata = data.frame(Frequency_rhlI = frequency_seq),
  interval = "confidence"
)
selected_index <- which.max(pred[, "fit"])
```

The grid includes both endpoints and has step:

```text
(1 - 0.25) / 999 = 0.000750750750751
```

The requested coordinate is the `frequency_seq` value at `selected_index`.
A continuous curve optimizer would target a different quantity from the
specified discrete-grid search.

## Archived Cell 20 console output

```text
Peak fitness occurs at frequency (spline): 0.9076577
Peak fitness (mean area) at this frequency (spline): 184371.8
```
