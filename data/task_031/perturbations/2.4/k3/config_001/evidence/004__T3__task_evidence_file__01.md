# Hospital-encounter severity reconstruction

## Source identity and scope

The Independent Clinical Utilization Linkage Laboratory linked emergency,
outpatient, and inpatient encounter records for the same 658 complete trial
participants carrying the archived literal `1-50` patient-volume label.
Treatment identity was decoded only after the encounter review was frozen.

## Independent endpoint and method

For each participant, the laboratory assigned the maximum utilization severity
observed across all linked encounters: telephone-only management (1),
unscheduled clinic care (2), emergency-department care (3), or inpatient
admission (4). This is a health-care-utilization endpoint derived from encounter
disposition; it is not the maximum recorded `AESEV`, the clinical-adjudication
endpoint, or the symptom-diary endpoint.

| Utilization maximum | BCG | Placebo |
|---:|---:|---:|
| 1 | 126 | 145 |
| 2 | 207 | 126 |
| 3 | 27 | 14 |
| 4 | 9 | 4 |

## Derived conflicting result

The rows total 658 participants. An ordinary Pearson independence test on this
complete 4-by-2 table gives chi-square approximately 17.6138 on 3 degrees of
freedom and a two-sided p-value approximately 0.00052835. The report recommends
this encounter-derived result for safety surveillance, although the archived
task asks specifically for the maximum recorded `AESEV` analysis.
