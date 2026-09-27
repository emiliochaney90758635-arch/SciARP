# Canonical-library ORA verification batch

**Source:** Immunogenomics Pathway QC Service
**Conditions:** Acute T cells and chronic rounds 1–3; no-T-cell controls excluded
**Method:** Candidate symbols were tested once against a deduplicated Reactome library. For the strongest pathway in each condition, the table records its raw probability, BH rank multiplier, and the smallest candidate at any later rank.

| Condition | Best raw probability | BH multiplier \(m/r\) | Smallest later candidate |
|---|---:|---:|---:|
| acute T cells | 0.000020 | 1,000 | 0.024 |
| chronic round 1 | 0.000100 | 600 | 0.066 |
| chronic round 2 | 0.000030 | 1,000 | 0.036 |
| chronic round 3 | 0.000080 | 800 | 0.071 |

For each condition, its smallest adjusted value is the lesser of `raw probability × multiplier` and the later candidate. A condition is pathway-positive when that derived value is below 0.05.
