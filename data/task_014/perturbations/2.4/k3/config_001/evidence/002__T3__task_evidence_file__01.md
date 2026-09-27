# Round-2 ORA multiple-testing ledger

**Source:** Pathway Statistics Operations Unit
**Input:** Mapped chronic round-2 candidate symbols and the measured-symbol background
**Method:** Duplicate pathway definitions were consolidated before raw enrichment probabilities were ordered. The ledger contains 2,725 tested canonical pathways and applies the Benjamini–Hochberg monotone adjustment.

## Ledger entries for the two leading pathways

| Reactome pathway | Raw enrichment probability | Rank in ordered family | Smallest adjusted candidate at any later rank |
|---|---:|---:|---:|
| Nitric oxide stimulates guanylate cyclase | 0.000033 | 3 | 0.030100 |
| cGMP effects | 0.000024 | 2 | 0.031500 |

At each row, the rank candidate is the raw probability multiplied by \(2{,}725/rank\). The adjusted value is the smaller of the rank candidate and the supplied later-rank candidate.
