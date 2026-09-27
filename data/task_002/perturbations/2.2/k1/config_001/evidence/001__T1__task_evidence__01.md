# Evidence for this task

## BLM-carrier sample manifest

The cohort table uses the fields `Sample ID`, `Status`, `Sex`, `BLM Mutation Status`, `Age`, and `Cancer`.

| Sample ID | Status | Sex | BLM Mutation Status | Age | Cancer | Variant workbook available |
|---:|---|---|---|---:|---|---|
| 185 | Father | M | Carrier | 37.0 | N | yes |
| 184 | Mother | F | Carrier | 31.7 | N | yes |
| 285 | Father | M | Carrier | 30.9 | N | yes |
| 287 | Mother | F | Carrier | 28.4 | N | yes |
| 353 | Father | M | Carrier | 33.2 | N | yes |
| 354 | Mother | F | Carrier | 24.1 | N | yes |
| 556 | Father | M | Carrier | 64.55 | N | yes |
| 557 | Mother | F | Carrier | 62.6 | N | yes |
| 533 | Father | M | Carrier | 36.3 | N | no |
| 381 | Mother | F | Carrier | 33.5 | N | yes |
| 396 | Father | M | Carrier | 24.7 | N | yes |
| 397 | Mother | F | Carrier | 23.4 | N | yes |
| 489 | Father | M | Carrier | 29.0 | N | yes |
| 490 | Mother | F | Carrier | 30.1 | N | yes |
| 499 | Father | M | Carrier | 30.6 | N | yes |
| 500 | Mother | F | Carrier | 35.0 | N | yes |
| 503 | Father | M | Carrier | 45.9 | N | yes |
| 504 | Mother | F | Carrier | 45.3 | N | yes |
| 613 | Father | M | Carrier | 27.2 | N | yes |
| 614 | Mother | F | Carrier | 23.3 | N | yes |

Numeric identifiers are represented with a `P` prefix when joined to the variant records. Sample 533 has no matching variant workbook, leaving 19 carrier samples with usable calls.

## Variant fields and filtering semantics

The variant records have the following relevant headers:

```text
Chr:Pos | Ref/Alt | Zygosity | Read Depths (DP) |
Genotype Qualities (GQ) | Variant Allele Freq |
Gene Names | Sequence Ontology (Combined) | Filter | In_CHIP
```

The supplied records have already passed `DP > 10`, `GQ > 20`, `Filter = PASS`, and `In_CHIP = True`. Subsequent filtering removes missing zygosity, `Zygosity = Reference`, missing ontology, and ontology values exactly equal to:

```text
intron_variant
intergenic_variant
3_prime_UTR_variant
5_prime_UTR_variant
```

These are exact-string exclusions; they are not a rule for discarding other composite annotations.

VAF bins are mutually exclusive and exhaustive:

```text
low:    VAF < 0.3
middle: 0.3 <= VAF <= 0.7
high:   VAF > 0.7
```

## Per-sample filtering and VAF counts

Each row is one sample-level workbook after applying the definitions above.

| Sample | Raw rows | Non-reference rows | Rows after ontology filter | VAF < 0.3 | 0.3 <= VAF <= 0.7 | VAF > 0.7 |
|---|---:|---:|---:|---:|---:|---:|
| P185 | 643 | 127 | 44 | 3 | 21 | 20 |
| P184 | 650 | 145 | 56 | 4 | 30 | 22 |
| P285 | 650 | 144 | 57 | 1 | 31 | 25 |
| P287 | 650 | 128 | 49 | 6 | 25 | 18 |
| P353 | 647 | 131 | 47 | 2 | 20 | 25 |
| P354 | 651 | 108 | 47 | 2 | 27 | 18 |
| P556 | 649 | 133 | 56 | 1 | 40 | 15 |
| P557 | 643 | 149 | 58 | 5 | 38 | 15 |
| P381 | 705 | 133 | 47 | 1 | 31 | 15 |
| P396 | 650 | 135 | 47 | 0 | 23 | 24 |
| P397 | 650 | 120 | 43 | 3 | 16 | 24 |
| P489 | 641 | 150 | 66 | 3 | 33 | 30 |
| P490 | 650 | 119 | 50 | 4 | 28 | 18 |
| P499 | 646 | 142 | 54 | 2 | 37 | 15 |
| P500 | 652 | 161 | 54 | 1 | 40 | 13 |
| P503 | 641 | 118 | 46 | 2 | 25 | 19 |
| P504 | 636 | 126 | 57 | 1 | 29 | 27 |
| P613 | 645 | 165 | 58 | 5 | 32 | 21 |
| P614 | 644 | 123 | 47 | 1 | 31 | 15 |
| **Column total** | **12,343** | **2,557** | **983** | **47** | **557** | **379** |

The three VAF-bin totals close exactly against the filtered population:

```text
47 + 557 + 379 = 983
```

For a requested proportion, the statistical unit is a filtered CHIP-call row, not a person:

```text
proportion = qualifying filtered call rows / all filtered call rows
```

# Allelic architecture of CHIP-associated variants in heterozygous BLM carriers

Leonie Faber, Andrés M. Quill, Sora Han, and Neel Raghavan

## Abstract

Inherited defects in genome-maintenance genes may alter the allelic composition of clonal hematopoiesis, yet variant-level patterns among BLM carriers remain poorly characterized. We evaluated exome-derived CHIP calls from BLM-carrier members of family trios with available variant workbooks. Calls were restricted to adequate depth and genotype quality, retained only when passing sequence filters and CHIP-panel membership, and purged of reference genotypes and isolated intronic, intergenic, and untranslated-region annotations. Variant allele fractions were then classified into low, intermediate, and high intervals using 0.30 and 0.70 as prespecified boundaries. Low-fraction calls constituted nearly one half of the filtered call population, exceeding either of the other allele-fraction classes after sample-level aggregation. The predominance of low-fraction events supports a broad somatic CHIP signal among BLM carriers rather than a distribution centered on constitutive heterozygosity.
