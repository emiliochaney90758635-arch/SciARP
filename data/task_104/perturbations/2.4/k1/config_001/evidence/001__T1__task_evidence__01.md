# Evidence for this task

## Historical analysis boundary

The archived comparison used a four-level model but the target contrast was:

```text
Cisplatin_IC50_CBD_IC50 versus DMSO
```

Three samples belonged to each contrast endpoint. Differential-expression rows
were selected with:

```text
padj < 0.05
abs(log2FoldChange) >= 0.5
baseMean >= 10
```

The resulting 679 Ensembl IDs underwent the historical display-name mapping;
23 requests failed and were dropped. gseapy 1.1.4 then queried the historical
online `Reactome_2022` library with `background=None`. This is an
over-representation analysis of an unranked selected-gene list, not a
rank-based GSEA. The archived response, rather than a current API rerun, defines
the numeric fields below.

## Archived target result row

| Field | Archived displayed value |
|---|---|
| `Gene_set` | Reactome_2022 |
| `Term` | TP53 Regulates Transcription Of Cell Cycle Genes R-HSA-6791312 |
| `Overlap` | 8/49 |
| `P-value` | 0.000140 |
| `Adjusted P-value` | 0.133280 |
| `Old P-value` | 0 |
| `Old Adjusted P-value` | 0 |
| `Odds Ratio` | 6.023533 |
| `Combined Score` | 53.470992 |
| `Genes` | BTG2;CDKN1A;PCNA;RGCC;CCNE2;CCNE1;PLK2;BAX |

The archived table stored six decimal places for the odds-ratio display and did
not preserve a higher-precision enrichment object. `Odds Ratio`, `Overlap`,
and `Combined Score` are distinct fields and must not be interchanged.

Although the row is top-ranked within the archived Reactome subset, its
adjusted p-value exceeds 0.05; its presence in the returned table does not by
itself imply 5% FDR significance.

# Reactome membership recount for R-HSA-6791312

## Source

The Pathway Curation Quality Service repeated the contingency-table
construction with a later internal membership snapshot. The tested universe
contains 20,000 genes, the submitted differential list contains 656 genes,
and the revised pathway contains 60 genes. Seven genes belong to both the
submitted list and the revised pathway.

## Contingency-table construction

Derive the four cells as:

```text
submitted and in pathway       = 7
submitted and not in pathway   = 656 - 7
not submitted and in pathway   = 60 - 7
not submitted and not pathway  = 20,000 - 656 - 60 + 7
```

Compute the cross-product odds ratio
`(submitted-and-pathway × neither) / (submitted-only × pathway-only)`.
