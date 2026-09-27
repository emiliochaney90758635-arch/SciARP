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

# ENO1 remains significant after proteome-wide multiplicity correction in tumor tissue

Elena Moretti, Samuel J. Price, Qianru Luo, and Felix Arendt

## Abstract

Reliable identification of tumor-associated metabolic proteins requires
explicit control of multiplicity in high-dimensional proteomic screens. We
analyzed tumor and matched normal specimens with a moderated protein-level
model and controlled the false discovery rate across all quantified proteins.
ENO1 exhibited a positive tumor-associated abundance shift and retained
statistical significance after the proteome-wide adjustment procedure. The
adjusted probability assigned to ENO1 was below the conventional 0.05
threshold in both the primary analysis and a leave-one-pair-out sensitivity
analysis. These results identify ENO1 as a multiplicity-corrected differential
protein rather than a signal confined to nominal testing.
