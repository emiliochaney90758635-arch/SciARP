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

# Limited loss of Zebra Finch CpG loci under extreme-methylation retention

Leonie Hartwig, Amir Rahimi, Kaori Fujita, and Samuel P. Dobson

## Abstract

Extreme methylation states can be used to reduce a multisample CpG catalog
while preserving loci with strong biological polarization. We retained Zebra
Finch records above 90% or below 10% methylation, merged genomic coordinates
across samples, and compared the distinct-site sets before and after
filtering. The procedure removed 601 distinct CpG sites, leaving a larger
extreme-methylation locus set than expected from record-level attrition. These
results show that cross-sample recurrence preserves many genomic positions
even when most sample-specific measurements fall within the intermediate
methylation range.
