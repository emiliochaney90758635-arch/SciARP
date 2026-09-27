# Specimen-accession reconciliation ledger

**Source:** Translational Data Stewardship Office, archived accession crosswalk
`ASXL1-BLD-R2`

**Scope:** Count-matrix libraries and phenotype records for the supplied
ASXL1/control blood comparison

**Acquisition method:** Count-column identifiers were matched to the phenotype
registry. Libraries without a current phenotype row were assigned the cohort's
fallback control code before the modeling roster was exported.

## Reconciliation output

| Reconciliation component | Number of libraries |
|---|---:|
| Count-matrix columns | 21 |
| Direct phenotype-record matches | 19 |
| Count libraries lacking a current phenotype row | 2 |
| Unmatched libraries carried by the fallback rule | 2 |

## Derived conflicting result

The ledger's exported modeling total is `19 + 2 = 21`. This conflicts with the
requested 19-sample phenotype-matched cohort. The two fallback accessions are
`MGD1640B` and `MGD1641B`.
