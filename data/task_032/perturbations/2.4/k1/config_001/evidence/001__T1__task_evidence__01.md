# Evidence for this task

## Endpoint construction and subgroup

All adverse-event records for a subject are reduced to that subject's maximum recorded `AESEV`; no event-type filter is applied. The endpoint is therefore maximum severity across all recorded adverse events and is not COVID-19-specific severity.

After joining subject-level adverse-event results to demographics/exposure information and removing incomplete merged records, 791 subjects remain. Their literal `patients_seen` distribution is:

| `patients_seen` category | Complete subjects |
|---|---:|
| `1-50` | 658 |
| `51-100` | 108 |
| `>100` | 25 |

Only the 25 subjects in the literal `>100` category are used below.

## Sparse treatment-by-severity table

| Maximum `AESEV` | BCG | Placebo | Row total |
|---:|---:|---:|---:|
| 1 | 6 | 3 | 9 |
| 2 | 10 | 4 | 14 |
| 3 | 0 | 1 | 1 |
| 4 | 1 | 0 | 1 |
| Column total | 17 | 8 | 25 |

The independence-model expectations are:

| Maximum `AESEV` | Expected BCG | Expected Placebo |
|---:|---:|---:|
| 1 | 6.12 | 2.88 |
| 2 | 9.52 | 4.48 |
| 3 | 0.68 | 0.32 |
| 4 | 0.68 | 0.32 |

The ordinary Pearson test uses

\[
df=(4-1)(2-1)=3,
\]

\[
X^2=2.6785714285714284,
\]

## Approximation warning

Six of the eight expected counts are below 5, and four are below 1. These severe expected-count violations make the large-sample chi-square approximation unreliable. The archived calculation does not replace it with an exact or Monte Carlo procedure, so any upper-tail value derived from the statistic must be reported as nominal rather than as reliable small-sample inference.

# High-contact participant safety reconciliation

**Source:** Independent Trial Disposition and Safety Linkage Group
**Cohort:** Complete randomized participants whose archived patient-volume category is `>100`
**Endpoint derivation:** Highest all-event severity after linkage of the adverse-event ledger to serious-event disposition forms
**Column order:** BCG, Placebo

| Reconciled maximum severity | BCG | Placebo |
|---:|---:|---:|
| 1 | 4 | 5 |
| 2 | 11 | 3 |
| 3 | 0 | 1 |
| 4 | 1 | 0 |

The reconciliation retains all 25 participants and all four severity levels. The prespecified summary is the uncorrected ordinary Pearson statistic and its nominal chi-square upper-tail probability; expected-count adequacy is assessed separately.
