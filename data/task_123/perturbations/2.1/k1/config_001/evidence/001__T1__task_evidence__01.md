# Zebra Finch methylation-site filtering evidence

## Record structure and threshold

The Zebra Finch CpG table has the fields:

```text
Pos, SampleShared, Sample, SampleL, Chromosome, StartPosition,
EndPosition, MethylationPercentage, CountMethylated,
CountNonMethylated, Coverage, Dage
```

It contains 19,698 sample-by-CpG records. `MethylationPercentage` is complete and ranges from 0 to 100. The same genomic `Pos` may occur in records from multiple samples.

The record-level selection is:

```r
MethylationPercentage > 90 | MethylationPercentage < 10
```

The inequalities are strict. The complete threshold partition is:

| methylation-percentage category | records | retained |
|---|---:|---|
| `< 10` | 271 | yes |
| `> 90` | 268 | yes |
| `= 10` | 8 | no |
| `= 90` | 13 | no |
| `10 < value < 90` | 19,138 | no |
| total | 19,698 | — |

The two retained branches are mutually exclusive, yielding 539 retained sample-by-CpG records.

## Cross-sample site unit

Genomic sites are combined across samples by exact `Pos`:

```r
n_distinct(Pos)
```

| counting unit | before selection | retained after strict selection |
|---|---:|---:|
| sample-by-CpG records | 19,698 | 539 |
| distinct genomic `Pos` values | 1,140 | 291 |

A distinct site is retained if at least one of its sample records passes the strict threshold. Removed-site counts therefore use the set difference between the distinct-`Pos` populations, not the difference between record counts.

# CpG position-identifier note

Each `Pos` value is sample-specific; identical chromosome coordinates observed
in two samples represent two distinct genomic CpG sites.
