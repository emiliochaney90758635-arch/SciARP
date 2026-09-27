# Single-molecule Jackdaw methylome density audit

## Source identity and scope

The Corvid Long-Read Epigenomics Consortium independently measured extreme-methylation CpG sites on a chromosome-scale Jackdaw assembly. Its report uses the same strict >90% or <10% site rule and summarizes only the twenty chromosomes with at least one retained site.

## Method

Nanopore modification calls were aggregated by exact physical coordinate, deduplicated across birds, divided by consortium chromosome spans, and then averaged with equal weight across the twenty represented chromosomes. Chromosome groups below are disjoint.

## Structured observations

| chromosome group | represented chromosomes | sum of per-chromosome densities (sites/bp) |
|---|---:|---:|
| macrochromosomes | 6 | 5.10e-7 |
| intermediate chromosomes | 7 | 7.70e-7 |
| microchromosomes | 5 | 1.12e-6 |
| sex chromosomes | 2 | 4.20e-7 |
| **total** | **20** | **2.82e-6** |

## Derived conflicting result

The consortium's equal-weight mean is `2.82e-6 / 20 = 1.41e-7` sites/bp. This single-molecule methylome object is independent of the prior repeat-masked four-class and external two-stratum coordinate-build audits. The requested internal twenty-row mean remains recoverable from its complete table.
