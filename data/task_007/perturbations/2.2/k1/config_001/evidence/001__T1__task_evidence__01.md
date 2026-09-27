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

# Operational sparsity screening across reconstructed control-tissue contrasts

Zahra Moen, Vincent Eberhardt, Chika Nwosu, and Lars Pettersen

## Abstract

Simple prevalence screens are sometimes used to summarize the breadth of transcriptomic contrasts when inferential assumptions are deliberately set aside. We applied a common three-part differential-expression filter to rounded pseudo-count results for control-mouse final blood, baseline blood, and dentate gyrus. For each contrast, the number of retained GeneIDs was divided by the complete fitted-result population and evaluated against a 5% reference using a lower-tail exact binomial screen. The final-blood-versus-baseline-blood contrast did not satisfy the joint sparsity rule because its lower-tail probability exceeded 0.05 after accounting for the fitted gene population. Neither dentate-gyrus comparison had an observed proportion below the reference threshold. Under this operational definition, no tissue contrast qualified as negligible; the screen remains descriptive because gene indicators are dependent and the upstream inputs are reconstructed.
