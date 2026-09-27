# Evidence for this task

## Subject-level endpoint and eligible subgroup

The adverse-event table contains 2,694 event records with fields including `STUDYID`, `TRTGRP`, `USUBJID`, `AESEV`, and `AEHS`. After duplicate selected rows are removed, records are grouped by `USUBJID` and the maximum recorded `AESEV` is taken for each subject.

No `AEPT` or other event-type filter is applied before aggregation. The endpoint is therefore maximum severity across all recorded adverse events, not COVID-19-specific severity.

The subject-level result is joined to a 1,000-subject demographics table containing `USUBJID`, `patients_seen`, and `expect_interact`, and incomplete merged records are removed. This gives 791 complete subjects:

| Literal `patients_seen` value | Complete subjects |
|---|---:|
| `1-50` | 658 |
| `51-100` | 108 |
| `>100` | 25 |

Only the literal `1-50` category is used here.

## Observed and independence-model frequencies

The subject-level four-severity-by-two-treatment table is:

| Maximum `AESEV` | BCG | Placebo | Row total |
|---:|---:|---:|---:|
| 1 | 135 | 136 | 271 |
| 2 | 200 | 136 | 336 |
| 3 | 27 | 11 | 38 |
| 4 | 7 | 6 | 13 |
| Column total | 369 | 289 | 658 |

With \(E_{ij}=R_iC_j/658\), the expected counts are:

| Maximum `AESEV` | Expected BCG | Expected Placebo |
|---:|---:|---:|
| 1 | 151.97416413 | 119.02583587 |
| 2 | 188.42553191 | 147.57446809 |
| 3 | 21.31003040 | 16.68996960 |
| 4 | 7.29027356 | 5.70972644 |

All eight expected counts exceed 5. The ordinary Pearson calculation uses

\[
X^2=\sum_{i,j}\frac{(O_{ij}-E_{ij})^2}{E_{ij}},
\qquad
df=(4-1)(2-1)=3.
\]

For this table, the archived Pearson statistic is \(X^2=9.420743463606744\). Evaluate \(P(\chi^2_3\ge X^2)\) and round the result to four decimal places.

# Maximum Adverse-Event Severity Among Low-Contact Healthcare Workers After BCG Vaccination

**Authors:** Elise Martens, Rafael Cuervo, Nadia Iqbal, and Tomás H. Veenstra

**Abstract**

**Background:** Whether bacillus Calmette–Guérin (BCG) vaccination alters the overall adverse-event experience of healthcare workers with relatively limited patient contact remains uncertain. **Methods:** We analyzed complete participant records from a randomized BCG-versus-placebo healthcare-worker cohort. Participants assigned to the recorded 1–50 patients-seen category were reduced to one observation per person using the highest severity grade among all reported adverse events. The resulting four-level severity distribution was compared between treatment groups using an ordinary Pearson chi-square test. **Results:** The treatment-specific severity profiles were closely aligned, and the omnibus test did not support an association between assignment and maximum adverse-event severity (\(p=0.312\)). Sensitivity analyses retaining duplicate event entries produced the same qualitative conclusion. **Conclusions:** Among healthcare workers in the 1–50 patient-contact category, BCG assignment was not associated with the maximum severity of recorded adverse events.
