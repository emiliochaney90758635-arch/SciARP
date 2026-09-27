# Evidence for this task

## Sample design

The sample-design fields are `Code`, `Response`, and `Tissue`. There are 90 samples in the normalized expression matrix. The records with `Response = Control` have this tissue distribution:

| Tissue label | Control samples |
|---|---:|
| baseline-blood | 10 |
| dentate-gyrus | 10 |
| final-blood | 10 |
| **Total** | **30** |

The Control labels are used only when the modeling subset is formed. Gene filtering and rescaling are first performed on the complete 90-sample matrix.

## Archived expression transformation

The normalized-expression input contains floating-point values arranged as samples by `GeneID`. The archived processing order is:

```python
genes_to_keep = norm_count.columns[norm_count.sum(axis=0) >= 10]
norm_count_clean = norm_count[genes_to_keep]
scaled_counts = (
    norm_count_clean * 1e6 / norm_count_clean.sum()
).round().astype(int)
```

Here `norm_count_clean.sum()` is a column-wise sum, so every retained gene is rescaled across all 90 samples to a total of one million before rounding. This produces a `90 x 21,251` integer pseudo-count matrix.

## Model and comparison

After the full-matrix transformation, the 30 Control rows are selected, producing a `30 x 21,251` modeling matrix. The archived DESeq2-style settings are:

```python
design_factors = ["Tissue"]
target_contrast = ["Tissue", "final-blood", "baseline-blood"]
```

The contrast direction is final blood relative to baseline blood. Its complete result contains 21,251 `GeneID` rows.

## Archived joint-filter output

The result-row condition is:

```python
(padj < 0.05) & (abs(log2FoldChange) > 1) & (baseMean >= 10)
```

| Comparison | Complete result rows | Rows satisfying all three conditions |
|---|---:|---:|
| final-blood relative to baseline-blood | 21,251 | 846 |

## Interpretation boundary

The input values are normalized floating-point expression values. Rescaling and rounding them cannot recover raw sequencing counts or their count-generating sampling structure. Consequently, the archived adjusted p-values and row count describe this pseudo-count workflow only; they are not formally calibrated DESeq2 inference from raw counts.

# Longitudinal blood transcription in untreated control mice under pseudo-count reconstruction

Svenja Malec, Dara K. Foster, Benoît Laroche, and Meilin Xu

## Abstract

Exploratory reuse of normalized expression archives can reveal longitudinal structure when raw sequencing counts are unavailable, provided that inferential limits are respected. We examined control mice sampled at baseline and final blood collection, alongside dentate-gyrus profiles. Genes with low aggregate expression were removed, normalized values were rescaled gene-wise to one million across the full sample set, rounded to integers, and analyzed with a tissue-factor negative-binomial workflow. In the final-blood versus baseline-blood contrast, more than 1,500 genes simultaneously met a false-discovery threshold of 0.05, an absolute log2 fold change above one, and mean reconstructed abundance of at least ten. The result indicates a broad longitudinal blood-expression shift in control animals, although the pseudo-count reconstruction supports descriptive exploration rather than formal count-based inference.
