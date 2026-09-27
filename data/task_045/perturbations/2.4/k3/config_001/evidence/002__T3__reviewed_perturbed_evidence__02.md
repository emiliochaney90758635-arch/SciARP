# Evidence for this task

## Matrix alignment

| Matrix | Cell lines | Complete gene labels | Meaning |
|---|---:|---:|---|
| CRISPR gene effect | 1,178 | 17,916 | Chronos gene-effect; lower values indicate stronger dependency |
| Expression | 1,673 | 19,138 | Batch-corrected `log2(TPM+1)` |

Alignment uses exact DepMap `ACH-...` cell-line IDs and exact complete `symbol (ID)` gene-column labels. Neither matrix has duplicate row IDs or duplicate complete gene labels. The intersections contain:

| Shared dimension | Count |
|---|---:|
| Cell lines | 1,103 |
| Gene labels | 17,676 |

`Model.csv` is not used for filtering.

For each shared gene, missing values are removed separately from both matrices and common nonmissing cell lines are then aligned. The minimum valid pair count is 283, so all 17,676 genes exceed the required \(n>10\) threshold. All resulting correlations and raw p-values are finite.

## Correlation and multiple-testing convention

For every gene:

\[
\rho=\operatorname{Spearman}
\left(
\text{expression},
-\text{Chronos gene effect}
\right),
\]

using a two-sided p-value. Negating gene effect makes larger values correspond to stronger essentiality; it reverses the sign of \(\rho\) but does not alter the two-sided p-value.

Benjamini-Hochberg correction is applied once across all 17,676 tested p-values. The decision boundary is:

| Raw-p rank | Gene label | \(\rho\) | Raw p | BH critical value | BH-adjusted p |
|---:|---|---:|---:|---:|---:|
| 3,853 | `TFB2M (64216)` | 0.076649571 | 0.0108808126 | 0.0108989590 | 0.0499167516 |
| 3,854 | `TIRAP (114609)` | 0.076631499 | 0.0108995998 | 0.0109017877 | 0.0499899654 |
| 3,855 | `RNGTT (8732)` | 0.076618388 | 0.0109132476 | 0.0109046164 | 0.0500395759 |
| 3,856 | `MPZL3 (196264)` | 0.076613301 | 0.0109185469 | 0.0109074451 | 0.0500508907 |

Because sorted BH-adjusted values are nondecreasing, use the last boundary-table rank whose adjusted value remains below 0.05 as the significant-gene numerator. Divide that rank by the full tested-gene count and round the directly computed combined percentage, rather than adding separately rounded directional percentages.

## Staged modified_2x evidence at T1

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.

## Staged modified_2x evidence at T3

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
