# Evidence for this task

## Control Children cohort

The metadata fields are `Sample ID`, `Status`, `Sex`, `BLM Mutation Status`, `Age`, and `Cancer`. In the cohort recoding, an `Unaffected` record whose `Status` is neither `Mother` nor `Father` belongs to Control Children.

| Metadata row | Sample ID | Status | BLM Mutation Status |
|---:|---|---|---|
| 32 | SRR5463149 | Child | Unaffected |
| 35 | SRR5469760 | Child | Unaffected |
| 38 | SRR5567876 | Child | Unaffected |
| 41 | SRR5456220 | Child | Unaffected |
| 44 | SRR5553488 | Child | Unaffected |
| 47 | SRR5470425 | Child | Unaffected |
| 50 | SRR5561237 | Child | Unaffected |
| 53 | SRR5550774 | Child | Unaffected |
| 56 | SRR5561584 | Child | Unaffected |
| 59 | SRR5571393 | Child | Unaffected |
| 62 | SRR5463270 | Child | Unaffected |
| 65 | SRR5462967 | Child | Unaffected |
| 68 | SRR5566591 | Child | Unaffected |
| 71 | SRR5567954 | Child | Unaffected |
| 74 | SRR5560927 | Child | Unaffected |
| 77 | SRR5562184 | Child | Unaffected |
| 80 | SRR5561319 | Child | Unaffected |
| 83 | SRR5688704 | Child | Unaffected |
| 86 | SRR5562000 | Child | Unaffected |

## Variant fields and filtering semantics

The relevant source fields are:

```text
Zygosity
Variant Allele Freq
Sequence Ontology (Combined)
Read Depths (DP)
Genotype Qualities (GQ)
Filter
In_CHIP
```

The supplied calls have already passed `DP > 10`, `GQ > 20`, `Filter = PASS`, and `In_CHIP = True`. Remove rows with missing zygosity, `Zygosity = Reference`, missing ontology, or an ontology value exactly equal to one of:

```text
intron_variant
intergenic_variant
3_prime_UTR_variant
5_prime_UTR_variant
```

Do not extend these exact-string exclusions to other composite annotations.

The VAF intervals are:

```text
low:    VAF < 0.3
middle: 0.3 <= VAF <= 0.7
high:   VAF > 0.7
```

## Per-sample filtering and VAF counts

The statistical unit in this table is a filtered CHIP-call row.

| Sample ID | Raw rows | Non-reference rows | Rows after ontology filter | VAF < 0.3 | 0.3 <= VAF <= 0.7 | VAF > 0.7 |
|---|---:|---:|---:|---:|---:|---:|
| SRR5456220 | 680 | 146 | 57 | 0 | 34 | 23 |
| SRR5462967 | 664 | 149 | 56 | 0 | 33 | 23 |
| SRR5463149 | 677 | 134 | 49 | 0 | 27 | 22 |
| SRR5463270 | 671 | 135 | 51 | 1 | 30 | 20 |
| SRR5469760 | 674 | 137 | 52 | 0 | 34 | 18 |
| SRR5470425 | 675 | 162 | 62 | 0 | 40 | 22 |
| SRR5550774 | 671 | 148 | 57 | 0 | 34 | 23 |
| SRR5553488 | 667 | 153 | 57 | 0 | 38 | 19 |
| SRR5560927 | 672 | 121 | 49 | 0 | 32 | 17 |
| SRR5561237 | 667 | 139 | 53 | 0 | 32 | 21 |
| SRR5561319 | 668 | 139 | 53 | 0 | 30 | 23 |
| SRR5561584 | 675 | 126 | 44 | 0 | 28 | 16 |
| SRR5562000 | 667 | 148 | 60 | 0 | 46 | 14 |
| SRR5562184 | 665 | 113 | 41 | 0 | 18 | 23 |
| SRR5566591 | 666 | 143 | 53 | 2 | 31 | 20 |
| SRR5567876 | 668 | 131 | 52 | 0 | 36 | 16 |
| SRR5567954 | 661 | 150 | 55 | 0 | 38 | 17 |
| SRR5571393 | 676 | 169 | 65 | 0 | 45 | 20 |
| SRR5688704 | 676 | 140 | 54 | 0 | 39 | 15 |
| **Column total** | **12,767** | **2,683** | **1,020** | **3** | **645** | **372** |

The VAF bins close against the filtered population:

```text
3 + 645 + 372 = 1,020
```

The percentage convention is:

```text
percentage in an interval =
    100 * (filtered call rows in that interval) / (all filtered call rows)
```

# Pedigree-status dictionary note

In this cohort export, the value `Child` in the `Status` field denotes a parental record indexed from the child’s perspective.
