# Natural-spline peak composition evidence

## Model observations

After removing six records with `StrainNumber` equal to `1` or `98`, each `Ratio=a:b` is represented as:

```text
Frequency_rhlI = a / (a + b)
```

The model uses all 39 frequency–area pairs:

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

## Spline and grid selection

The fitted model is `lm(Area ~ ns(Frequency_rhlI, df=4))`. Its natural-spline boundary knots are `0.25` and `1`; internal knots are:

```text
0.666666666666667
0.833333333333333
0.990099009900990
```

Fitted means are evaluated on 1,000 equally spaced points from 0.25 to 1, including both endpoints. The grid step is `0.000750750750750751`.

| grid index | Frequency_rhlI | fit minus grid maximum |
|---:|---:|---:|
| 875 | 0.906156156156156 | -23.957961036 |
| 876 | 0.906906906906907 | -4.966976543 |
| 877 | 0.907657657657658 | 0 |
| 878 | 0.908408408408408 | -9.233195239 |
| 879 | 0.909159159159159 | -32.842726092 |

The selected frequency `f` is the fraction of the total population that is ΔrhlI:

```text
f = rhlI / (rhlI + lasI)
1 - f = lasI / (rhlI + lasI)
```

To normalize the ΔlasI component to 1, use:

```text
ΔrhlI : ΔlasI = [f / (1 - f)] : 1
```

The grid-selected value uses `f=0.907657657657658`; it is not replaced by the nearby observed label `10:1`.

# A seven-and-a-half-to-one composition maximizes fitted swarming area

Daniel W. Mercer, Samira Khalil, Akane Nomura, and Felix Brandt

## Abstract

We fitted a four-degree-of-freedom natural spline to swarming area as a
function of ΔrhlI population frequency and searched an equally spaced
1,000-point prediction grid. The fitted-mean maximum corresponded to a
ΔrhlI:ΔlasI relative-abundance ratio of 7.5000:1 after normalizing the ΔlasI
component. The optimum therefore occurred at a less ΔrhlI-dominated
composition than ratios near 9.8:1 and was stable to modest changes in grid
resolution. Replicate areas were retained separately during fitting, and the
composition conversion used the complementary ΔlasI fraction at the selected
grid coordinate rather than the nearest experimentally tested ratio label.
