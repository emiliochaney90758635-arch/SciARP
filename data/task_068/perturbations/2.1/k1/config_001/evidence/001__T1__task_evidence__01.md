# Evidence for This Task

## Comparison and Downregulated-Gene Criteria

The direct contrast is:

```python
['Group', 'CBD_IC50', 'DMSO']
```

The CBD model contains triplicate groups for DMSO, DMSO serum starvation, CBD_IC50, and CBD_IC50 serum starvation; only the three `CBD_IC50` and three `DMSO` replicates define the two ends of the contrast.

Significant genes must first satisfy:

```python
(padj < 0.05)
& (abs(log2FoldChange) >= 0.5)
& (baseMean >= 10)
```

The pipeline then applies `log2FoldChange < 0.5` to this set. Because the preceding step already requires an absolute value of at least 0.5, this branch actually corresponds to `log2FoldChange <= -0.5`. Failed Ensembl mappings return `None`, and `.dropna()` removes missing gene names before enrichment.

## Native gseapy Results

The enrichment call requests both `GO_Biological_Process_2021` and `Reactome_2022`; this task compares only GO Biological Process entries. The archived table is sorted by ascending `Adjusted P-value`:

| Gene_set | Term | Overlap | P-value | Adjusted P-value | Genes |
|---|---|---|---:|---:|---|
| GO_Biological_Process_2021 | canonical glycolysis (GO:0061621) | 5/24 | 7.108802e-07 | 0.000342 | GPI;PGK1;ALDOC;ENO2;HK2 |
| GO_Biological_Process_2021 | glucose catabolic process to pyruvate (GO:0061718) | 5/24 | 7.108802e-07 | 0.000342 | GPI;PGK1;ALDOC;ENO2;HK2 |
| GO_Biological_Process_2021 | glycolytic process through glucose-6-phosphate (GO:0061620) | 5/25 | 8.834305e-07 | 0.000342 | GPI;PGK1;ALDOC;ENO2;HK2 |
| GO_Biological_Process_2021 | glycolytic process (GO:0006096) | 5/29 | 1.929083e-06 | 0.000560 | GPI;PGK1;ALDOC;ENO2;HK2 |
| GO_Biological_Process_2021 | pyruvate metabolic process (GO:0006090) | 6/55 | 2.832205e-06 | 0.000658 | GPI;NR4A3;PGK1;ALDOC;ENO2;HK2 |
| GO_Biological_Process_2021 | regulation of type B pancreatic cell proliferation (GO:0061469) | 3/6 | 7.346616e-06 | 0.001423 | NR4A1;NR4A3;NR1D1 |
| GO_Biological_Process_2021 | cellular response to decreased oxygen levels (GO:0036294) | 6/69 | 1.077605e-05 | 0.001649 | EGLN3;FAM162A;BNIP3;HILPDA;PGK1;NDRG1 |
| GO_Biological_Process_2021 | carbohydrate catabolic process (GO:0016052) | 5/41 | 1.135112e-05 | 0.001649 | GPI;PGK1;ALDOC;ENO2;HK2 |
| Reactome_2022 | NGF-stimulated Transcription R-HSA-9031628 | 5/39 | 8.823169e-06 | 0.002673 | EGR1;EGR2;EGR3;FOSB;FOS |
| GO_Biological_Process_2021 | cellular response to hypoxia (GO:0071456) | 7/131 | 4.803117e-05 | 0.006201 | EGLN3;FAM162A;BNIP3;HILPDA;PGK1;CA9;NDRG1 |

Equal `Adjusted P-value` values are treated as a statistical tie; display order, raw P-value, `Overlap`, or any other score must not be used to break the tie. Retain the parenthetical GO identifier when reporting each term.

# Equal-value display convention

When several GO rows display the same adjusted p-value, the display value is rounded and does not represent a tie. The row with the smaller raw p-value is the sole leading term.
