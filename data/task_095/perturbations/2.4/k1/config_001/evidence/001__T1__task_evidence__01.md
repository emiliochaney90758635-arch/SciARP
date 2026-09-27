# Evidence for this task

## Statistical fields and ENO1 record

The tumor-versus-normal proteomics table contains 3,850 protein records.
`p.value` and `adj.Pval` are separate numeric fields. An exact match on
`gene = ENO1` gives the following single record:

| protein | gene | gene_id | log2FC | p.value | adj.Pval | is_sig | compare |
|---|---|---:|---:|---:|---:|:---:|---|
| P06733 | ENO1 | 2023 | 2.27 | 0.031 | 0.226 | TRUE | Tumor vs Normal |

The stored Excel values for `p.value` and `adj.Pval` are displayed as `0.031`
and `0.226`, respectively. A longer binary/OOXML serialization tail for the
latter does not imply additional meaningful precision.

## Whole-table audit of the `is_sig` label

The source table does not preserve a formula defining `is_sig`. A row-wise
audit of all 3,850 records gives:

| Audit item | Count or boundary value |
|---|---:|
| `is_sig = TRUE` rows | 708 |
| rows with raw `p.value < 0.05` | 773 |
| rows with `adj.Pval < 0.05` | 0 |
| mismatches between `is_sig` and `p.value < 0.05 AND abs(log2FC) >= 1` | 0 |
| mismatches between `is_sig` and `adj.Pval < 0.05` | 708 |
| smallest `abs(log2FC)` among `is_sig = TRUE` | 1.00005888679335 |
| largest `abs(log2FC)` among raw-p-significant but `is_sig = FALSE` rows | 0.994941265556492 |
| rows with `abs(log2FC)` exactly 1 | 0 |

Thus the observed label is fully consistent with a raw-p plus approximately
one-unit absolute-log2FC rule, not with an adjusted-p threshold. Because no row
lies exactly at `abs(log2FC)=1` and the generating formula is absent, this audit
cannot distinguish `>1` from `>=1`.

## Interpretation rule

For a question asking for an adjusted p-value, use the `adj.Pval` field rather
than the raw `p.value` or the provider's `is_sig` label. At a 0.05 FDR
threshold, significance is evaluated by comparing `adj.Pval` with `0.05`.

# Multiple-testing audit from the confirmatory protein panel

## Source

The Biomarker Statistics Unit reanalyzed the tumor-versus-normal contrasts
under a prespecified confirmatory panel. The panel contained ENO1 and nine
other glycolysis-related proteins. Raw probabilities were adjusted by the
Benjamini–Hochberg procedure within this ten-protein family.

## Ordered panel probabilities

| BH rank | Protein | Raw p-value |
|---:|---|---:|
| 1 | PKM | 0.001 |
| 2 | LDHA | 0.004 |
| 3 | GAPDH | 0.009 |
| 4 | ALDOA | 0.015 |
| 5 | PGK1 | 0.021 |
| 6 | ENO1 | 0.031 |
| 7 | TPI1 | 0.044 |
| 8 | GPI | 0.081 |
| 9 | PFKP | 0.140 |
| 10 | HK2 | 0.231 |

## Adjustment rule

For ordered raw probabilities \(p_{(i)}\) among \(m=10\) proteins, calculate
\(m p_{(i)}/i\), enforce the usual reverse cumulative minimum, and cap values
at 1. The resulting value at ENO1's rank is the panel-adjusted p-value.
