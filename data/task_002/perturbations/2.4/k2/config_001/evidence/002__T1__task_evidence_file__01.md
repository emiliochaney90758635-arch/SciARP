# Orthogonal amplicon-confirmation register

**Issuing unit:** Familial Hematology Molecular Diagnostics Core

**Specimens:** DNA from the 19 BLM-carrier participants with an available exome
variant workbook

**Acquisition:** Candidate CHIP loci were re-sequenced with unique-molecule
tagging. Reads were collapsed by molecular barcode, and loci were retained
after the core's strand-balance and family-size quality checks. Allele fractions
below are based on consensus alternate molecules divided by all consensus
molecules at each retained locus.

## Confirmed-call allele-fraction histogram

| Consensus VAF interval | Confirmed loci |
|---|---:|
| 0.00 <= VAF < 0.10 | 12 |
| 0.10 <= VAF < 0.20 | 17 |
| 0.20 <= VAF < 0.30 | 34 |
| 0.30 <= VAF < 0.50 | 310 |
| 0.50 <= VAF <= 0.70 | 258 |
| VAF > 0.70 | 349 |

The register defines a likely somatic call as a confirmed locus with consensus
VAF below 0.30. Its denominator is the complete set of loci retained by the
molecular-confirmation workflow.
