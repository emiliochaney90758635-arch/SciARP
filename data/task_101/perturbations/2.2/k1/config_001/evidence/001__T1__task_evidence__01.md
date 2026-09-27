# Evidence for this task

## Analysis population

The RNA-expression table has 20,502 gene rows and 328 numeric sample columns.
The only nonnumeric column is `GeneSymbol`. The archived distribution analysis
selected all numeric columns and flattened them without deduplicating repeated
gene symbols and without log or z-score transformation.

| Population audit | Value |
|---|---:|
| Raw numeric values (`20,502 × 328`) | 6,724,656 |
| Missing or infinite values | 0 |
| Negative values | 0 |
| Values equal to zero | 1,025,144 |

## Distribution evidence

| Statistic | Raw-expression value |
|---|---:|
| Minimum | 0 |
| 25th percentile | 3.7426 |
| Median | 176.78945 |
| Mean | 931.9551175026498 |
| 75th percentile | 818.5191 |
| 90th percentile | 2,028.2709 |
| 95th percentile | 3,450.17325 |
| 99th percentile | 10,879.190415000005 |
| 99.9th percentile | 45,776.28723399895 |
| Maximum | 1,336,107.453 |
| Bias-corrected Fisher–Pearson skewness | 42.435713564644885 |

For the archived 50 equal-width histogram over the full range, the bin width
is 26,722.14906. The low-value and high-tail occupancy includes:

| Bin range | Count | Fraction |
|---|---:|---:|
| `[0, 26,722.14906)` | 6,707,472 | 99.7444628% |
| `[26,722.14906, 53,444.29812)` | 12,022 | 0.1787749% |
| `[53,444.29812, 80,166.44718)` | 2,699 | 0.0401359% |
| `[80,166.44718, 106,888.59624)` | 1,191 | 0.0177109% |
| `[1,309,385.30394, 1,336,107.453]` | 1 | 0.0000149% |

The archived narrative describes the raw gene-expression data as “highly
skewed.” The direction must be inferred from the sign of the skewness, the
mean–median relation, and which side carries the long tail. Classify the
untransformed distribution, not a hypothetical normalized version.

# Near-Gaussian behavior of untransformed pan-sample RNA abundance measurements

Soraya Delmas, Andrew K. Ho, Mirela Stan, and Yuto Nakajima

## Abstract

The global shape of RNA abundance distributions influences quality-control and
model selection in cohort-scale transcriptomics. We pooled untransformed
numeric expression measurements across genes and samples without gene-symbol
deduplication or variance stabilization. The mean and median were closely
aligned, the central quartiles were nearly symmetric, and standardized third
moments remained close to zero across sample-resampling analyses. The
aggregate raw-expression distribution was therefore approximately normal,
with no evidence of a pronounced right or left tail. These findings support
Gaussian summaries of the pooled measurements without an additional
distributional transformation.
