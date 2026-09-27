# Evidence for this task

## Cohort and count definition

The metadata contain 30 records with BLM mutation status `Affected` or
`Carrier`. Sample `P533` has no matching variant workbook and is excluded,
leaving 29 analyzable patients.

For each patient, count rows satisfying only:

```text
Zygosity != "Reference"
```

Do not add the later exonic-consequence exclusions or the `VAF < 0.3` filter;
they define different subsets.

## Patient-level metadata and non-reference counts

| Sample ID | BLM mutation status | Age | Non-reference variant calls |
|---|---|---:|---:|
| P179 | Affected | 8.1 | 138 |
| P185 | Carrier | 37.0 | 127 |
| P184 | Carrier | 31.7 | 145 |
| P286 | Affected | 1.9 | 147 |
| P285 | Carrier | 30.9 | 144 |
| P287 | Carrier | 28.4 | 128 |
| P360 | Affected | 0.8 | 109 |
| P353 | Carrier | 33.2 | 131 |
| P354 | Carrier | 24.1 | 108 |
| P364 | Affected | 36.3 | 137 |
| P556 | Carrier | 64.55 | 133 |
| P557 | Carrier | 62.6 | 149 |
| P380 | Affected | 4.3 | 133 |
| P381 | Carrier | 33.5 | 133 |
| P409 | Affected | 2.6 | 119 |
| P396 | Carrier | 24.7 | 135 |
| P397 | Carrier | 23.4 | 120 |
| P488 | Affected | 1.8 | 123 |
| P489 | Carrier | 29.0 | 150 |
| P490 | Carrier | 30.1 | 119 |
| P498 | Affected | 5.8 | 157 |
| P499 | Carrier | 30.6 | 142 |
| P500 | Carrier | 35.0 | 161 |
| P502 | Affected | 26.6 | 116 |
| P503 | Carrier | 45.9 | 118 |
| P504 | Carrier | 45.3 | 126 |
| P615 | Affected | 2.0 | 148 |
| P613 | Carrier | 27.2 | 165 |
| P614 | Carrier | 23.3 | 123 |

Select the patient with the largest count, then read the age from the same
row. Treat the rows as patient-level records, not variant-level observations.

# Variant-workbook QC registry: high-burden shortlist

## Source and scope

The Clinical Sequencing QC Registry screened all 29 affected/carrier
workbooks. The five rows below were the only patients with more than 150
non-reference calls in the registry build; all other analyzable patients had
150 or fewer.

| Patient | Age | Total variant rows | Rows called Reference |
|---|---:|---:|---:|
| P489 | 29.0 | 650 | 490 |
| P498 | 5.8 | 640 | 480 |
| P500 | 35.0 | 650 | 470 |
| P557 | 62.6 | 660 | 500 |
| P613 | 27.2 | 670 | 500 |

For each patient, subtract Reference rows from total variant rows. Select the
largest remainder and read age from the same row.
