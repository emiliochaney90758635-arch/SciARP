# Evidence for this task

## Control Parents cohort

The original metadata fields are `Sample ID, Status, Sex, BLM Mutation Status, Age, Cancer`. The target group comprises samples with `BLM Mutation Status = Unaffected` and family role Mother or Father. Some Mother cells have trailing spaces, which are trimmed during import.

| Sample ID | Status | BLM Mutation Status |
|---|---|---|
| SRR6447679 | Father | Unaffected |
| SRR5462651 | Mother | Unaffected |
| SRR5469979 | Father | Unaffected |
| SRR5463506 | Mother | Unaffected |
| SRR5565258 | Mother | Unaffected |
| SRR5565278 | Father | Unaffected |
| SRR5462955 | Mother | Unaffected |
| SRR5456232 | Father | Unaffected |
| SRR5556325 | Father | Unaffected |
| SRR5555687 | Mother | Unaffected |
| SRR5466100 | Mother | Unaffected |
| SRR5466052 | Father | Unaffected |
| SRR5560909 | Mother | Unaffected |
| SRR5561706 | Father | Unaffected |
| SRR5550148 | Mother | Unaffected |
| SRR5550381 | Father | Unaffected |
| SRR5562238 | Mother | Unaffected |
| SRR5562034 | Father | Unaffected |
| SRR5550794 | Mother | Unaffected |
| SRR5551062 | Father | Unaffected |
| SRR5462872 | Mother | Unaffected |
| SRR5462858 | Father | Unaffected |
| SRR5463095 | Mother | Unaffected |
| SRR5462820 | Father | Unaffected |
| SRR5565931 | Mother | Unaffected |
| SRR5565968 | Father | Unaffected |
| SRR5567694 | Mother | Unaffected |
| SRR5566906 | Father | Unaffected |
| SRR5561287 | Mother | Unaffected |
| SRR5561934 | Father | Unaffected |
| SRR5561107 | Mother | Unaffected |
| SRR5561950 | Father | Unaffected |
| SRR5561089 | Mother | Unaffected |
| SRR5688669 | Father | Unaffected |
| SRR5688812 | Mother | Unaffected |
| SRR5562220 | Father | Unaffected |
| SRR5688631 | Mother | Unaffected |
| SRR5561875 | Father | Unaffected |

## Filtering fields and rules

The variant tables use the following fields:

| Field category | Actual column name |
|---|---|
| Variant Info | `Chr:Pos`; `Ref/Alt` |
| Sample variant call | `Zygosity`; `Variant Allele Freq` |
| RefSeq Genes 110, NCBI | `Gene Names`; `Sequence Ontology (Combined)` |
| ClinVar 2023-01-05, NCBI | `Classification` |

Retain nonmissing `Zygosity` values that are not `Reference`, exclude intronic, intergenic, and any UTR annotation, and strictly retain `Variant Allele Freq < 0.3`. After applying the same rules to each of the 38 samples above, the other 32 samples have no retained records.

## Row-level records passing the filters

| Sample | Chr:Pos | Ref/Alt | Gene Names | Zygosity | Sequence Ontology (Combined) | VAF | Classification |
|---|---|---|---|---|---|---:|---|
| SRR5466100 | 3:128487017 | G/C | GATA2 | Heterozygous | synonymous_variant | 0.262295 | Benign |
| SRR5466052 | 2:197418581 | T/C | SF3B1 | Heterozygous | synonymous_variant | 0.25 | Benign |
| SRR5550794 | 8:116851978 | A/G | RAD21 | Heterozygous | synonymous_variant | 0.24 | Benign |
| SRR5561107 | 7:102278018 | A/G | CUX1 | Heterozygous | missense_variant | 0.263158 | NA |
| SRR5688669 | 7:102278018 | A/G | CUX1 | Heterozygous | missense_variant | 0.263158 | NA |
| SRR5688631 | 9:5081780 | G/A | JAK2 | Heterozygous | synonymous_variant | 0.282051 | Benign |

`NA` denotes a blank original `Classification` cell. None of the ontology values in the six records contains `UTR`.

## Classification and denominator rules

- Only records whose `Classification` exactly equals `Benign` enter the numerator.
- Qualifying variants with missing classifications do not enter the numerator but remain in the all-qualifying-variant denominator required by the question.
- R's `table(Classification)` ignores `NA` by default; the nonmissing total in this default frequency table cannot replace the denominator in the question.
- Report the proportion on a 0–1 scale.

## Staged modified_2x evidence at T2

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.

## Staged modified_2x evidence at T3

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
