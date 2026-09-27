# Evidence for this task

## Paired acute-screen p-values

The table is keyed by `RefSeq ID`. The two target columns are `Acute Tcells S1` and `Acute Tcells S2`; values on the same row form one replicate pair.

| RefSeq ID | Acute Tcells S1 | Acute Tcells S2 |
|---|---:|---:|
| NM_130786 | 0.69139 | 0.44325 |
| NM_014576 | 0.19823 | 0.44005 |
| NM_000014 | 0.54829 | 0.36919 |
| NM_001282424 | 0.14469 | 0.76956 |
| NM_144670 | 0.84643 | 0.047154 |
| NM_001080438 | 0.85947 | 0.77624 |
| NM_017436 | 0.35363 | 0.58080 |
| NM_016161 | 0.50956 | 0.14728 |

The complete paired columns have:

| Integrity check | Count |
|---|---:|
| Data rows | 23,726 |
| Valid finite S1/S2 pairs | 23,726 |
| Missing S1 values | 0 |
| Missing S2 values | 0 |
| Non-finite values | 0 |
| Duplicate RefSeq IDs | 0 |

Rows remain paired by `RefSeq ID`; the two p-value columns must not be sorted independently.

## Rank convention and sufficient statistics

Spearman correlation is the Pearson correlation of the two rank vectors. Equal p-values receive their average rank.

| Tie property | S1 | S2 |
|---|---:|---:|
| Tied-value groups | 986 | 982 |
| Observations belonging to tied groups | 1,989 | 1,988 |
| Largest tied group | 3 | 4 |

Let the average-rank vectors be \(R_1\) and \(R_2\). From all 23,726 pairs:

| Quantity | Value |
|---|---:|
| \(\operatorname{mean}(R_1)\) | 11,863.5 |
| \(\operatorname{mean}(R_2)\) | 11,863.5 |
| \(\sum (R_1-\bar R_1)(R_2-\bar R_2)\) | 24,046,183,543.5 |
| \(\sum (R_1-\bar R_1)^2\) | 1,112,992,739,269.0 |
| \(\sum (R_2-\bar R_2)^2\) | 1,112,992,739,259.0 |

The coefficient is computed as:

\[
\rho_s=
\frac{\sum (R_1-\bar R_1)(R_2-\bar R_2)}
{\sqrt{\left[\sum(R_1-\bar R_1)^2\right]
\left[\sum(R_2-\bar R_2)^2\right]}}.
\]

# Reproducibility of acute T-cell phenotypes in genome-scale CRISPR activation screening

Noémie Laurent, Arjun B. Shah, Ines Vuković, and Peter K. Dunn

## Abstract

Replicate concordance is essential for interpreting pooled activation screens in primary immune-cell models. We evaluated two acute T-cell replicates from a genome-wide CRISPR activation experiment by pairing MAGeCK gene-level probabilities on RefSeq accession and retaining all finite matched entries. Because probability distributions were strongly non-Gaussian and contained repeated values, replicate agreement was quantified using average-rank Spearman correlation. Acute replicate ranks showed a moderate inverse association (\(\rho=-0.41\)), indicating that genes with stronger evidence in one replicate frequently had weaker evidence in the other. Concordance improved after excluding low-guide-coverage transcripts but remained negative. These findings reveal substantial rank instability in the acute T-cell arm and caution against interpreting replicate-specific MAGeCK extremes without joint modeling.
