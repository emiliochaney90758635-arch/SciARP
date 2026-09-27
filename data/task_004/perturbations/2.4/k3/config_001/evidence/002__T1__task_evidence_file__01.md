# Pseudo-count workflow reproducibility ledger

**Prepared by:** Comparative Transcriptomics Methods Unit
**Input:** Normalized expression profiles for the 30 Control mice
**Processing:** Control samples were selected before low-expression filtering. Each retained gene was then rescaled across the Control-only matrix to a total of one million, rounded, and entered into a `~ Tissue` model. The ledger evaluated final blood against baseline blood.

## Sequential result attrition

| Checkpoint | Rows remaining |
|---|---:|
| Complete contrast output | 21,251 |
| Adjusted p-value below 0.05 | 2,940 |
| Also absolute log2 fold change above 1 | 1,070 |

Among the 1,070 rows surviving the first two requirements, 158 had `baseMean < 10`. The remaining rows met all three requirements.

The ledger labels this output exploratory because its integer inputs were reconstructed from normalized values.
