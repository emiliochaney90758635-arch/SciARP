# Evidence for this task

## Measurement fields and grouping

`Circularity` is the image-derived circularity measurement. It is distinct from
the neighboring `Area` and `Round` fields. Group means are arithmetic means
within each `StrainNumber × Ratio` group.

Both relevant strains occur only at the single-strain ratio `1:0`. Their
complete nonmissing observations are:

| StrainNumber | Ratio | Replicate | Circularity |
|---:|---|---|---:|
| 1 | 1:0 | A | 0.045 |
| 1 | 1:0 | B | 0.068 |
| 1 | 1:0 | C | 0.071 |
| 98 | 1:0 | A | 2.91 |
| 98 | 1:0 | B | 6.54 |
| 98 | 1:0 | C | 5.25 |

## Calculation convention

For each strain:

```text
mean circularity = sum of its three Circularity observations / 3
```

The requested raw difference is directional:

```text
mean(Circularity | Strain 98, Ratio 1:0)
-
mean(Circularity | Strain 1, Ratio 1:0)
```

Do not standardize the difference, express it as a percentage, or substitute
the `Area` or `Round` measurement.
