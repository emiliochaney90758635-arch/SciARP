# Independent Jackdaw chromosome-stratum audit

## Source identity and scope

The Independent Jackdaw Chromosome-Stratum Audit reports the same mean-density
estimand over twenty chromosome categories, using an external coordinate
build rather than the requested internal table.

## Method

The audit grouped the twenty chromosomes into two disjoint strata, summed the
within-chromosome densities in each stratum, added the two stratum sums, and
divided by twenty.

## Structured observations

| stratum | represented chromosomes | sum of chromosome densities |
|---|---:|---:|
| autosomes | 18 | 1.98e-6 |
| sex chromosomes | 2 | 4.90e-7 |

## Derived conflicting result

The external result is `(1.98e-6 + 4.90e-7) / 20 = 1.235e-7`. It conflicts
with the requested internal twenty-row mean but remains attributable to the
independent coordinate build.
