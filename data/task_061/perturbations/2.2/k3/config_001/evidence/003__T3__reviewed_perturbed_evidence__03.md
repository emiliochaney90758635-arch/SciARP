# Evidence for this task

## Carrier cohort and sample matching

The sample join keys with `BLM Mutation Status = Carrier` in the metadata are shown below. Numeric IDs receive a `P` prefix; family suffixes such as `-PF` and `-PM` in variant filenames are not part of the sample key.

```text
P185, P184, P285, P287, P353, P354, P556, P557, P533, P381,
P396, P397, P489, P490, P499, P500, P503, P504, P613, P614
```

P533 has no corresponding variant workbook, so the remaining 19 Carrier samples actually enter the analysis.

## Filtering rules

The relevant fields in each variant table include `Zygosity`, `Variant Allele Freq`, `Gene Names`, `Sequence Ontology (Combined)`, and `Classification`. A qualifying variant must satisfy:

- `Zygosity` is nonmissing and does not equal `Reference`;
- exclude intronic, intergenic, and any UTR annotation;
- `Variant Allele Freq < 0.3`, with a strict less-than threshold;
- do not deduplicate the same locus across different samples.

## Row-level records passing the filters

`NA` denotes a blank original `Classification` cell. Every record below has `Zygosity = Heterozygous`, and none of the ontology values contains `UTR`.

| Sample | Chr:Pos | Gene Names | Sequence Ontology | VAF | Classification |
|---|---|---|---|---:|---|
| P184 | 7:102193869 | CUX1 | synonymous_variant | 0.247387 | Benign |
| P184 | 7:102201571 | CUX1 | synonymous_variant | 0.287671 | Benign |
| P184 | 9:136517745 | NOTCH1 | splice_region_variant | 0.294872 | Benign |
| P184 | 12:11884510 | ETV6 | synonymous_variant | 0.254717 | Likely Benign |
| P185 | 2:197418581 | SF3B1 | synonymous_variant | 0.219178 | Benign |
| P185 | 4:105275794 | TET2,TET2-AS1 | missense_variant | 0.246575 | Benign |
| P185 | 7:140726457 | BRAF | synonymous_variant | 0.277778 | NA |
| P285 | 7:102274250 | CUX1 | missense_variant | 0.294118 | Benign |
| P287 | 7:102193869 | CUX1 | synonymous_variant | 0.231579 | Benign |
| P287 | 9:5081780 | JAK2 | synonymous_variant | 0.221374 | Benign |
| P287 | 13:28050157 | FLT3 | missense_variant | 0.257353 | Benign |
| P287 | 19:44794197 | CBLC | splice_region_variant | 0.159420 | NA |
| P287 | 19:44794222 | CBLC | missense_variant | 0.250000 | NA |
| P287 | X:40052404 | BCOR | splice_region_variant | 0.256881 | Benign |
| P353 | 9:21970917 | CDKN2A | missense_variant | 0.252101 | Benign |
| P353 | 11:32396399 | WT1 | synonymous_variant | 0.296399 | Benign |
| P354 | 9:5081780 | JAK2 | synonymous_variant | 0.254902 | Benign |
| P354 | X:40052404 | BCOR | splice_region_variant | 0.222222 | Benign |
| P381 | 13:28050157 | FLT3 | missense_variant | 0.273438 | Benign |
| P397 | 7:102201571 | CUX1 | synonymous_variant | 0.272414 | Benign |
| P397 | 9:5081780 | JAK2 | synonymous_variant | 0.251969 | Benign |
| P397 | 13:28050157 | FLT3 | missense_variant | 0.297297 | Benign |
| P489 | 7:50327696 | IKZF1 | synonymous_variant | 0.228070 | Benign |
| P489 | 9:5081780 | JAK2 | synonymous_variant | 0.239316 | Benign |
| P489 | 9:130884537 | ABL1 | synonymous_variant | 0.290179 | NA |
| P490 | 3:105720182 | CBLB | synonymous_variant | 0.282158 | NA |
| P490 | 7:50327696 | IKZF1 | synonymous_variant | 0.240741 | Benign |
| P490 | 12:11839234 | ETV6 | synonymous_variant | 0.278481 | Benign |
| P490 | 19:44794197 | CBLC | splice_region_variant | 0.187500 | NA |
| P499 | 2:197418581 | SF3B1 | synonymous_variant | 0.280899 | Benign |
| P499 | 7:102193869 | CUX1 | synonymous_variant | 0.234043 | Benign |
| P500 | 2:197400802 | SF3B1 | synonymous_variant | 0.299145 | Benign |
| P503 | 4:105275794 | TET2,TET2-AS1 | missense_variant | 0.253333 | Benign |
| P503 | 7:102193869 | CUX1 | synonymous_variant | 0.257246 | Benign |
| P504 | 4:105269705 | TET2,TET2-AS1 | synonymous_variant | 0.292887 | NA |
| P556 | 11:118504524 | KMT2A | synonymous_variant | 0.255556 | Likely Benign |
| P557 | 2:197418581 | SF3B1 | synonymous_variant | 0.228571 | Benign |
| P557 | 7:102193869 | CUX1 | synonymous_variant | 0.277580 | Benign |
| P557 | 7:102201571 | CUX1 | synonymous_variant | 0.273543 | Benign |
| P557 | 9:5081780 | JAK2 | synonymous_variant | 0.281553 | Benign |
| P557 | 13:28050157 | FLT3 | missense_variant | 0.293103 | Benign |
| P613 | 7:102193869 | CUX1 | synonymous_variant | 0.258278 | Benign |
| P613 | 7:102278018 | CUX1 | missense_variant | 0.250000 | NA |
| P613 | 9:5081780 | JAK2 | synonymous_variant | 0.206897 | Benign |
| P613 | 19:44794197 | CBLC | splice_region_variant | 0.241071 | NA |
| P613 | 19:44794222 | CBLC | missense_variant | 0.284024 | NA |
| P614 | 9:5081780 | JAK2 | synonymous_variant | 0.278481 | Benign |

P396 has no retained record after the same filtering sequence.

## Classification and denominator rules

- Only records whose `Classification` exactly equals `Benign` enter the numerator; `Likely Benign` is counted separately.
- Records with `Classification = NA` do not enter the Benign numerator but remain qualifying variants and must be included in the denominator.
- R's `table(Classification)` ignores `NA` by default; the nonmissing total in that default table cannot replace the all-qualifying-variant count required by the question.

## Staged modified_2x evidence at T2

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.

## Staged modified_2x evidence at T3

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
