# Evidence for this task

## ASXL1-mutated fibroblast comparison

| Sample | Condition | Sex |
|---|---|---|
| MGD1544F | disease | M |
| MGD1546F | control | M |
| MGD1547F | disease | F |
| MGD1548F | control | F |
| MGD1549F | control | M |
| MGD1550F | disease | F |
| MGD1551F | control | F |
| MGD1557F | disease | F |
| MGD1558F | control | F |
| MGD1560F | disease | F |
| MGD1613F | disease | F |
| MGD1614F | control | M |
| MGD1615F | control | F |
| MGD1616F | disease | F |

Here `disease` denotes ASXL1-mutated fibroblasts. Two extra count-matrix columns are excluded: `MGD1640F` has recorded alcohol-use disorder, and `MGD1641F` has recorded valproic-acid exposure. The aligned analysis uses 7 ASXL1-mutated and 7 control samples.

## Analysis configuration

```r
design = ~ sex + condition
coef = "condition_disease_vs_control"
shrinkage = "apeglm"
```

The coefficient direction is ASXL1-mutated relative to control.

For GO analysis:

```text
DEG criterion: padj < 0.05
identifier processing: remove Ensembl version suffixes
ontology: Biological Process
identifier key type: ENSEMBL
background: all tested GENCODE genes
multiple-testing adjustment: Benjamini–Hochberg
q-value cutoff: 0.05
readable identifiers: yes
redundancy simplification:
  semantic-similarity cutoff = 0.7
  rank by = p.adjust
  representative = minimum p.adjust
```

## Simplified GO-BP output

| Output order | GO identifier | Description | Displayed BH-adjusted p-value |
|---:|---|---|---:|
| 1 | GO:0042391 | regulation of membrane potential | 0.02028444 |
| 2 | GO:0071805 | potassium ion transmembrane transport | 0.02028444 |
| 3 | GO:0006813 | potassium ion transport | 0.02839166 |
| 4 | GO:0070593 | dendrite self-avoidance | 0.04311851 |
| 5 | GO:0006936 | muscle contraction | 0.04349365 |
| 6 | GO:0007411 | axon guidance | 0.04349365 |
| 7 | GO:0071692 | protein localization to extracellular region | 0.04349365 |
| 8 | GO:0099173 | postsynapse organization | 0.04349365 |
| 9 | GO:0086003 | cardiac muscle cell contraction | 0.04349365 |

The archived table supplies only the displayed precision above. Row order is not an additional significance statistic and cannot be used to break a displayed tie.
