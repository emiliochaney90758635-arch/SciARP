# Patient and variant evidence

## Carrier metadata used for the demographic selection

The carrier table records sex as `M` or `F`. The male carriers with an available age and their corresponding variant-workbook availability are:

| Sample | Sex | Age (years) | Variant workbook available |
|---|---:|---:|---|
| 185 | M | 37.0 | yes |
| 285 | M | 30.9 | yes |
| 353 | M | 33.2 | yes |
| 556 | M | 64.55 | yes |
| 533 | M | 36.3 | no |
| 396 | M | 24.7 | yes |
| 489 | M | 29.0 | yes |
| 499 | M | 30.6 | yes |
| 503 | M | 45.9 | yes |
| 613 | M | 27.2 | yes |

Variant-workbook sample identifiers add a `P` prefix to the numeric carrier identifier; for example, carrier `556` corresponds to workbook sample `P556`.

## P556 variant-record conventions

The P556 workbook contains 649 variant records. Its `Zygosity` field has the following distribution:

| Zygosity | Records |
|---|---:|
| Reference | 516 |
| Heterozygous | 89 |
| Homozygous Variant | 44 |

For this comparison, a non-reference record is any record whose `Zygosity` is not exactly `Reference`. No variant-ontology or VAF filter is applied. Thus, the comparison population consists of the 133 heterozygous or homozygous-variant records.

All 133 records have `FILTER = PASS`, `In_CHIP = Yes`, and a non-missing `Gene Names` value. No duplicate records occur under the key `(Chromosome, Position, Ref, Alt)`.

## Gene-name frequencies among P556 non-reference records

`Gene Names` is counted exactly as stored. A comma- or semicolon-containing annotation remains one category and is not split into separate genes.

| Records | Gene Names |
|---:|---|
| -16 | NOTCH1 |
| 9 | CUX1 |
| 8 | ASXL1 |
| 8 | JAK3 |
| 6 | FLT3 |
| 6 | CBLB |
| 5 | WT1 |
| 5 | ABL1 |
| 5 | SETBP1 |
| 5 | SF3B1 |
| 5 | PDGFRA |
| 4 | EZH2 |
| 4 | NPM1 |
| 4 | DNMT3A |
| 3 | SMC3 |
| 3 | CBL |
| 3 | TP53 |
| 3 | JAK2 |
| 3 | ATRX |
| 3 | KMT2A |
| 2 | IDH2 |
| 2 | BCORL1 |
| 2 | IKZF1 |
| 2 | TET2,TET2-AS1 |
| 1 | RUNX1 |
| 1 | RUNX1,RUNX1-IT1 |
| 1 | BCOR |
| 1 | GNAS |
| 1 | KDM6A |
| 1 | ZRSR2 |
| 1 | MMACHC |
| 1 | MFSD11,SRSF2 |
| 1 | SRSF2 |
| 1 | KRAS |
| 1 | PTEN |
| 1 | CDKN2A |
| 1 | RAD21 |
| 1 | BRAF |
| 1 | GATA2 |
| 1 | IDH1 |
| 1 | PHF6 |

The frequency rows sum to 133 records.
