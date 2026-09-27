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
| P396 | -4 |
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
