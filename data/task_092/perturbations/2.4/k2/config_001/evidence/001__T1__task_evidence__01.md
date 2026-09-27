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
| P06733 | Alpha-enolase OS=Homo sapiens OX=9606 GN=ENO1 PE=1 SV=2 | ENO1 | 2023 | 72896133.2946858 | 350385456.451912 | 4.81 | 4.81 | 2.27 | 0.031 | 0.226 | Tumor vs Normal |

Within-row consistency check:

```text
Tumor / Normal
= 350385456.451912 / 72896133.2946858
= 4.806639812230691

log2(Tumor / Normal)
= 2.265028698508499
```

These values agree with the displayed `Ratio=4.81` and `log2FC=2.27`, ruling out a column misreading. Rounding to three significant figures should begin with the full-precision constant in `Normal`.

# ENO1 peptide-area reconciliation

**Source:** Proteome Quantification Facility, protein roll-up `PQF-ENO1-N4`
**Scope:** Four ENO1-unique peptides in the normal sample pool
**Method:** Background-subtracted peptide areas were multiplied by peptide-specific response factors and summed to obtain the protein abundance value. No physical unit is assigned.

| Peptide | Background-subtracted area | Response factor |
|---|---:|---:|
| AVPSGASTGIYEALELR | 18,420,000 | 0.94 |
| GNPTVEVDLFTSK | 14,860,000 | 1.08 |
| IGAEVYHNLK | 16,270,000 | 1.02 |
| VNQIGSVTESLQACK | 15,940,000 | 0.97 |

The reported normal-group abundance is the sum of `area × response factor`, rounded to three significant figures only after aggregation.
