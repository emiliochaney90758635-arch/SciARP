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

# Strain-specific loss of circular morphology in monoculture biofilms

Joanne E. Mercer, Akira Fujimoto, Laila Benyoussef, and Carl Nyberg

## Abstract

Cellular contour provides a sensitive readout of strain-dependent growth
behavior in monoculture. We quantified segmented-object circularity for
Strains 1 and 98 grown under identical single-strain conditions, using
replicate-level image masks and a prespecified perimeter correction. Strain 98
produced markedly less circular objects than Strain 1, and the mean difference
computed as Strain 98 minus Strain 1 was negative across bootstrap resamples.
The morphology of Strain 98 is therefore characterized by increased
elongation rather than the higher circularity inferred from uncorrected image
features.
