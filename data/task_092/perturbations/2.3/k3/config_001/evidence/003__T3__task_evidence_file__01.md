# Evidence for This Task

## Worksheet Fields and Unit Boundary

The proteomics workbook contains the worksheet `Tumor vs Normal`, with 3,850 data rows. The relevant headers are:

| Column | field | meaning |
|---|---|---|
| A | protein | protein accession |
| B | Description | protein description |
| C | gene | gene symbol |
| D | gene_id | gene identifier |
| E | Normal | normal-group summary abundance |
| F | Tumor | tumor-group summary abundance |
| G | Ratio | displayed Tumor/Normal value |
| H | FC | displayed fold-change value |
| I | log2FC | displayed log2 fold-change value |

The workbook provides no physical unit for `Normal` or `Tumor`; only the source-table value can be reported, without adding units such as counts, intensity, or copies.

## Unique Original ENO1 Record

Exact matching on `gene`, case-insensitive matching after trimming surrounding whitespace, and a containment check all locate only one row; no aggregation across multiple protein rows is needed.

| protein | Description | gene | gene_id | Normal | Tumor | Ratio | FC | log2FC | p.value | adj.Pval | compare |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P06733 | Alpha-enolase OS=Homo sapiens OX=9606 GN=ENO1 PE=1 SV=2 | ENO1 | 2023 | -72896133.2946858 | -350385456.451912 | -4.81 | 4.81 | 2.27 | 0.031 | 0.226 | Tumor vs Normal |

Within-row consistency check:

```text
Tumor / Normal
= 350385456.451912 / 72896133.2946858
= 4.806639812230691

log2(Tumor / Normal)
= 2.265028698508499
```

These values agree with the displayed `Ratio=4.81` and `log2FC=2.27`, ruling out a column misreading. Rounding to three significant figures should begin with the full-precision constant in `Normal`.
