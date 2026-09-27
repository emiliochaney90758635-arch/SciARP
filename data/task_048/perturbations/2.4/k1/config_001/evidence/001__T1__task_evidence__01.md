# Evidence for this task

## Cohort and statistical unit

The metadata contain 20 records labeled `BLM Mutation Status = Carrier`. Sample ID `533` has no matched per-sample variant workbook and is excluded rather than imputed as a zero. The 19 carriers with variant data are:

```text
P184, P185, P285, P287, P353, P354, P381, P396, P397,
P489, P490, P499, P500, P503, P504, P556, P557, P613, P614
```

The statistical unit for the requested summary is one carrier's count of retained sample–variant rows.

## Variant-row eligibility rule

Workbook fields used by the archived analysis are `Zygosity`, `Sequence Ontology (Combined)`, and `Variant Allele Freq`. For each included carrier:

```text
exclude Zygosity = Reference or missing Zygosity
exclude ontology exactly equal to:
  intron_variant
  intergenic_variant
  3_prime_UTR_variant
  5_prime_UTR_variant
retain Variant Allele Freq < 0.3
```

The VAF comparison is strict. These rows were called putative somatic CHIP variants operationally; no paired-normal confirmation was performed.

## Complete carrier-level retained-row counts

The table gives the number of sample–variant rows remaining after the complete rule above. A carrier with a workbook but no retained row remains in the table with count zero.

| Carrier | Retained rows |
|---|---:|
| P185 | 3 |
| P184 | 4 |
| P285 | 1 |
| P287 | 6 |
| P353 | 2 |
| P354 | 2 |
| P556 | 1 |
| P557 | 5 |
| P381 | 1 |
| P396 | 0 |
| P397 | 3 |
| P489 | 3 |
| P490 | 4 |
| P499 | 2 |
| P500 | 1 |
| P503 | 2 |
| P504 | 1 |
| P613 | 5 |
| P614 | 1 |

For an odd number of subjects, the median is the central observation after sorting all subject-level counts, including zero.

# UMI panel reconciliation summary

**Source:** Molecular Diagnostics Laboratory, reconciled call-set `MDL-BLM-UMI-R2`
**Scope:** Nineteen BLM-carrier libraries with callable depth above 250×
**Method:** Duplex-supported non-reference calls were annotated against the canonical transcript. Intronic, intergenic, 3′-UTR, and 5′-UTR consequences were removed before binning retained calls by allele fraction.

The three VAF-bin columns below are mutually exclusive. A subject's low-frequency burden is the row sum across the three columns.

| Subject | \(0\leq\mathrm{VAF}<0.10\) | \(0.10\leq\mathrm{VAF}<0.20\) | \(0.20\leq\mathrm{VAF}<0.30\) |
|---|---:|---:|---:|
| BLM-R01 | 1 | 1 | 0 |
| BLM-R02 | 1 | 1 | 1 |
| BLM-R03 | 0 | 1 | 0 |
| BLM-R04 | 2 | 1 | 1 |
| BLM-R05 | 1 | 1 | 1 |
| BLM-R06 | 0 | 2 | 1 |
| BLM-R07 | 1 | 0 | 1 |
| BLM-R08 | 2 | 2 | 1 |
| BLM-R09 | 1 | 1 | 1 |
| BLM-R10 | 0 | 0 | 0 |
| BLM-R11 | 1 | 2 | 0 |
| BLM-R12 | 2 | 1 | 0 |
| BLM-R13 | 1 | 2 | 1 |
| BLM-R14 | 1 | 1 | 0 |
| BLM-R15 | 0 | 1 | 1 |
| BLM-R16 | 1 | 1 | 1 |
| BLM-R17 | 1 | 1 | 1 |
| BLM-R18 | 2 | 2 | 1 |
| BLM-R19 | 0 | 1 | 1 |

The laboratory report summarises carriers at the subject level after these bin totals are calculated.
