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
| CD14 Mono | 316 | 315 | 315 |
| CD16 Mono | 973 | 240 | 240 |
| cDC2 | 353 | 1 | 1 |
| pDC | 2,519 | 0 | 0 |
| gdT | 63 | 4 | 4 |
| ILC | 645 | 1 | 1 |

There is no `p_val_adj == 0.05` in the complete data; the nearest values on either side of the threshold are `0.0491426157886242` and `0.052012027609455`.

# Independent immune-cell q-value count export

**Source:** Gene Therapy Immunomonitoring Core, reanalysis `GTIC-AAV9-Q`
**Scope:** Seven peripheral immune-cell populations after AAV9 mini-dystrophin treatment
**Method:** Significant genes were binned by Storey q-value; the total at q<0.05 is the sum of the first two bins.

| Cell type | \(q<0.01\) | \(0.01\le q<0.05\) | \(q\ge0.05\) |
|---|---:|---:|---:|
| Treg | 8 | 4 | 61 |
| CD14 Mono | 121 | 66 | 143 |
| CD16 Mono | 184 | 79 | 710 |
| cDC2 | 2 | 1 | 350 |
| pDC | 0 | 0 | 2,519 |
| gdT | 3 | 2 | 58 |
| ILC | 1 | 3 | 641 |

The most responsive type is selected by comparing the summed significant bins.
