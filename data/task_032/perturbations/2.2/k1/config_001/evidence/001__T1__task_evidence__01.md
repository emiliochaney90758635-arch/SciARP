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

# Treatment Assignment and Maximum Adverse-Event Severity in Highly Exposed Healthcare Workers

**Authors:** Marit J. Koster, Denis A. Nwosu, Helen G. Park, and João B. Serrano

**Abstract**

**Background:** Safety signals among healthcare workers with the highest patient-contact burden may be obscured in analyses of an entire vaccination cohort. **Methods:** Complete records from a randomized BCG-versus-placebo study were restricted to participants in the recorded greater-than-100 patients-seen category. All adverse-event types were retained, and each participant contributed the maximum recorded severity grade. A four-level severity-by-treatment table was assessed with an uncorrected ordinary Pearson chi-square test. **Results:** Treatment assignment was associated with maximum adverse-event severity, with a nominal asymptotic \(p\)-value of 0.041. The pattern reflected an excess of the two highest grades in the BCG arm. **Conclusions:** In the highest-contact subgroup, the maximum severity distribution differed between BCG and placebo recipients, although confirmation in a larger high-exposure sample is warranted.
