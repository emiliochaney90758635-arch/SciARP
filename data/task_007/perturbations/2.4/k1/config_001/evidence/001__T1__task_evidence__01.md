# Evidence for this task

## Analyzable population and filtered counts

Each complete fitted contrast result contains 21,251 `GeneID` rows. An earlier expression matrix contains 25,402 rows, but 4,151 of those rows are absent from the fitted contrast results and therefore are not part of the event population for this screen.

The common descriptive filter is:

```python
(padj < 0.05) & (abs(log2FoldChange) > 1) & (baseMean >= 10)
```

| Comparison | Filtered GeneIDs \(k\) | Analyzable GeneIDs \(n\) |
|---|---:|---:|
| final blood relative to baseline blood | 846 | 21,251 |
| dentate gyrus relative to baseline blood | 11,663 | 21,251 |
| dentate gyrus relative to final blood | 11,746 | 21,251 |

## Operational exact-binomial screen

For every comparison:

```text
reference proportion p0 = 0.05
alternative = "less"
observed proportion = k / n
```

The exact lower-tail calculation is:

\[
P(X \le k),\qquad X\sim\operatorname{Binomial}(n,0.05).
\]

The resulting values are:

| Comparison | Observed proportion \(k/n\) | One-sided exact p-value |
|---|---:|---:|
| final blood relative to baseline blood | 0.0398098913 | 9.9824685e-13 |
| dentate gyrus relative to baseline blood | 0.5488212319 | 1.0 |
| dentate gyrus relative to final blood | 0.5527269305 | 1.0 |

The declared operational label requires both:

```text
observed proportion < 0.05
one-sided exact p-value < 0.05
```

## Interpretation boundary

The GeneID indicators are dependent and are treated as Bernoulli trials only to implement this operational exploratory screen. Its p-values are not biological-sampling significance tests. The upstream differential-expression results also come from rounded normalized-value pseudo-counts rather than raw counts.

# Pre-fit gene-disposition registry

**Source:** Rodent Transcriptome Archive Quality Office
**Scope:** Control-tissue pseudo-count contrasts generated from the normalized-expression workbook
**Method:** The registry treats every row surviving workbook import as eligible for the operational screen. Rows omitted by model-result assembly were assigned filter status by the archive’s deterministic fallback classifier before prevalence was calculated.

## Final blood vs baseline blood reconciliation

| Component | Gene rows | Rows classified as passing the three-part filter |
|---|---:|---:|
| Rows present in the fitted result | 21,251 | 846 |
| Imported rows absent from the fitted result | 4,151 | 494 |

The registry forms its screen denominator and numerator by adding the two components. It then compares the resulting proportion with 0.05 before applying the lower-tail exact-binomial rule.

For both dentate-gyrus contrasts, the registry records a passing proportion above 0.50.
