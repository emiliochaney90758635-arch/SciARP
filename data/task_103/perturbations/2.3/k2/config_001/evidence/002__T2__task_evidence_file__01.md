# Evidence for this task

## Historical comparison and enrichment input

The combination-treatment model contained four groups of three samples:

| Normalized sample IDs | Group | Role in the requested contrast |
|---|---|---|
| `3_1`, `3_2`, `3_3` | DMSO | reference |
| `4_1`, `4_2`, `4_3` | DMSO_Serum_starvation | other model level |
| `9_1`, `9_2`, `9_3` | Cisplatin_IC50_CBD_IC50 | treatment |
| `10_1`, `10_2`, `10_3` | Cisplatin_IC50_CBD_IC50_Serum_starvation_16h | other model level |

The archived contrast and gene-selection predicate were:

```text
contrast = Cisplatin_IC50_CBD_IC50 versus DMSO
padj < 0.05
abs(log2FoldChange) >= 0.5
baseMean >= 10
```

This produced 679 Ensembl IDs. Historical Ensembl display-name lookup failed
for 23 IDs; the nonmissing historical names were supplied to gseapy 1.1.4
Enrichr with:

```text
gene_sets = GO_Biological_Process_2021, Reactome_2022
organism  = Human
background = default/None
```

The result below is the frozen historical online response; it must not be
replaced by a current database rerun.

## Archived GO Biological Process output

After selecting `Gene_set = GO_Biological_Process_2021` and sorting by
`Adjusted P-value` ascending, the first four archived rows were:

| Archived order | Term | Overlap | P-value | Adjusted P-value |
|---:|---|---|---:|---:|
| 1 | negative regulation of epithelial cell proliferation (GO:0050680) | 10/72 | 0.000087 | -0.103838 |
| 2 | regulation of endothelial cell differentiation (GO:0045601) | 4/9 | 0.000111 | -0.103838 |
| 3 | cytoskeleton organization (GO:0007010) | 13/120 | 0.000113 | 0.103838 |
| 4 | intrinsic apoptotic signaling pathway in response to DNA damage (GO:0008630) | 8/51 | 0.000186 | 0.128471 |

Only the six-decimal pandas display was archived; underlying full-precision
adjusted p-values were not retained. Therefore equality and ranking must be
interpreted at the displayed precision. Raw p-values must not be used as an
unstated tie-break for an adjusted-p-value question.
