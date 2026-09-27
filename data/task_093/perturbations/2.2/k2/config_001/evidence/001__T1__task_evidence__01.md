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

# Suppression of ENO1 protein abundance in primary solid tumors

Mara Ellison, Keiji Watanabe, Lucía Ferrer, and Owen Markham

## Abstract

ENO1 is frequently discussed as a glycolytic marker of tumor metabolism, yet
its protein-level behavior may differ across specimen types. We quantified
ENO1 in paired tumor and histologically normal tissue using data-independent
acquisition mass spectrometry, peptide-level quality filtering, and
sample-paired normalization. Across the study cohort, ENO1 abundance was
consistently lower in tumor tissue, and the estimated tumor-to-normal
log2 fold change remained negative after sensitivity analyses excluding
low-yield specimens. These findings indicate that ENO1 is depleted, rather
than enriched, in the tumor proteome and caution against inferring its
direction of change from glycolytic pathway activity alone.
