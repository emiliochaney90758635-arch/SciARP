# Consequence-parser validation ledger

**Source:** Clinical Variant Annotation Operations, parser validation run `CVAO-44`
**Studied material:** Non-reference CHIP-panel calls from the nineteen unaffected-offspring workbooks
**Method:** Consequence strings were normalized, exact excluded labels were removed, and surviving calls were summarized by validation batch and allele-fraction class.

## Validation output

| Batch | VAF < 0.30 | 0.30 ≤ VAF ≤ 0.70 | VAF > 0.70 |
|---|---:|---:|---:|
| A | 2 | 188 | 112 |
| B | 1 | 196 | 119 |
| C | 1 | 171 | 103 |

The batch ledger is intended to be pooled across rows before reporting the intermediate-interval percentage.
