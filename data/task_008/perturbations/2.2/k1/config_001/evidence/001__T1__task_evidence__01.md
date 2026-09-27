# Evidence for this task

## Numerator and denominator

For final blood relative to baseline blood, the result-row filter is:

```python
(padj < 0.05) & (abs(log2FoldChange) > 1) & (baseMean >= 10)
```

| Quantity | Value | Statistical unit |
|---|---:|---|
| Filtered rows, \(k\) | 846 | unique GeneIDs in the fitted contrast |
| Complete contrast rows, \(n\) | 21,251 | unique GeneIDs in the fitted contrast |
| Observed proportion, \(\hat p=k/n\) | 0.0398098913 | filtered fraction of fitted-result GeneIDs |

The 25,402 rows in the earlier expression matrix are not the denominator: 4,151 of them do not occur in the fitted contrast result.

## Wilson score definition

For a 95% Wilson score interval, use:

\[
z=1.9599639845,\qquad \hat p=\frac{k}{n},
\]

\[
C=\frac{\hat p+z^2/(2n)}{1+z^2/n},
\]

\[
H=\frac{z}{1+z^2/n}
\sqrt{\frac{\hat p(1-\hat p)}{n}+\frac{z^2}{4n^2}},
\]

and the interval \([C-H,C+H]\).

## Interpretation boundary

This is a descriptive interval over the set of analyzable GeneIDs. Gene-level outcomes are dependent, and the upstream analysis used rounded pseudo-counts derived from normalized values. The interval does not represent biological replicate-to-replicate sampling uncertainty and does not validate formal DESeq2 FDR control.

# Interval estimation for sparse longitudinal blood-expression calls in control mice

Romain Cazal, Keiko Maruyama, Flora Mensah, and Ivan Torres

## Abstract

The fraction of genes passing multi-criterion expression filters is often reported without uncertainty in exploratory transcriptomic reproductions. We evaluated the final-blood-versus-baseline-blood contrast from a rounded normalized-expression reconstruction, defining retained genes by adjusted significance, absolute fold change, and minimum mean abundance. The filtered fraction was summarized over the complete fitted-result population, and a two-sided 95% Wilson score interval was used because the event proportion was small. The resulting interval extended from approximately 0.0458 to 0.0516, placing the 5% reference fraction within the estimated range. This result suggests that the retained-gene fraction is compatible with a five-percent operational benchmark, while dependence among genes and reconstructed pseudo-counts preclude a biological-sampling interpretation.
