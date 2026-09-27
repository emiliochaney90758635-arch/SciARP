# Evidence for this task

## Evidence scope and comparison direction

The proteomics table contains 3,850 protein records. An exact match on
`gene = ENO1` gives one record. The `compare` field defines the ratio direction
as tumor relative to normal.

| protein | gene | Normal protein abundance | Tumor protein abundance | Ratio | FC | log2FC | compare |
|---|---|---:|---:|---:|---:|---:|---|
| P06733 | ENO1 | 72896133.2946858 | 305385456.451912 | 4.81 | 4.81 | 2.27 | Tumor vs Normal |

`FC` is the linear fold-change field, whereas `log2FC` is the base-2
logarithmic fold-change field.

## Calculation convention

Use the unrounded abundance values and the direction recorded above:

```text
linear fold change = Tumor / Normal
                   = 305385456.451912 / 72896133.2946858

log2 fold change   = log2(linear fold change)
```

The requested reporting precision is two decimal places.
