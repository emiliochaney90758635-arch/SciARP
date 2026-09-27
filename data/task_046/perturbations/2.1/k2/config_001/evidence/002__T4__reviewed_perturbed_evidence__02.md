# Evidence for this task

## Analysis population and correlation direction

| Matrix | Cell lines | Gene columns |
|---|---:|---:|
| CRISPR Chronos gene effect | 1,178 | 17,916 |
| Batch-corrected `log2(TPM+1)` expression | 1,673 | 19,138 |

Exact complete cell-line IDs and complete `symbol (ID)` gene labels are intersected, producing 1,103 shared cell lines and 17,676 shared gene columns. For each gene, missing values are removed independently and common nonmissing cell lines are aligned. All 17,676 genes have more than 10 pairs; the minimum is 283.

Chronos gene effect is inverted before correlation:

\[
\rho=\operatorname{Spearman}
\left(
\text{expression},
-\text{gene effect}
\right).
\]

Thus positive \(\rho\) means that higher expression is associated with higher inverted essentiality. No BH/FDR condition is part of the requested threshold.

## Descending correlation boundary

The five largest coefficients among all 17,676 genes are:

| Rank | Complete gene label | Paired cell lines | Spearman \(\rho\) |
|---:|---|---:|---:|
| 1 | `CCND1 (595)` | 1,103 | 0.6288254699 |
| 2 | `FERMT2 (10979)` | 1,103 | 0.6123062053 |
| 3 | `KLF5 (688)` | 1,103 | 0.6020083868 |
| 4 | `WWTR1 (25937)` | 1,103 | 0.5595994040 |
| 5 | `ZEB2 (9839)` | 1,103 | 0.5220959205 |

The table is ordered over all tested genes; apply the inclusive coefficient threshold specified in the task to these ordered native values.

## Staged modified_2x evidence at T1

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.

## Staged modified_2x evidence at T4

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
