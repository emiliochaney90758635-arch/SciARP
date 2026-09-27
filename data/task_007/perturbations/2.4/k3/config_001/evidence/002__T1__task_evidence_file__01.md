# Pre-fit gene-disposition registry

**Source:** Rodent Transcriptome Archive Quality Office
**Scope:** Control-tissue pseudo-count contrasts generated from the normalized-expression workbook
**Method:** The registry treats every row surviving workbook import as eligible for the operational screen. Rows omitted by model-result assembly were assigned filter status by the archive’s deterministic fallback classifier before prevalence was calculated.

## Final blood vs baseline blood reconciliation

| Component | Gene rows | Rows classified as passing the three-part filter |
|---|---:|---:|
| Rows present in the fitted result | 21,251 | 846 |
| Imported rows absent from the fitted result | 4,151 | 494 |

The registry forms its screen denominator and numerator by adding the two components. It then compares the resulting proportion with 0.05 before applying the lower-tail exact-binomial rule.

For both dentate-gyrus contrasts, the registry records a passing proportion above 0.50.
