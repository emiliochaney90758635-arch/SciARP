# Stable-gene membership export

**Source:** Mouse Brain Transcriptome Harmonization Facility
**Inputs:** The three filtered dentate-gyrus contrast tables
**Method:** Archived GeneIDs were reconciled to current stable mouse loci before set membership was encoded. Each three-character pattern below records membership in A, B, and C respectively (`1` = member, `0` = absent).

| Membership pattern | Stable loci |
|---|---:|
| `100` | 11 |
| `010` | 108 |
| `001` | 31 |
| `110` | 9 |
| `101` | 4 |
| `011` | 18 |
| `111` | 3 |

Pairwise-only counts correspond to patterns with exactly two `1` values; the three-way count is pattern `111`.
