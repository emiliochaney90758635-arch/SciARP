# RefSeq accession reconciliation audit

**Source:** Genome Screening Data Harmonization Center
**Object:** Acute T-cell S1 and S2 MAGeCK probability columns
**Method:** Versioned and retired RefSeq accessions were remapped to current transcript records. When several archived accessions mapped to one current record, the smallest probability was retained per replicate before average ranks were assigned.

## Reconciled rank sufficient statistics

| Quantity | Audit value |
|---|---:|
| Matched current transcript records | 23,104 |
| Mean rank in each replicate | 11,552.5 |
| Centered rank cross-product | -76,842,000,000.0 |
| S1 centered rank square sum | 1,028,400,000,000.0 |
| S2 centered rank square sum | 1,011,600,000,000.0 |

The audit coefficient is the centered cross-product divided by the square root of the two centered rank square sums.
