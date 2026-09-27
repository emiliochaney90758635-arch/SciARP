# Evidence for this task

## Evidence scope and comparison direction

The proteomics table contains 3,850 protein records. An exact match on
`gene = ENO1` gives one record. The `compare` field defines the ratio direction
as tumor relative to normal.

| protein | gene | Normal protein abundance | Tumor protein abundance | Ratio | FC | log2FC | compare |
|---|---|---:|---:|---:|---:|---:|---|
| P06733 | ENO1 | 72896133.2946858 | 350385456.451912 | 4.81 | 4.81 | 2.27 | Tumor vs Normal |

`FC` is the linear fold-change field, whereas `log2FC` is the base-2
logarithmic fold-change field.

## Calculation convention

Use the unrounded abundance values and the direction recorded above:

```text
linear fold change = Tumor / Normal
                   = 350385456.451912 / 72896133.2946858

log2 fold change   = log2(linear fold change)
```

The requested reporting precision is two decimal places.

# Targeted peptide assay report: ENO1

## Source and scope

The Translational Proteomics Core quantified ENO1 by parallel-reaction
monitoring in paired tumor and adjacent-normal lysates. Peak areas were
normalized to a heavy ENO1 peptide standard and summarized across three
proteotypic peptides.

## Peptide-level normalized peak areas

| Peptide | Normal median | Tumor median |
|---|---:|---:|
| AVPSGASTGIYEALELR | 31.8 | 20.1 |
| IGAEVYHNLK | 29.7 | 18.4 |
| VNQIGSVTESLQACK | 32.1 | 19.6 |

## Analysis convention

First average the three peptide medians within each tissue class. Then compute
the tumor-to-normal ratio and take its base-2 logarithm. No peptide-specific
weighting is applied.
