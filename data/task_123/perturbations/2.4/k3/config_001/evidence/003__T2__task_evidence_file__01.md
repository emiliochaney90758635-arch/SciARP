# Independent Zebra Finch site-set intersection audit

## Source identity, scope, and method

The Comparative Methylome Archive independently lifted all coordinates to the
current assembly, intersected the exact `Pos` sets before and after applying
the strict extreme-methylation record filter, and deduplicated across samples.
The audit used four disjoint coordinate partitions.

| Coordinate partition | Distinct sites before | Distinct sites retained |
|---|---:|---:|
| chr1–chr4 | 401 | 121 |
| chr5–chr12 | 329 | 96 |
| chr13–chr28 | 237 | 61 |
| sex chromosomes and unplaced | 173 | 37 |

The removed-site count is the sum of the first numeric column minus the sum
of the second numeric column.
