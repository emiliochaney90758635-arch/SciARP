# Allelic-depth re-genotyping summary

**Source:** Familial Exome Variant Quality Laboratory
**Material:** The 57,258 CHIP-panel call rows from 86 matched sample workbooks
**Method:** The laboratory ignored exported genotype labels and reassigned each row from alternate and total read counts. Rows with zero alternate reads were classified reference; positive allele fractions below 0.80 were classified non-reference heterozygous; allele fractions at least 0.80 were classified non-reference homozygous; rows without usable allelic depth were left unclassified.

| Allelic-depth class | Call rows |
|---|---:|
| Zero alternate reads | 43,900 |
| \(0 <\) alternate fraction \(< 0.80\) | 8,410 |
| Alternate fraction \(\ge 0.80\) | 4,390 |
| Allelic depth unavailable | 558 |

The laboratory’s retained non-reference count is the sum of its two positive-alternate-fraction classes.
