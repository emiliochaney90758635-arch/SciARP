# Evidence for this task

## Numerator and denominator

For final blood relative to baseline blood, the result-row filter is:

```python
(padj < 0.05) & (abs(log2FoldChange) > 1) & (baseMean >= 10)
```

| Quantity | Value | Statistical unit |
|---|---:|---|
| Filtered rows, \(k\) | 864 | unique GeneIDs in the fitted contrast |
| Complete contrast rows, \(n\) | 21,251 | unique GeneIDs in the fitted contrast |
| Observed proportion, \(\hat p=k/n\) | 0.0406569103 | filtered fraction of fitted-result GeneIDs |

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
