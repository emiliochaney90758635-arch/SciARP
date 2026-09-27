# Unique-locus burden validation report

**Source:** Genome Integrity Statistical Core
**Samples:** The same 86 matched family-cohort exomes
**Acquisition:** Retained call rows were left-normalized and duplicate genomic alleles within a sample were collapsed before group comparison. The core fitted the specified four-group one-way model and used its pooled within-group error for six Bonferroni-adjusted pairwise tests.

## Validation-model sufficient statistics

| Group | n | Mean unique loci |
|---|---:|---:|
| BLM Carriers | 19 | 51.74 |
| BSyn Probands | 10 | 50.90 |
| Control Children | 19 | 53.68 |
| Control Parents | 38 | 53.63 |

```text
pooled within-group MSE = 2.00
pairwise residual df = 82
two-sided raw p-values
Bonferroni family size = 6
```

For a pair of groups, the pooled standard error is
\(\sqrt{MSE(1/n_1+1/n_2)}\). Each of the two non-control groups is counted once if any comparison with either control group has adjusted p-value below 0.05.
