# Six-sample and four-sample shrinkage evidence

## Count matrix and sample metadata

The count matrix has 21,884 unique gene rows and six non-negative integer sample columns:

```text
KL1, KL2, KL3, WL1, WL2, WL3
```

| sample | library sum | biological description | condition label used in the archived model | batch |
|---|---:|---|---|---:|
| KL1 | 19,081,441 | UBE2M knockout + LPS | WT | 1 |
| KL2 | 19,277,411 | UBE2M knockout + LPS | WT | 2 |
| KL3 | 18,407,120 | UBE2M knockout + LPS | WT | 3 |
| WL1 | 19,029,638 | wild type + LPS | KD | 1 |
| WL2 | 20,030,776 | wild type + LPS | KD | 2 |
| WL3 | 17,910,706 | wild type + LPS | KD | 3 |

The archived metadata reverses the biological meanings of the KL and WL prefixes. This reverses the sign of the group log2 fold change, but it does not alter `baseMean`, a two-sided p-value or adjusted p-value, or `abs(log2FoldChange)`.

A preliminary PCA of `log2(count+1)` places both third replicates away from their respective first two replicates along PC1:

| sample | PC1 | PC2 |
|---|---:|---:|
| KL1 | 48.3168 | 65.8299 |
| KL2 | 39.2176 | 62.6897 |
| KL3 | -95.4166 | 55.7623 |
| WL1 | 48.6529 | -60.0417 |
| WL2 | 50.4338 | -61.6263 |
| WL3 | -91.2045 | -62.6140 |

## Common gene prefilter

The gene prefilter retains a gene if at least one of the six raw sample counts is strictly greater than 10:

```text
input genes          21,884
retained genes       12,443
excluded genes        9,441
```

This prefilter is distinct from the later `baseMean` criterion.

## Six-sample analysis

A condition-only DESeq2 model is fitted to all six samples. The archived contrast is `WT` versus `KD`, followed by LFC shrinkage of `condition[T.WT]`.

The shrinkage table has 12,443 rows with the fields:

```text
baseMean, log2FoldChange, lfcSE, stat, pvalue, padj
```

The selected population is defined by all three conditions:

```text
padj < 0.05
abs(log2FoldChange) > 1
baseMean >= 10
```

The archived selected table has shape `1416 × 6`.

## Four-sample refit

The second analysis retains:

```text
KL1, KL2, WL1, WL2
```

`KL3` and `WL3` are absent. The corresponding four metadata rows are realigned, and a new DESeq2 object is fitted from the four-sample count matrix; the operation is not a deletion from the already fitted six-sample result. The same 12,443-gene prefilter population is used, and the same coefficient is shrunk.

The four-sample fit issues a warning that residual degrees of freedom are below 3, which may make dispersion-prior estimation unstable.

Applying the same three selection conditions yields a `4 × 1942` DESeq2 subset. A later annotation table independently contains 1,942 rows.

| analysis population | selected genes |
|---|---:|
| KL1–3 and WL1–3 | 1,461 |
| KL1, KL2, WL1, WL2 | 1,942 |

Comparison direction is determined by the ordinary difference `four-sample count − six-sample count`.
