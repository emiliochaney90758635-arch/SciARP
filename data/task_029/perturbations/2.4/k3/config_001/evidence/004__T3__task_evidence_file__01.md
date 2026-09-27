# Blinded all-event clinical-severity adjudication register

**Source:** Independent Trial Data Monitoring Committee, adjudication export
`DMC-AESEV-ALL-029`

**Scope:** The same 506 complete-case participants with
`expect_interact = Yes`, retaining all recorded adverse-event narratives
without a solicited-window, event-term, or serious-event restriction.

**Method:** Two blinded clinicians reviewed every participant's complete set of
event narratives and assigned one consensus worst clinical grade. The result
was crossed with randomized BCG versus Placebo and tested with an ordinary
4-by-2 Pearson chi-square test. The adjudicated clinical grade is distinct
from the maximum stored `AESEV` code requested by the task.

## Adjudicated participant table

| Consensus worst grade | BCG | Placebo | Row total |
|---:|---:|---:|---:|
| 1 | 115 | 100 | 215 |
| 2 | 132 | 110 | 242 |
| 3 | 20 | 15 | 35 |
| 4 | 9 | 5 | 14 |
| Column total | 276 | 230 | 506 |

The table gives `chi-square = 0.7278516`, `df = 3`, and
`p = 0.8666342`. This conflicts with the p-value from the raw recorded-AESEV
maximum table while preserving the same participants and all-event scope.
