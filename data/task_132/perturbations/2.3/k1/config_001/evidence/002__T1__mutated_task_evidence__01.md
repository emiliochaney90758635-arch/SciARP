# Cubic swarming-area model evidence

## Frequency and area observations

The source table has 45 records. Six records whose `StrainNumber` is `1` or `98` are excluded. For each remaining `Ratio=a:b`,

```text
Frequency_rhlI = a / (a + b)
```

The 39 retained observations are shown without loss by grouping the three independent area replicates at each frequency:

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

Each replicate remains a separate regression row. The source table does not state a physical unit for `Area`.

## Raw-power cubic OLS fit

The model contains an intercept and raw first, second, and third powers:

```text
Area = b0 + b1*x + b2*x^2 + b3*x^3 + error
x = Frequency_rhlI
```

| quantity | value |
|---|---:|
| n | 39 |
| fitted parameters | 4 |
| residual degrees of freedom | 35 |
| mean Area | 73,373.4358974359 |
| b0 | 428,376.063362908 |
| b1 | -2,731,968.81963712 |
| b2 | 5,399,762.02461135 |
| b3 | -3,050,542.14276508 |
| residual sum of squares, SSE | 51,111,836,206.8076 |
| total sum of squares, SST | 123,937,331,313.590 |

Ordinary and adjusted coefficients of determination are distinct:

```text
ordinary R^2 = 1 - SSE / SST
adjusted R^2 = 0.552250484458990
```

The archived model summary displays `Multiple R-squared: 0.5876` and `Adjusted R-squared: 0.5523`.
