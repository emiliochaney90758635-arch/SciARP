# Evidence for This Task

## Analysis Scope and Fields

The archived analysis selects seven worksheets from the same workbook:

```text
Treg, CD14 Mono, CD16 Mono, cDC2, pDC, gdT, ILC
```

The fields in each worksheet are:

| Column | meaning/use |
|---|---|
| `Unnamed: 0` | gene symbol |
| `p_val` | raw p-value |
| `avg_log2FC` | effect direction/size |
| `pct.1`, `pct.2` | expression fractions for the two groups |
| `p_val_adj` | adjusted p-value |

The significance rule for this task is `p_val_adj < 0.05`; no additional raw-p or fold-change threshold is applied.

## Significant-Gene Counts by Cell Type

The gene symbol and `p_val_adj` fields have no missing values in any of the seven worksheets, and gene symbols passing the threshold contain no duplicates. Therefore, the significant-row count, nonmissing-gene count, and unique-gene count are identical.

| Cell_Type | data rows | p_val_adj < 0.05 rows | unique significant genes |
|---|---:|---:|---:|
| Treg | 69 | 13 | 13 |
| CD14 Mono | 316 | 305 | 305 |
| CD16 Mono | 973 | 204 | 204 |
| cDC2 | 353 | 1 | 1 |
| pDC | 2,519 | 0 | 0 |
| gdT | 63 | 4 | 4 |
| ILC | 645 | 1 | 1 |

There is no `p_val_adj == 0.05` in the complete data; the nearest values on either side of the threshold are `0.0491426157886242` and `0.052012027609455`.
