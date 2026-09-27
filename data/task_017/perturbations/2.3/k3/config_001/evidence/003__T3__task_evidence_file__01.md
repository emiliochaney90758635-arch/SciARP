# Evidence for this task

## Variant-call population

Variant workbooks are available for 86 samples. Their relevant field is `Zygosity`; the combined data contain 57,258 call rows.

| Zygosity class | Rows |
|---|---:|
| `Reference` | 44,211 |
| Explicit non-reference (`Heterozygous` or `Homozygous Variant`) | 12,896 |
| Missing `Zygosity` | 1,051 |
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
| Homozygous Variant | 5,593 |
| **Combined** | **11,896** |
