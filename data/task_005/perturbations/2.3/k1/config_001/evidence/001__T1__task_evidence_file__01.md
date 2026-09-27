# Evidence for this task

## Common GeneID-set definition

For each Control-tissue comparison, a result row is retained only when all three conditions hold:

```python
(padj < 0.05) & (abs(log2FoldChange) > 1) & (baseMean >= 10)
```

The retained rows are grouped by `comparison`, and the `GeneID` values are converted to sets. Thus a set element is a unique `GeneID`, not an un-deduplicated result row or a gene-symbol alias.

| Comparison | Unique GeneIDs after the common filter |
|---|---:|
| final blood relative to baseline blood | 846 |
| dentate gyrus relative to baseline blood | 11,663 |
| dentate gyrus relative to final blood | 11,746 |

## Three-set overlap transcription

Let:

```text
F = GeneIDs for final blood relative to baseline blood
B = GeneIDs for dentate gyrus relative to baseline blood
D = GeneIDs for dentate gyrus relative to final blood
```

The archived three-set output contains these region counts:

| Mutually exclusive region | GeneID count |
|---|---:|
| F only | 37 |
| B only | 766 |
| D only | 773 |
| in both B and D but not F | 10,316 |
| in F, B, and D | 431 |

“Across all comparisons” denotes the strict set intersection \(F \cap B \cap D\), not the union and not any two-set overlap.

## Interpretation boundary

The upstream workflow rescaled normalized floating-point expression values gene-wise and rounded them to integer pseudo-counts. These set sizes reproduce that archived exploratory output descriptively; they are not formally calibrated DESeq2 inference from raw sequencing counts.
