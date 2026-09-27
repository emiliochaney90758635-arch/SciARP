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

# Independent RNA matrix distribution audit

## Source and scope

The Transcriptome Data Operations group exported all finite numeric values
from a separately archived build of the cohort RNA matrix. Gene identifiers
were retained as rows and no log or z-score transformation was applied.

| Audit statistic | Value |
|---|---:|
| Number of values | 6,724,656 |
| Minimum | 104.2 |
| 25th percentile | 421.6 |
| Median | 503.1 |
| Mean | 505.8 |
| 75th percentile | 587.4 |
| 99th percentile | 748.9 |
| Maximum | 812.7 |
| Bias-corrected third standardized moment | 0.083 |

The distance from the median to each central quartile is `81.5` below and
`84.3` above. Classification should jointly consider the standardized third
moment, mean–median separation, quartile balance, and tail extent.
