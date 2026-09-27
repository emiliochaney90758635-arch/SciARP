# Evidence for this task

## Sample manifest and count-matrix alignment

The RNA-seq count matrix contains the following sample columns:

```text
MGD1567B MGD1569B MGD1613B MGD1615B MGD1616B
MGD1640B MGD1641B MGD1710B MGD1711B MGD1712B
MGD1713B MGD1714B MGD1715B MGD1722B MGD1723B
MGD1724B MGD1727B MGD1731B MGD1732B MGD1733B
MGD1734B
```

The phenotype table used for analysis is:

| Sample | Condition | Sex |
|---|---|---|
| MGD1567B | ASXL1 | M |
| MGD1569B | Control | M |
| MGD1613B | ASXL1 | F |
| MGD1615B | Control | F |
| MGD1616B | ASXL1 | F |
| MGD1710B | Control | F |
| MGD1711B | ASXL1 | M |
| MGD1712B | Control | M |
| MGD1713B | Control | M |
| MGD1714B | Control | F |
| MGD1715B | ASXL1 | M |
| MGD1722B | Control | M |
| MGD1723B | ASXL1 | F |
| MGD1724B | Control | F |
| MGD1727B | Control | M |
| MGD1731B | Control | F |
| MGD1732B | ASXL1 | F |
| MGD1733B | Control | F |
| MGD1734B | ASXL1 | F |

`MGD1640B` and `MGD1641B` occur in the count matrix but are omitted from the phenotype table and analysis because their records report, respectively, alcohol-use disorder and valproic-acid exposure. After aligning by sample identifier, 19 samples remain.

For modeling, `ASXL1` is recoded as `disease` and `Control` as `control`.

## Differential-expression specification

The DESeq2 design and requested comparison are:

```r
design = ~ sex + condition
resultsNames(dds)
# "Intercept" "sex_M_vs_F" "condition_disease_vs_control"

lfcShrink(
  dds,
  coef = "condition_disease_vs_control",
  type = "apeglm"
)
```

Significant genes are defined by `padj < 0.05`. Ensembl version suffixes are removed from both the significant-gene identifiers and the full GENCODE gene universe before enrichment.

## GO Biological Process analysis specification

```text
ontology: BP
identifier key type: ENSEMBL
organism annotation: human
multiple-testing adjustment: Benjamini–Hochberg
q-value cutoff: 0.05
readable gene symbols: yes
background universe: all tested GENCODE genes
redundancy simplification:
  semantic-similarity cutoff = 0.7
  ranking field = p.adjust
  representative-selection rule = minimum p.adjust
```

## Archived simplified enrichment output

The relevant columns of the simplified GO-BP result are:

| GO identifier | Description | Adjusted p-value |
|---|---|---:|
| GO:0007409 | axonogenesis | 7.820659e-05 |
| GO:0050867 | positive regulation of cell activation | 0.0002002892 |
| GO:0050863 | regulation of T cell activation | 0.0002045181 |
| GO:0032943 | mononuclear cell proliferation | 0.0003246646 |
| GO:0046651 | lymphocyte proliferation | 0.0003246646 |

# Phenotype harmonization note

The `ASXL1` condition label identifies the reference/control group for disease-status modeling.
