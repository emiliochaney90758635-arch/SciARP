# Longitudinal Reactome canonicalization extract

**Source:** Chronic Screen Integration Repository
**Data product:** Adjusted-significant Reactome records from three separately processed chronic-exposure rounds
**Method:** Each round was analyzed against the repository’s release-matched pathway catalogue. Release suffixes after `@` identify catalogue versions and are removed before canonical cross-round comparison.

| Chronic round | Significant release-specific pathway IDs |
|---:|---|
| 1 | `R-HSA-418457@2023-4`, `R-HSA-9006934@2023-4` |
| 2 | `R-HSA-392154@2024-1`, `R-HSA-418457@2024-1` |
| 3 | `R-HSA-418457@2024-3`, `R-HSA-9711123@2024-3` |

A pathway is considered shared only when its suffix-stripped canonical ID occurs in all three rows.
