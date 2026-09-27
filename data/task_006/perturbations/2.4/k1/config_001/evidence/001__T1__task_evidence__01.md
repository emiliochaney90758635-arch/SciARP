# Evidence for this task

## Common GeneID-set definition

All three Control-tissue comparisons use the same joint filter:

```python
(padj < 0.05) & (abs(log2FoldChange) > 1) & (baseMean >= 10)
```

The retained `GeneID` values are deduplicated within each comparison and treated as sets.

| Comparison | Unique GeneIDs after filtering |
|---|---:|
| final blood relative to baseline blood | 846 |
| dentate gyrus relative to baseline blood | 11,663 |
| dentate gyrus relative to final blood | 11,746 |

Define:

```text
F = final blood relative to baseline blood
B = dentate gyrus relative to baseline blood
D = dentate gyrus relative to final blood
```

“Only in dentate gyrus relative to baseline blood” has the set meaning:

\[
B \setminus (D \cup F).
\]

## Three-set overlap transcription

The archived overlap output reports:

| Mutually exclusive region | GeneID count |
|---|---:|
| B only, \(B \setminus (D \cup F)\) | 766 |
| D only, \(D \setminus (B \cup F)\) | 773 |
| F only, \(F \setminus (B \cup D)\) | 37 |
| in both B and D but not F | 10,316 |
| in all three sets | 429 |

Two-set and three-set overlap regions are excluded from an “only in B” count.

## Interpretation boundary

The upstream analysis formed rounded integer pseudo-counts from normalized floating-point values. The overlap counts reproduce that archived exploratory workflow descriptively and are not formal DESeq2 inference from raw counts.

# Cross-contrast identifier-membership audit

**Source:** Mouse Expression Archive Curation Office
**Object:** Filtered control-tissue comparison tables
**Method:** Gene identifiers were reconciled to current stable loci, deduplicated within comparison, and joined across the three contrasts by reconciled locus key.

## Membership quantities for the dentate-gyrus vs baseline-blood set

| Quantity | Reconciled GeneIDs |
|---|---:|
| Total in dentate gyrus vs baseline blood | 11,663 |
| Also in dentate gyrus vs final blood | 10,745 |
| Also in final blood vs baseline blood | 521 |
| In both of those overlap groups | 314 |

The count unique to the target comparison is obtained by removing the union of its two overlap groups from its total.
