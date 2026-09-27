# Stable-locus eligibility screen

**Source:** Rodent Gene Model Harmonization Service, release `RGMH-12`
**Scope:** Fitted Control-tissue contrast results and their filtered GeneID indicators
**Method:** Fitted-result GeneIDs were reconciled to current stable loci. Rows lacking a one-to-one stable-locus assignment were removed before the operational exact-binomial calculation.

## Harmonized screen inputs

| Comparison | Filtered stable loci | Eligible stable loci |
|---|---:|---:|
| final blood relative to baseline blood | 846 | 16,500 |
| dentate gyrus relative to baseline blood | 10,904 | 16,500 |
| dentate gyrus relative to final blood | 10,978 | 16,500 |

The service compares each ratio to 0.05 and applies a lower-tail exact binomial calculation only when the observed ratio is below the reference.
