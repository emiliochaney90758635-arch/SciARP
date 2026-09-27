# Current-annotation transcript reconciliation

**Source:** Urothelial Epitranscriptome Data Coordination Center
**Input:** The 617 unique ENST accessions among rows labeled `m6A Hyper`
**Method:** Archived transcript accessions were remapped to the center’s current Ensembl gene registry. Many-to-one transcript mappings reduce the number of current loci, whereas retired accessions that now resolve to two loci add one extra locus each.

| Reconciliation component | Count |
|---|---:|
| Unique archived ENST accessions | 617 |
| Redundant transcript-to-gene mappings removed | 349 |
| Retired accessions resolving to a second locus | 8 |

The center’s current-locus total is calculated as the archived transcript count minus redundant mappings plus added split loci.
