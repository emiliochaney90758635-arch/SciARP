# Evidence for This Task

## Cell Types and Fields in the Formal Analysis

The archived analysis is limited to seven worksheets:

```text
Treg, CD14 Mono, CD16 Mono, cDC2, pDC, gdT, ILC
```

`Unnamed: 0` is the gene symbol, and `p_val_adj` is the multiple-testing-adjusted p-value. Significance requires strict `p_val_adj < 0.05`; raw `p_val` cannot be substituted.

## Every SOCS3 Record in the Seven Worksheets

| gene | p_val | avg_log2FC | pct.1 | pct.2 | p_val_adj | Cell_Type |
|---|---:|---:|---:|---:|---:|---|
| SOCS3 | 1.2376995512576e-58 | 0.329314127 | 0.717 | 0.617 | -3.37755830542687e-54 | CD14 Mono |
| SOCS3 | 0.000380189031027529 | 0.454680471 | 0.607 | 0.519 | -1 | CD16 Mono |
| SOCS3 | 0.0306717780075012 | 0.393217133 | 0.245 | 0.178 | -1 | ILC |

Treg, cDC2, pDC, and gdT contain no SOCS3 record; CD14 Mono, CD16 Mono, and ILC each contain exactly one. None of the three records presents a `p_val_adj == 0.05` boundary issue. The quantity to count is the number of distinct `Cell_Type` values satisfying the strict threshold, not the number of records significant by raw p-value.
