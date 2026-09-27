# Evidence for this task

## Comparison groups and measurement structure

The reference group is `StrainNumber = 1, Ratio = 1:0`. Candidate groups are
only the 12 two-strain cultures with `StrainNumber = 287_98`; the single-strain
98 and 287 groups are not candidates. Each group has three observations ordered
as replicates A, B, and C.

`Ratio` is an ordered culture-mixture label in the Strain 287 : Strain 98
direction. It is not arithmetic division and must be retained verbatim.

| Group | Ratio | Area (A / B / C) | Circularity (A / B / C) |
|---|---|---|---|
| Strain 1 reference | 1:0 | 152138 / 93040 / 90701 | 0.045 / 0.068 / 0.071 |
| 287_98 | 1:3 | 17327 / 19749 / 19206 | 0.668 / 0.591 / 0.562 |
| 287_98 | 1:2 | 29886 / 26359 / 24189 | 0.324 / 0.389 / 0.454 |
| 287_98 | 1:1 | 32388 / 47048 / 50235 | 0.211 / 0.197 / 0.183 |
| 287_98 | 2:1 | 62165 / 67375 / 131630 | 0.130 / 0.101 / 0.058 |
| 287_98 | 3:1 | 96584 / 76362 / 94430 | 0.086 / 0.086 / 0.085 |
| 287_98 | 4:1 | 137316 / 130242 / 189336 | 0.061 / 0.065 / 0.039 |
| 287_98 | 5:1 | 127082 / 122640 / 104537 | 0.058 / 0.069 / 0.073 |
| 287_98 | 10:1 | 129141 / 185482 / 238479 | 0.055 / 0.038 / 0.034 |
| 287_98 | 50:1 | 92265 / 116187 / 73305 | 0.093 / 0.066 / 0.126 |
| 287_98 | 100:1 | 85812 / 85686 / 51863 | 0.095 / 0.095 / 0.144 |
| 287_98 | 500:1 | 10623 / 9175 / 10341 | 0.747 / 0.856 / 0.853 |
| 287_98 | 1000:1 | 14736 / 73579 / 47991 | 0.634 / 0.107 / 0.166 |

All displayed observations are nonmissing; there are no duplicate group ×
replicate rows.

## Similarity rule

First compute the arithmetic `Mean Area` and `Mean Circularity` separately for
the reference and each candidate. For each ratio \(r\), compare:

```text
ΔArea(r) = |MeanArea(287_98, r) - MeanArea(Strain 1, 1:0)|
ΔCirc(r) = |MeanCircularity(287_98, r) - MeanCircularity(Strain 1, 1:0)|
```

Area and circularity have different scales, so do not add them into an
unweighted composite distance. Determine whether one candidate uniquely
minimizes both columns. Carry full precision through the comparison; premature
rounding of mean circularity can create a false tie.

No significance threshold, Dunnett p-value, standard deviation, or standard
error is used for this mean-similarity task.

# Co-culture ratio metadata

For `StrainNumber = 287_98`, the two positions in every `Ratio` label are
ordered as Strain 98 followed by Strain 287.
