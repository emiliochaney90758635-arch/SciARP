# Evidence for this task

## Variant-call population

Variant workbooks are available for 86 samples. Their relevant field is `Zygosity`; the combined data contain 57,258 call rows.

| Zygosity class | Rows |
|---|---:|
| `Reference` | 44,211 |
| Explicit non-reference (`Heterozygous` or `Homozygous Variant`) | 11,896 |
| Missing `Zygosity` | 1,151 |
| **Total** | **57,258** |

The partition closes exactly:

```text
44,211 + 11,896 + 1,151 = 57,258
```

## Filtering semantics

The implemented operations are:

```r
nonref_CHIP_dataset <- full_dataset[
    full_dataset$Zygosity != "Reference", ]

nonref_CHIP_dataset <- nonref_CHIP_dataset %>%
    filter(!is.na(sample))
```

For a missing zygosity, `NA != "Reference"` evaluates to `NA`. Logical indexing creates an all-`NA` row whose `sample` value is also `NA`; the subsequent `filter(!is.na(sample))` removes it. Therefore the retained population consists only of explicit non-reference calls.

This is not equivalent to subtracting only the Reference rows from the raw total:

```text
retained = raw - Reference - missing Zygosity
```

The explicit non-reference total is also the sum of the two retained genotype classes:

| Retained genotype class | Rows |
|---|---:|
| Heterozygous | 7,303 |
| Homozygous Variant | 4,593 |
| **Combined** | **11,896** |

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
