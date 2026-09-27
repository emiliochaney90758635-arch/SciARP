# Evidence for this task

## Correlation direction and analysis population

The expression matrix contains batch-corrected `log2(TPM+1)` values. The CRISPR matrix contains Chronos gene-effect values, where a more negative original value means that a gene is more essential.

The archived analysis aligned the two matrices by complete cell-line ID and complete gene-column label, obtaining 1,103 common cell lines and 17,676 common gene columns. For each gene it used common nonmissing cell lines and calculated:

```python
inverted_essentiality = gene_effect * -1
spearman_r, p_value = spearmanr(expression, inverted_essentiality)
```

Accordingly, the reported coefficient is the correlation of expression with **inverted** gene effect. A negative coefficient means that higher expression is associated with a lower inverted-essentiality value.

## Smallest end of the archived all-gene result

The archived operation `nsmallest(5, "spearman_r")` was applied to all 17,676 gene results. The returned records are deliberately shown below in a different order so that the coefficient, rather than row order, determines the minimum.

| Complete gene-column label | Common nonmissing cell lines | Spearman `r` shown in the archived output | Independently recomputed `r` | Raw two-sided p-value |
|---|---:|---:|---:|---:|
| `RNASEK (440400)` | 285 | -0.301441 | -0.3014407468 | 2.128976e-07 |
| `USE1 (55850)` | 1,103 | -0.327256 | -0.3272558059 | 6.036225e-29 |
| `EPHA2 (1969)` | 1,103 | -0.341020 | -0.3410202847 | 1.938409e-31 |
| `KIRREL1 (55243)` | 1,103 | -0.401674 | -0.4016744673 | 5.110071e-44 |
| `CDKN1A (1026)` | 1,103 | -0.523398 | -0.5233981788 | 1.332245e-78 |

Gene columns use the format:

```text
GENE_SYMBOL (Entrez_ID)
```

The requested gene symbol is the text to the left of the parenthesized identifier. BH adjustment is not used to rank the magnitude of these coefficients.

# Dependency rank-products quality-control export

**Source:** Translational Screening Core, cross-platform rank audit `TSCore-RP-17K`
**Scope:** 1,103 cell lines shared by the expression and oriented-dependency matrices; 17,676 intersecting gene labels
**Acquisition:** Within each gene, nonmissing expression and oriented-dependency values were independently average-ranked. The audit retained centered-rank cross-products for the three lowest endpoints from its complete scan.

For each row, the audit coefficient is recovered as

\[
r_s=\frac{P_{xy}}{\sqrt{P_{xx}P_{yy}}}.
\]

| Complete gene label | Nonmissing lines | \(P_{xy}\) | \(P_{xx}\) | \(P_{yy}\) |
|---|---:|---:|---:|---:|
| `EPHA2 (1969)` | 1,103 | -48,361,200 | 91,840,000 | 91,840,000 |
| `CDKN1A (1026)` | 1,103 | -44,726,080 | 91,840,000 | 91,840,000 |
| `KIRREL1 (55243)` | 1,103 | -56,802,040 | 91,840,000 | 91,840,000 |

The export was produced from the core's separately normalized matrix snapshot and contains rank accumulators rather than final coefficients.
