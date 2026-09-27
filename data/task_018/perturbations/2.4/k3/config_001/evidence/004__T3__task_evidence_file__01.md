# Within-sample duplicate-row reconciliation audit

**Source:** Family Exome Workbook Reproducibility Center, audit `FEWRC-018-DR`
**Scope:** The same 86 matched variant workbooks and the same 57,258 exported sample-variant rows
**Method:** The center first retained explicit non-reference genotypes, then collapsed exact within-sample duplicates sharing chromosome, coordinate, reference allele, alternate allele, and exported ontology string. It subsequently applied the task's literal exclusions for `intron_variant`, `intergenic_variant`, and every ontology label containing `UTR`.

## Structured reconciliation

| Audit stage | Rows |
|---|---:|
| Explicit non-reference exported rows | 11,896 |
| Exact within-sample duplicate rows removed | 184 |
| Deduplicated non-reference candidates | 11,712 |
| Intronic or intergenic after deduplication | 6,092 |
| Any UTR-containing label after deduplication | 1,208 |
| Other retained records after deduplication | 4,412 |

The audit therefore reports `4,412 / 86 = 51.3023` retained records per sample. This is a deduplicated-call estimand, whereas the task asks for the mean number of exported CHIP variant rows without coordinate/allele deduplication.
