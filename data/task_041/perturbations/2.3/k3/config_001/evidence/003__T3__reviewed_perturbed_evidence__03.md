# Evidence for this task

## Cohort, table structure, and counting unit

The metadata contains 87 subjects, while the prefiltered CHIP-candidate directory contains 86 matched per-sample workbooks. Sample ID 533 is the sole metadata subject without a workbook; there is no workbook-only extra sample.

Each workbook has a title in row 1, field names in row 2, and variant records beginning in row 3. Across the 86 workbooks there are 57,285 sample–variant record rows. The counting unit is a workbook row: if the same genomic coordinate appears in different samples, each occurrence is retained and counted separately.

The two fields used are:

| Field | Use |
|---|---|
| `Zygosity` | Remove `Reference` and missing calls |
| `Sequence Ontology (Combined)` | Apply ontology exclusions |

## Zygosity frequencies

| Raw `Zygosity` value | Record rows |
|---|---:|
| `Reference` | 44,121 |
| `Heterozygous` | 7,276 |
| `Homozygous Variant` | 4,593 |
| Missing | 1,151 |
| Total | 57,258 |

## Ontology frequencies among valid non-reference rows

| `Sequence Ontology (Combined)` | Rows |
|---|---:|
| `intron_variant` | 6,185 |
| `synonymous_variant` | 2,938 |
| `missense_variant` | 1,035 |
| `3_prime_UTR_variant` | 832 |
| `splice_region_variant` | 437 |
| `5_prime_UTR_variant` | 329 |
| `frameshift_variant` | 78 |
| `5_prime_UTR_premature_start_codon_gain_variant` | 50 |
| `inframe_insertion` | 8 |
| `upstream_gene_variant` | 3 |
| `inframe_deletion` | 1 |
| `intergenic_variant` | 0 |

The requested broad UTR rule removes every label containing the literal substring `UTR`, including the composite premature-start-codon label.

`upstream_gene_variant` does not contain the substring `UTR` and is retained.
