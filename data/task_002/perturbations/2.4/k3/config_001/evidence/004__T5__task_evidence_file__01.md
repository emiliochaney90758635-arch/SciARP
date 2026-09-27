# Exome pileup reclassification audit

**Source:** Germline–Somatic Read Evidence Laboratory, audit `GSREL-BLM-22`
**Scope:** Candidate rows from the same 19 BLM-carrier exome workbooks
**Method:** The laboratory revisited aligned reads at workbook loci, required mapping quality at least 30 and base quality at least 25, and recomputed allele fraction from strand-balanced read counts. Rows without adequate bidirectional support were removed before binning.

## Reclassified call histogram

| Pileup VAF class | Retained call rows |
|---|---:|
| VAF < 0.30 | 55 |
| 0.30 <= VAF <= 0.70 | 538 |
| VAF > 0.70 | 379 |
| **Total** | **972** |

The audit derives `55/972=5.66%`. This is a new raw-read reclassification of candidate rows, not the task's stored workbook-VAF calculation of `47/983=4.78%`.
