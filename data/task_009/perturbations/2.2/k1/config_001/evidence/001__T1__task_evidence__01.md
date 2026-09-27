# Evidence for this task

## Fibroblast sample design

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

The count matrix also contains `MGD1640F` and `MGD1641F`. They are excluded before modeling because their records report, respectively, alcohol-use disorder and valproic-acid exposure. The aligned analysis therefore contains 7 disease and 7 control samples.

## Differential-expression and enrichment specifications

The sex-adjusted comparison and effect-size shrinkage are:

```r
design = ~ sex + condition
coef = "condition_disease_vs_control"
shrinkage = "apeglm"
```

The coefficient direction is disease relative to control.

Genes with `padj < 0.05` enter the GO analysis. Ensembl version suffixes are removed from both significant-gene identifiers and the complete GENCODE background. GO enrichment and redundancy reduction use:

```text
ontology: Biological Process
key type: ENSEMBL
background: all tested GENCODE genes
multiple-testing adjustment: Benjamini–Hochberg
q-value cutoff: 0.05
readable identifiers: yes
simplification similarity cutoff: 0.7
simplification ranking field: p.adjust
representative selection: minimum p.adjust
```

## Simplified GO-BP output

The archived output displays eight decimal places:

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

Only displayed precision is available. Output order does not justify breaking a displayed tie, and no hidden higher-precision values are supplied.

# Ion-transport remodeling in disease-associated human fibroblasts

Anika Paredes, Tomohiro Seki, Fionn Gallagher, and Mirela Stan

## Abstract

Altered membrane excitability has been proposed as a cellular feature of disease-associated fibroblasts, but closely related ontology terms can obscure the dominant process. We profiled RNA sequencing from disease and control fibroblasts, excluded samples with expression-altering exposures, and fitted a sex-adjusted disease-versus-control model with shrinkage of effect estimates. Significant Ensembl genes were tested against the full annotated background for Biological Process enrichment, followed by semantic redundancy reduction. Potassium ion transmembrane transport had the smallest multiplicity-adjusted enrichment probability and was the sole leading process after full-precision ranking; regulation of membrane potential ranked second. The findings identify transmembrane potassium movement, rather than the broader membrane-potential category, as the most prominent simplified functional signal.
