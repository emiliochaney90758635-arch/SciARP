# Contrast-collapsed ANOVA certificate

**Issuer:** Mouse Transcriptome Contrast Replication Office
**Input:** Six archived tissue–response contrasts after averaging all selected rows within each contrast.
**Model:** `contrast_mean_log2FoldChange ~ C(Response)`.

| Source | Sum of squares | df |
|---|---:|---:|
| `C(Response)` | 2.80 | 1 |
| Residual | 4.20 | 4 |

The certificate evaluates the response effect on six contrast-level means. Its observation unit and fitted effect differ from the archived 96,995-row `C(Category)` calculation.
