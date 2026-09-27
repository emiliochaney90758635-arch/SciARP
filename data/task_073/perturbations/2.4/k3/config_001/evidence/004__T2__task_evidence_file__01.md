# Replicate-aware sample-retention audit

**Source:** Longitudinal Cohort Data Core, audit `LCDC-PROJID-222`
**Scope:** the same 222 metadata records and 2,456-gene expression table
**Method:** Repeated `projid` values were treated as longitudinal technical replicates. For each repeated ID, the first metadata row and base expression column were retained; only later rows and dot-suffixed columns were removed.

| Object | Reported retained dimensions |
|---|---:|
| metadata | 201 samples × 9 fields |
| expression matrix | 2,456 genes × 201 samples |

The audit reports identical sample-ID sets after this replicate-aware cleaning. This procedure is independent of, and conflicts with, the archived rule that removes every row and both base and suffixed expression columns for duplicated IDs.
