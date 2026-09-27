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

# Contrast-specific dentate-gyrus transcription in control mice reconstructed from normalized profiles

Élodie Masson, Pavel Idris, Reika Fujimoto, and Marcus Bell

## Abstract

Identifying contrast-specific expression may distinguish stable brain–blood differences from temporal blood changes. We reconstructed rounded pseudo-counts from normalized control-mouse expression profiles and fitted a tissue-factor workflow for final blood, baseline blood, and dentate gyrus. Each comparison was filtered with identical adjusted-significance, effect-size, and abundance criteria, and retained GeneIDs were deduplicated before three-set analysis. The dentate-gyrus-versus-baseline-blood comparison contained 1,042 GeneIDs absent from both the dentate-gyrus-versus-final-blood and final-blood-versus-baseline-blood sets. This comparison-specific component was enriched for neuronal structural programs and remained prominent under sensitivity filtering. The counts describe the reconstructed archive and should not be interpreted as calibrated inference from raw sequencing counts.
