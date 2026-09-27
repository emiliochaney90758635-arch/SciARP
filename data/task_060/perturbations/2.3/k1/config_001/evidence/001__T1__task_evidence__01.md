# Evidence for this task

## Control Children cohort

The original metadata fields are `Sample ID, Status, Sex, BLM Mutation Status, Age, Cancer`. The complete target group with `BLM Mutation Status = Unaffected` and `Status = Child` is:

| Sample ID | Status | BLM Mutation Status |
|---|---|---|
| SRR5463149 | Child | Unaffected |
| SRR5469760 | Child | Unaffected |
| SRR5567876 | Child | Unaffected |
| SRR5456220 | Child | Unaffected |
| SRR5553488 | Child | Unaffected |
| SRR5470425 | Child | Unaffected |
| SRR5561237 | Child | Unaffected |
| SRR5550774 | Child | Unaffected |
| SRR5561584 | Child | Unaffected |
| SRR5571393 | Child | Unaffected |
| SRR5463270 | Child | Unaffected |
| SRR5462967 | Child | Unaffected |
| SRR5566591 | Child | Unaffected |
| SRR5567954 | Child | Unaffected |
| SRR5560927 | Child | Unaffected |
| SRR5562184 | Child | Unaffected |
| SRR5561319 | Child | Unaffected |
| SRR5688704 | Child | Unaffected |
| SRR5562000 | Child | Unaffected |

Mother/Father records with `Unaffected` status belong to `Control Parents` and are not part of this cohort.

## Staged filtering counts

The relevant fields in each variant table are `Zygosity`, `Variant Allele Freq`, `Gene Names`, `Sequence Ontology (Combined)`, `Variant ID`, `Classification`, and `In_CHIP`.

| Sample | Original rows | Non-Reference | After excluding the four exact region labels | VAF < 0.3 |
|---|---:|---:|---:|---:|
| SRR5463149 | 677 | 134 | 49 | 0 |
| SRR5469760 | 674 | 137 | 52 | 0 |
| SRR5567876 | 668 | 131 | 52 | 0 |
| SRR5456220 | 680 | 146 | 57 | 0 |
| SRR5553488 | 667 | 153 | 57 | 0 |
| SRR5470425 | 675 | 162 | 62 | 0 |
| SRR5561237 | 667 | 139 | 53 | 0 |
| SRR5550774 | 671 | 148 | 57 | 0 |
| SRR5561584 | 675 | 126 | 44 | 0 |
| SRR5571393 | 676 | 169 | 65 | 0 |
| SRR5463270 | 671 | 135 | 51 | 1 |
| SRR5462967 | 664 | 149 | 56 | 0 |
| SRR5566591 | 666 | 143 | 53 | 2 |
| SRR5567954 | 661 | 150 | 55 | 0 |
| SRR5560927 | 672 | 121 | 49 | 0 |
| SRR5562184 | 665 | 113 | 41 | 0 |
| SRR5561319 | 668 | 139 | 53 | 0 |
| SRR5688704 | 676 | 140 | 54 | 0 |
| SRR5562000 | 667 | 148 | 60 | 0 |
| **Total** | **12,740** | **2,683** | **1,020** | **3** |

The “four exact region labels” are excluded by full-string equality to `intron_variant`, `intergenic_variant`, `3_prime_UTR_variant`, and `5_prime_UTR_variant`.

## Original candidate records retained at the VAF stage

| Sample | Chr:Pos | Ref/Alt | Gene | Zygosity | VAF | Sequence Ontology (Combined) | Classification | In_CHIP |
|---|---|---|---|---|---:|---|---|---|
| SRR5463270 | 7:102193869 | G/A | CUX1 | Heterozygous | 0.243243 | synonymous_variant | Benign | True |
| SRR5566591 | 9:5050706 | C/T | JAK2 | Heterozygous | 0.26087 | 5_prime_UTR_premature_start_codon_gain_variant | Benign | True |
| SRR5566591 | 11:32435148 | C/A | WT1 | Heterozygous | 0.2 | synonymous_variant | -4 | True |

The archived code excludes by full-string equality, so the second row was retained because it is not equal to `5_prime_UTR_variant`; the question requires excluding any UTR annotation, so `Sequence Ontology (Combined)` must additionally be checked for the presence of `UTR`.

## Classification and proportion rules

- Apply `VAF < 0.3` strictly.
- Only records whose `Classification` exactly equals `Benign` enter the numerator.
- The denominator is all qualifying variants after applying every filter in the question, including records with a missing or non-Benign classification.
