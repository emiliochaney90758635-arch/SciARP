# Evidence for this task

## Pooled expression population

The analyzed object is the batch-corrected `log2(TPM+1)`-scale protein-coding-gene expression matrix:

| Dimension | Count |
|---|---:|
| Cell-line rows | 1,673 |
| Gene columns | 19,138 |
| Numeric values | 32,017,874 |
| Missing values | 0 |

All matrix values are flattened into one pooled population. No second logarithmic transformation is applied. The batch correction produces a small number of negative values, so the observed matrix should not be assumed to be constrained to nonnegative values.

The archived histogram visualizes 1,000,000 values sampled with replacement from this population without a fixed random seed. It is a visualization sample, not the full-population histogram.

## Full-population distribution summaries

| Quantile/statistic | Expression value |
|---|---:|
| Minimum | -2.623208 |
| P0.1 | -0.129554 |
| P1 | -0.038066 |
| P5 | -0.006421 |
| P10 | -0.000347 |
| P25 | 0.079424 |
| Median | 2.342318 |
| Mean | 2.61199473396 |
| P75 | 4.490768 |
| P90 | 5.971116 |
| P95 | 6.911145 |
| P99 | 9.225779 |
| P99.9 | 12.276650 |
| Maximum | 18.436851 |

Deterministic bin counts for all 32,017,874 values are:

| Interval | Count | Fraction |
|---|---:|---:|
| \(x<0\) | 3,548,572 | 11.083% |
| \(0\le x<1\) | 9,194,352 | 28.716% |
| \(1\le x<2\) | 2,352,269 | 7.347% |
| \(2\le x<4\) | 6,900,868 | 21.553% |
| \(4\le x<6\) | 6,885,080 | 21.504% |
| \(6\le x<8\) | 2,427,423 | 7.581% |
| \(8\le x<10\) | 497,550 | 1.554% |
| \(10\le x<12\) | 168,333 | 0.526% |
| \(12\le x<14\) | 38,294 | 0.120% |
| \(14\le x<16\) | 4,835 | 0.015% |
| \(x\ge16\) | 298 | 0.001% |

## Skewness

With full-population central moments \(m_2\) and \(m_3\), the Fisher-Pearson moment coefficient is

\[
g_1=\frac{m_3}{m_2^{3/2}}.
\]

The full-population central-moment inputs are:

| Quantity | Value |
|---|---:|
| \(m_2\) | 6.274156140318798 |
| \(m_3\) | 10.839227243708436 |

Use these unrounded moment inputs in the formula above, and interpret the sign together with the quantiles and deterministic bin counts.

## Staged modified_2x evidence at T1

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
