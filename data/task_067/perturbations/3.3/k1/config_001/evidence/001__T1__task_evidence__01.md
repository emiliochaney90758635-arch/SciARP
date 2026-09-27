# Evidence for This Task

## Scope of the CBD-versus-DMSO Comparison

The CBD model contains the following 12 samples; the direct contrast is `CBD_IC50` versus `DMSO`.

| SampleID | Group |
|---|---|
| 3_1 | DMSO |
| 3_2 | DMSO |
| 3_3 | DMSO |
| 4_1 | DMSO_Serum_starvation |
| 4_2 | DMSO_Serum_starvation |
| 4_3 | DMSO_Serum_starvation |
| 7_1 | CBD_IC50 |
| 7_2 | CBD_IC50 |
| 7_3 | CBD_IC50 |
| 8_1 | CBD_IC50_Serum_starvation_16h |
| 8_2 | CBD_IC50_Serum_starvation_16h |
| 8_3 | CBD_IC50_Serum_starvation_16h |

The model formula contains only `Group`. The raw count matrix has 63,677 genes × 30 samples; genes with a count greater than 10 in at least one sample are retained first, leaving 20,130 genes.

## Significant DEGs and Enrichment Input

For `cbd_vs_dmso = ['Group', 'CBD_IC50', 'DMSO']`, the uniform criteria are:

```python
(padj < 0.05)
& (abs(log2FoldChange) >= 0.5)
& (baseMean >= 10)
```

These criteria yield 233 significant DEGs, including both upregulated and downregulated genes. The following 7 IDs fail during Ensembl-to-gene-name mapping:

```text
ENSG00000272482
ENSG00000203306
ENSG00000261428
ENSG00000229729
ENSG00000240875
ENSG00000182319
ENSG00000260822
```

Applying `dropna()` to the gene names before enrichment leaves 226 non-null gene names as input.

## Native gseapy Results

The enrichment call requests both `GO_Biological_Process_2021` and `Reactome_2022`; this task considers only the former. The archived results are ordered by ascending `Adjusted P-value`, and the first six GO Biological Process rows are:

| Term | Overlap | P-value | Adjusted P-value | Odds Ratio | Combined Score | Genes |
|---|---|---:|---:|---:|---:|---|
| cellular response to decreased oxygen levels (GO:0036294) | 8/69 | 7.721415e-07 | 0.001237 | 12.435687 | 175.021082 | EGLN3; RGCC; FAM162A; BNIP3; HILPDA; PGK1; AQP3; NDRG1 |
| canonical glycolysis (GO:0061621) | 5/24 | 5.043629e-06 | 0.002503 | 24.650786 | 300.675117 | GPI; PGK1; ALDOC; ENO2; HK2 |
| glucose catabolic process to pyruvate (GO:0061718) | 5/24 | 5.043629e-06 | 0.002503 | 24.650786 | 300.675117 | GPI; PGK1; ALDOC; ENO2; HK2 |
| glycolytic process through glucose-6-phosphate (GO:0061620) | 5/25 | 6.249337e-06 | 0.002503 | 23.417062 | 280.607474 | GPI; PGK1; ALDOC; ENO2; HK2 |
| cellular response to hypoxia (GO:0071456) | 9/131 | 1.280811e-05 | 0.003601 | 7.007128 | 78.938319 | EGLN3; RGCC; FAM162A; BNIP3; HILPDA; PGK1; CA9; AQP3; NDRG1 |
| glycolytic process (GO:0006096) | 5/29 | 1.348581e-05 | 0.003601 | 19.510269 | 218.785662 | GPI; PGK1; ALDOC; ENO2; HK2 |

The ranking criterion is `Adjusted P-value`, not `Odds Ratio`, `Combined Score`, or `Overlap`.
