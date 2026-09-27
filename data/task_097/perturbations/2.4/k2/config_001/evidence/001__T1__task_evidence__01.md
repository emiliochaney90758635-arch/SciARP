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
| 98 | 1:0 | A | 0.291 |
| 98 | 1:0 | B | 0.654 |
| 98 | 1:0 | C | 0.525 |

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

# Independent contour-geometry export

## Source and acquisition

The Imaging Core resegmented three monoculture fields per strain with a
boundary-smoothing pipeline. For each replicate, the table records object area
and perimeter in matched pixel units.

| StrainNumber | Replicate | Area (px²) | Perimeter (px) |
|---:|---|---:|---:|
| 1 | A | 184 | 87.0 |
| 1 | B | 207 | 88.5 |
| 1 | C | 196 | 86.8 |
| 98 | A | 177 | 108.0 |
| 98 | B | 215 | 112.4 |
| 98 | C | 203 | 110.7 |

## Calculation

For each replicate, calculate circularity as \(4\pi A/P^2\). Average the three
replicate circularities within strain, then report the Strain 98 mean minus
the Strain 1 mean.
