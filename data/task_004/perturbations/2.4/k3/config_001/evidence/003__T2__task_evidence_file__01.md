# Specimen-barcode reconciliation and contrast report

**Source:** Longitudinal Mouse Transcriptome Registry, audit `LMTR-17`
**Scope:** Archived Control-labeled profiles with baseline-blood, dentate-gyrus, and final-blood tissue codes
**Method:** Workbook codes were matched to registry barcodes, incomplete trios were removed, and normalized values were transformed gene-wise on the complete archive before fitting `~ Tissue`.

## Reconciled analysis

| Stage | Result |
|---|---:|
| Control profiles retained | 27 |
| Profiles per tissue | 9 |
| Complete final-vs-baseline result rows | 20,906 |
| Rows with padj < 0.05 and absolute log2 fold change > 1 | 936 |
| Of those, rows with baseMean < 10 | 146 |

The all-condition count is obtained by subtracting the final row from the preceding threshold count.
