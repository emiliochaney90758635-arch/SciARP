# Evidence for this task

## Endpoint, merge, and strata

The adverse-event table has 2,694 records. Severity is reduced to one observation per subject as the maximum `AESEV` over all that subject's adverse-event records, with no event-term filter. Thus the endpoint is maximum severity across all recorded adverse events, not a COVID-specific endpoint.

The reduction gives 1,000 subjects and is merged with a 1,000-subject demographics/exposure table. There are 209 missing severity values and 143 missing `AEHS` values in the source fields; restricting to complete analysis variables leaves 791 subjects.

The `patients_seen` strata and complete-case counts are:

| Stratum | Merged subjects | Excluded for missing analysis values | Complete cases |
|---|---:|---:|---:|
| 1–50 | 835 | 177 | 658 |
| 51–100 | 129 | 21 | 108 |
| >100 | 36 | 11 | 25 |

## Observed treatment-by-severity tables

### Patients seen: 1–50

| Maximum `AESEV` | BCG | Placebo | Row total |
|---:|---:|---:|---:|
| 1 | 135 | 136 | 271 |
| 2 | 200 | 136 | 336 |
| 3 | 27 | 11 | 38 |
| 4 | 7 | 6 | 13 |
| Column total | 369 | 289 | 658 |

### Patients seen: 51–100

| Maximum `AESEV` | BCG | Placebo | Row total |
|---:|---:|---:|---:|
| 1 | 19 | 29 | 48 |
| 2 | 29 | 23 | 52 |
| 3 | 1 | 3 | 4 |
| 4 | 2 | 2 | 4 |
| Column total | 51 | 57 | 108 |

### Patients seen: >100

| Maximum `AESEV` | BCG | Placebo | Row total |
|---:|---:|---:|---:|
| 1 | 6 | 3 | 9 |
| 2 | 10 | 4 | 14 |
| 3 | 0 | 1 | 1 |
| 4 | 1 | 0 | 1 |
| Column total | 17 | 8 | 25 |

## Separate ordinary Pearson tests

Each table is tested separately with an ordinary Pearson chi-square test:

| `patients_seen` stratum | \(X^2\) | df | Nominal p-value | Minimum expected count | Cells with expected <5 | Cells with expected <1 |
|---|---:|---:|---:|---:|---:|---:|
| 1–50 | 9.420743463606744 | 3 | 0.024189637931453605 | 5.7097 | 0/8 | 0/8 |
| 51–100 | 3.4529649916646816 | 3 | 0.32691383506649596 | 1.8889 | 4/8 | 0/8 |
| >100 | 2.6785714285714284 | 3 | 0.4438811470106675 | 0.3200 | 6/8 | 4/8 |

## Interpretation limits

Three separate tests were run without a multiplicity correction. If a Bonferroni sensitivity check is reported, compare three times the smallest nominal probability with 0.05. The 51–100 and especially the >100 table also have sparse expected cells, making the usual chi-square approximation weak. These issues, together with the all-adverse-event maximum-severity endpoint, should accompany any interpretation.
