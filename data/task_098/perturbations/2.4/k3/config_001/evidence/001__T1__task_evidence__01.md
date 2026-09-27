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

# Cross-platform swarm morphology summary

## Source

The Automated Colony Phenotyping Facility analyzed an independent plate series
with illumination correction and size calibration. Values are group means
normalized to the contemporaneous Strain 1 mean, which equals 1.00 for each
trait.

| 287:98 ratio | Relative mean area | Relative mean circularity |
|---|---:|---:|
| 1:3 | 0.16 | 8.90 |
| 1:2 | 0.24 | 6.20 |
| 1:1 | 0.42 | 3.10 |
| 2:1 | 0.74 | 1.35 |
| 3:1 | 0.97 | 1.04 |
| 4:1 | 1.31 | 0.82 |
| 5:1 | 1.18 | 0.91 |
| 10:1 | 1.52 | 0.69 |
| 50:1 | 0.81 | 1.52 |
| 100:1 | 0.65 | 1.71 |
| 500:1 | 0.09 | 11.80 |
| 1000:1 | 0.43 | 4.60 |

For each candidate, take the absolute departure of each normalized trait from
1.00. A joint match requires the same candidate to have the smallest
departure in both columns; do not sum the two departures.
