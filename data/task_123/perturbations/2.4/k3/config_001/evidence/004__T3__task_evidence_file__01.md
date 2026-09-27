# Independent methylation-intensity recalibration audit

## Source identity and scope

The Avian Bisulfite Quantification Core reprocessed the raw methylated and
unmethylated read counts for the same Zebra Finch samples and the same 1,140
distinct genomic Pos values represented by the 19,698 sample-by-CpG records.

## Independent measurement method

Instead of accepting the stored MethylationPercentage field, the core corrected
read counts for sample-specific bisulfite-conversion efficiency, recalculated
`100 * methylated / (methylated + unmethylated)`, and then applied the same
strict record-level rule: less than 10 percent or greater than 90 percent. A
site was retained if at least one corrected sample record passed. Coordinate
partitions below are disjoint.

| Coordinate partition | Distinct sites before | Retained after recalibration |
|---|---:|---:|
| chromosomes 1-5 | 452 | 115 |
| chromosomes 6-15 | 321 | 85 |
| chromosomes 16-28 | 210 | 50 |
| sex chromosomes and unplaced | 157 | 29 |

## Derived conflicting result

The partitions sum to 1,140 prefilter sites and 279 retained sites, implying
861 removed sites. This audit changes the measurement acquisition for
methylation percentage; it is distinct from E1's coordinate normalization and
E2's assembly-set intersection. The archived task uses the stored
MethylationPercentage field and its directly enumerated retained Pos set.
