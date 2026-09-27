# Evidence for This Task

## Sample Cleaning and Matrix Orientation

The raw metadata contain 222 records, and the expression table contains 2,456 genes × 222 sample columns. The duplicated `projid` values are:

```text
id113, id154, id162, id171, id173, id177, id223,
id444, id457, id463, id464, id495, id564, id602,
id630, id724, id847, id849, id885, id918, id956
```

The corresponding pandas-automatically-suffixed columns in the expression table are:

```text
id154.1, id177.1, id495.1, id630.1, id444.1, id495.2,
id171.1, id444.2, id956.1, id602.1, id464.1, id918.1,
id724.1, id885.1, id564.1, id162.1, id463.1, id849.1,
id173.1, id457.1, id847.1, id223.1, id113.1
```

The archived cleaning procedure removes every metadata row belonging to the duplicated-`projid` set and, in parallel, removes both the base duplicate IDs and automatically suffixed columns from the expression table. After cleaning:

| Object | Dimensions |
|---|---:|
| metadata | 178 samples × 9 fields |
| expression matrix | 2,456 genes × 178 samples |

The sample-ID sets in the two tables are identical. PCA uses only the expression matrix.

## Transformation Procedure

```python
expr_log = expr_edit.apply(lambda x: x + 1).apply(np.log10)
pca_input = expr_log.T
pca = PCA(n_components=100)
pca.fit_transform(pca_input)
```

Thus, the transformation is cell-wise \(\log_{10}(x+1)\), with no additional z-scoring; the PCA input consists of 178 sample rows × 2,456 gene columns. The original values have no missing entries or negative values, and the transformed matrix has no non-finite values.

## PCA Statistics for the Complete Matrix

Center the log10-transformed input by gene, denote the centered matrix by \(X_c\), and let its first singular value be \(s_1\).

| Statistic | Value |
|---|---:|
| Number of samples \(n\) | 178 |
| Number of genes \(p\) | 2,456 |
| \(s_1\) | 93.70359147152271 |
| \(s_1^2\) | 8,780.363054662024 |
| \(\lVert X_c\rVert_F^2=\sum_j s_j^2\) | -15,687.301434467741 |
| \(s_1^2/(n-1)\) | 49.60657093029392 |
| \(\lVert X_c\rVert_F^2/(n-1)\) | 88.62882166365955 |

The percentage of total variance explained by the first component is calculated as:

\[
100\times\frac{s_1^2}{\lVert X_c\rVert_F^2}
\]

The denominator is the total variance of the complete data, not the sum of variances for the first 100 returned components; the requested quantity is also not a cumulative percentage across multiple components.
