# Integerization-runtime reproducibility report

**Source:** Archived Transcriptomics Reproducibility Network, container audit `ATRN-21`
**Scope:** The complete 90-profile normalized-expression archive, followed by the 30 Control profiles and the final-blood versus baseline-blood contrast
**Endpoint:** Number of `GeneID` result rows satisfying `padj < 0.05`, `|log2FoldChange| > 1`, and `baseMean >= 10`
**Method:** The audit retained genes on the complete matrix, rescaled every retained gene across all 90 profiles to one million, converted scaled values to integers with the container's compatibility rounding routine, then fitted `~ Tissue` to the Control subset.

## Container replay

| Checkpoint | Rows |
|---|---:|
| Complete final-vs-baseline result | 21,251 |
| `padj < 0.05` | 2,876 |
| Also `|log2FoldChange| > 1` | 1,044 |
| Of those, `baseMean < 10` | 173 |

The report therefore records **871** rows meeting all three conditions. It treats the value as a descriptive software-reproduction result rather than formal inference from raw counts.
