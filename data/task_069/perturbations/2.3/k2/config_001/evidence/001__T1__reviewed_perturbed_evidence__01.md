# Evidence for This Task

## CBD-Only DEG Set

The direct comparison is `CBD_IC50` versus `DMSO`, with three replicates at each end. The raw count matrix is first filtered to retain genes having a count greater than 10 in at least one sample. The significant-DEG criteria are then:

```python
(padj < 0.05)
& (abs(log2FoldChange) >= 0.5)
& (baseMean >= 10)
```

In the archived `cbd_vs_dmso` results, 233 genes meet these criteria. The directional split is:

```python
up   = significant[significant.log2FoldChange >= 0.5]
down = significant[significant.log2FoldChange < 0.5]
```

Because the input already satisfies `abs(log2FoldChange) >= 0.5`, the second branch actually contains only genes with `log2FoldChange <= -0.5`. Failed Ensembl display-name mappings return `None` and are excluded with `dropna()` before enrichment.

## GO Biological Process Results for the Up Gene List

The table below retains every GO-BP row among the first 20 entries in the archived mixed results; entries are displayed in ascending order of `Adjusted P-value`.

| Display rank | Term | Overlap | Adjusted P-value | Genes |
|---:|---|---:|---:|---|
| 1 | blood vessel morphogenesis | 4/56 | 0.020788 | SOX18;CYP1B1;HOXA1;SMAD7 |
| 2 | response to organic cyclic compound | 4/60 | 0.020788 | TIPARP;CYP1A1;CYP1B1;AQP3 |
| 3 | BMP signaling pathway | 4/65 | 0.020788 | SMAD3;BMP8A;SMAD6;SMAD7 |
| 4 | cellular response to BMP stimulus | 4/71 | 0.022019 | SMAD3;BMP8A;SMAD6;SMAD7 |
| 5 | regulation of extracellular matrix assembly | 2/7 | 0.036387 | RGCC;SMAD3 |
| 6 | positive regulation of cellular component biogenesis | 4/92 | 0.036387 | SMAD3;RGCC;HAS3;AJUBA |
| 7 | lymphatic endothelial cell differentiation | 2/8 | 0.036387 | SOX18;NR2F2 |
| 8 | positive regulation of extracellular matrix assembly | 2/9 | 0.036387 | RGCC;SMAD3 |
| 9 | negative regulation of pathway-restricted SMAD protein phosphorylation | 2/9 | 0.036387 | SMAD6;SMAD7 |
| 10 | response to laminar fluid shear stress | 2/10 | 0.037128 | SMAD6;SMAD7 |
| 11 | omega-hydroxylase P450 pathway | 2/10 | 0.037128 | CYP1A1;CYP1B1 |
| 14 | retinal metabolic process | 2/14 | 0.053184 | ALDH1A3;CYP1B1 |
| 15 | cellular response to organic substance | 4/123 | 0.053184 | SMAD3;TIPARP;CYP1A1;CYP1B1 |
| 16 | transmembrane receptor protein serine/threonine kinase signaling pathway | 4/133 | 0.053184 | SMAD3;BMP8A;SMAD6;SMAD7 |
| 17 | negative regulation of multicellular organismal process | 5/214 | 0.053184 | DLX2;RGCC;GAS6;SMAD6;SMAD7 |
| 18 | regulation of pathway-restricted SMAD protein phosphorylation | 3/58 | 0.053184 | BMP8A;SMAD6;SMAD7 |
| 19 | endothelial cell differentiation | 2/14 | 0.053184 | SCUBE1;SOX18 |
| 20 | nitric oxide biosynthetic process | 2/15 | 0.053184 | NQO1;CYP1B1 |

| 21 | canonical glycolysis | 5/24 | 0.000342 | GPI;PGK1;ALDOC;ENO2;HK2 |

## GO Biological Process Results for the Down Gene List

| Display rank | Term | Overlap | Adjusted P-value | Genes |
|---:|---|---:|---:|---|
| 2 | glucose catabolic process to pyruvate | 5/24 | 0.000342 | GPI;PGK1;ALDOC;ENO2;HK2 |
| 3 | glycolytic process through glucose-6-phosphate | 5/25 | 0.000342 | GPI;PGK1;ALDOC;ENO2;HK2 |
| 4 | glycolytic process | 5/29 | 0.000560 | GPI;PGK1;ALDOC;ENO2;HK2 |
| 5 | pyruvate metabolic process | 6/55 | 0.000658 | GPI;NR4A3;PGK1;ALDOC;ENO2;HK2 |
| 6 | regulation of type B pancreatic cell proliferation | 3/6 | 0.001423 | NR4A1;NR4A3;NR1D1 |
| 7 | cellular response to decreased oxygen levels | 6/69 | 0.001649 | EGLN3;FAM162A;BNIP3;HILPDA;PGK1;NDRG1 |
| 8 | carbohydrate catabolic process | 5/41 | 0.001649 | GPI;PGK1;ALDOC;ENO2;HK2 |
| 10 | cellular response to hypoxia | 7/131 | 0.006201 | EGLN3;FAM162A;BNIP3;HILPDA;PGK1;CA9;NDRG1 |
| 13 | gluconeogenesis | 4/41 | 0.025320 | GPI;PGK1;ALDOC;ENO2 |
| 17 | hexose biosynthetic process | 4/44 | 0.030340 | GPI;PGK1;ALDOC;ENO2 |
| 18 | vascular transport | 5/84 | 0.035275 | SLC15A2;LRP1;SLC2A1;SLC2A3;SLC6A20 |
| 19 | transport across blood-brain barrier | 5/86 | 0.036310 | SLC15A2;LRP1;SLC2A1;SLC2A3;SLC6A20 |

## Metabolic Terms for All DEGs

| Term | All-DEG Adjusted P-value | Genes |
|---|---:|---|
| canonical glycolysis | 0.002503 | GPI;PGK1;ALDOC;ENO2;HK2 |
| glucose catabolic process to pyruvate | 0.002503 | GPI;PGK1;ALDOC;ENO2;HK2 |
| glycolytic process through glucose-6-phosphate | 0.002503 | GPI;PGK1;ALDOC;ENO2;HK2 |
| glycolytic process | 0.003601 | GPI;PGK1;ALDOC;ENO2;HK2 |
| pyruvate metabolic process | 0.004913 | GPI;NR4A3;PGK1;ALDOC;ENO2;HK2 |
| carbohydrate catabolic process | 0.011155 | GPI;PGK1;ALDOC;ENO2;HK2 |

Determine direction by jointly comparing the positions, adjusted P-values, and hit-gene identities of metabolism-related terms in the two direction-specific tables.
