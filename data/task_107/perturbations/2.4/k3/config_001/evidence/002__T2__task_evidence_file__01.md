# mexG RT-qPCR validation worksheet

## Source and assay

The Microbial Gene Regulation Core measured mexG and the reference gene rpoD
in wild type strain #1 and ΔrhlI strain #97. Values are technical-replicate
mean threshold cycles from three biological replicates.

| Strain | Replicate | mexG Ct | rpoD Ct |
|---|---|---:|---:|
| wt #1 | A | 22.1 | 18.0 |
| wt #1 | B | 21.9 | 17.9 |
| wt #1 | C | 22.0 | 18.1 |
| ΔrhlI #97 | A | 22.8 | 18.0 |
| ΔrhlI #97 | B | 22.9 | 18.1 |
| ΔrhlI #97 | C | 22.7 | 17.9 |

For each replicate calculate `ΔCt = mexG Ct - rpoD Ct`, then average ΔCt by
strain. With equal amplification efficiencies,
`log2 fold change (ΔrhlI/wt) = -(mean ΔCt_ΔrhlI - mean ΔCt_wt)`.
