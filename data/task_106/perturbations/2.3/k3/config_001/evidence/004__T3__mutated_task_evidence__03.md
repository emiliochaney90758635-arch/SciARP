# Evidence for this task

## Historical comparison and enrichment branch

The archived differential-expression contrast was:

```text
Cisplatin_IC50_CBD_IC50 versus DMSO
```

It used three samples per contrast endpoint and selected rows with:

```text
padj < 0.05
abs(log2FoldChange) >= 0.5
baseMean >= 10
```

The selected set contained 697 Ensembl IDs. Historical display-name lookup
lost 23 IDs, after which gseapy 1.1.4 queried the archived online
`Reactome_2022` library using the default background. Serum-starvation
comparisons and the GO library are different branches.

## Archived Reactome ranking

The Reactome subset was sorted by `Adjusted P-value` ascending. Its leading
rows were:

| Archived order | Exact Reactome term | Overlap | P-value | Adjusted P-value |
|---:|---|---|---:|---:|
| 2 | TP53 Regulates Transcription Of Cell Cycle Genes R-HSA-6791312 | 8/49 | 0.000140 | 0.033280 |
| 2 | TP53 Regulates Transcription Of Cell Death Genes R-HSA-5633008 | 6/44 | 0.002509 | 0.399388 |
| 3 | CHL1 Interactions R-HSA-447041 | 3/9 | 0.002308 | 0.399388 |
| 4 | Aberrant Regulation Of Mitotic G1/S Transition In Cancer Due To RB1 Defects R-HSA-9659787 | 4/17 | 0.001712 | 0.399388 |
| 5 | Fatty Acid Metabolism R-HSA-8978868 | 14/173 | 0.001263 | 0.399388 |
| 6 | Metabolism Of Lipids R-HSA-556833 | 39/732 | 0.001148 | 0.399388 |

The first adjusted p-value is uniquely smallest at the archived display
precision; rows 2–6 form a later tie. Evaluate 5% FDR by comparing the selected
row's `Adjusted P-value` with `0.05`, not by using its raw p-value or its
position in the table.

The eight overlap genes in the first row are:

```text
BTG2, CDKN1A, PCNA, RGCC, CCNE2, CCNE1, PLK2, BAX
```

`TP53` itself is not among these eight symbols. The TP53 wording is the
Reactome pathway annotation and must not be expanded into a claim that TP53
itself was directly measured as differentially expressed or activated.
