# Transcript-accession consolidation table

**Source:** Urothelial RNA Modification Statistics Core
**Input:** Bladder-cancer m6A and DEG result records
**Method:** Duplicate instances of the same ENST accession were consolidated before cross-classification. When duplicated rows disagreed, the pair of labels from the row with the smallest m6A probability was retained.

| Consolidated m6A status | Down | Up | no-DEGs |
|---|---:|---:|---:|
| m6A Hyper | 15 | 82 | 480 |
| m6A Hypo | 96 | 14 | 330 |
| m6A no sig | 250 | 390 | 9,000 |

The core uses each consolidated transcript as an observational unit and computes the ordinary 3×3 Pearson statistic from this table without a continuity correction.
