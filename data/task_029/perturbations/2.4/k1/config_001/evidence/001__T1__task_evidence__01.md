# Evidence for this task

## Endpoint construction and cohort

The adverse-event table contains 2,694 records with fields including `STUDYID`, `TRTGRP`, `USUBJID`, `AESEV`, and `AEHS`. After retaining the relevant fields and removing duplicate selected rows, adverse-event severity is reduced to one value per subject:

\[
\text{subject severity}=\max(\texttt{AESEV})
\]

over all adverse-event records for that subject. No event-term filter is applied, so this endpoint is maximum severity across all recorded adverse events, not a COVID-specific event endpoint.

The demographics/exposure table contains 1,000 subjects and includes `USUBJID`, `patients_seen`, and `expect_interact`. Merging the subject-level severity with this table gives 1,000 subjects; 791 have complete values for the analysis variables. Among complete cases, `expect_interact = Yes` contains 506 subjects and `expect_interact = No` contains 285.

## `expect_interact = Yes` contingency table

Within the 506 healthcare workers who expected interaction, the four-level subject maximum severity by randomized treatment is:

| Maximum `AESEV` | BCG | Placebo | Row total |
|---:|---:|---:|---:|
| 1 | 106 | 119 | 225 |
| 2 | 145 | 97 | 242 |
| 3 | 17 | 10 | 27 |
| 4 | 8 | 4 | 12 |
| Column total | 276 | 230 | 506 |

For the ordinary Pearson chi-square test, compute

\[
E_{ij}=\frac{R_iC_j}{506},
\qquad
X^2=\sum_{i,j}\frac{(O_{ij}-E_{ij})^2}{E_{ij}},
\]

with

\[
df=(4-1)(2-1)=3,
\]

then evaluate the corresponding upper-tail probability and round it to four decimal places.

# Solicited-event adjudication table

**Source:** Trial Safety Adjudication Office
**Population:** Complete-case participants with `expect_interact = Yes`
**Method:** Each subject was assigned the maximum severity among protocol-solicited systemic events recorded within the adjudication window. Unsolicited and out-of-window records were excluded before subject reduction.

| Adjudicated maximum severity | BCG | Placebo |
|---:|---:|---:|
| 1 | 100 | 105 |
| 2 | 120 | 115 |
| 3 | 30 | 8 |
| 4 | 12 | 6 |

The office applies an ordinary Pearson test to this 4×2 table, using the table-derived margins and three degrees of freedom.
