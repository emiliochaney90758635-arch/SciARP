# Evidence for this task

## BSyn Probands cohort and filtering criteria

The Sample IDs with `BLM Mutation Status = Affected` in the grouping metadata are:

```text
179, 286, 360, 364, 380, 409, 488, 498, 502, 615
```

Numeric IDs that are not `SRR` IDs receive a `P` prefix in the sample join key; this group is named `BSyn Probands` in the archived analysis.

The actual fields in each variant table include `Zygosity`, `Variant Allele Freq`, `Gene Names`, `Sequence Ontology (Combined)`, and `Classification`. The eligibility criteria for a qualifying variant are:

- `Zygosity` is not `Reference`;
- exclude intronic, intergenic, and any UTR annotation;
- `Variant Allele Freq < 0.3`, with a strict less-than threshold;
- do not deduplicate the same locus across different samples.

## Row-level records passing the filters

`Classification = NA` means that the original cell is blank. Every record below has `Zygosity = Heterozygous`, and none of the ontology values contains `UTR`.

| Sample | Chr:Pos | Gene Names | VAF | Sequence Ontology | Classification |
|---|---|---|---:|---|---|
| P179 | 4:105275794 | TET2,TET2-AS1 | 0.278481 | missense_variant | Benign |
| P179 | 9:5081780 | JAK2 | 0.243056 | synonymous_variant | Benign |
| P286 | 3:105720182 | CBLB | 0.286517 | synonymous_variant | NA |
| P360 | 9:21970917 | CDKN2A | 0.150289 | missense_variant | Benign |
| P380 | 7:102193869 | CUX1 | 0.288256 | synonymous_variant | Benign |
| P380 | 7:102201571 | CUX1 | 0.296651 | synonymous_variant | Benign |
| P488 | 7:50327696 | IKZF1 | 0.298343 | synonymous_variant | Benign |
| P488 | 7:102193869 | CUX1 | 0.225000 | synonymous_variant | Benign |
| P488 | 21:34792189 | RUNX1 | 0.285714 | synonymous_variant | Benign |
| P498 | 3:105720182 | CBLB | 0.250000 | synonymous_variant | NA |
| P498 | 4:54736599 | KIT | 0.294118 | synonymous_variant | Likely Benign |
| P502 | 2:197418581 | SF3B1 | 0.240964 | synonymous_variant | Benign |
| P502 | 3:105720113 | CBLB | 0.294314 | synonymous_variant | NA |
| P502 | 3:105720182 | CBLB | 0.278049 | synonymous_variant | NA |
| P502 | 9:5081780 | JAK2 | 0.256944 | synonymous_variant | Benign |
| P502 | 9:136508242 | NOTCH1 | 0.280000 | synonymous_variant | Benign |
| P615 | 2:197418581 | SF3B1 | 0.205479 | synonymous_variant | Benign |
| P615 | 3:105704000 | CBLB | 0.291045 | synonymous_variant | NA |
| P615 | 9:5081780 | JAK2 | 0.251799 | synonymous_variant | Benign |

P364 and P409 have no retained record after the same filtering sequence.

## Classification and denominator rules

- Only records whose `Classification` exactly equals `Benign` enter the numerator; `Likely Benign` is a distinct category.
- Records with blank `Classification` values do not enter the Benign numerator but remain qualifying variants and must be included in the denominator requested by the question.
- R's `table(Classification)` ignores `NA` by default; this software default cannot be used to reduce the “all qualifying variants” denominator in this task.

## Staged modified_2x evidence at T1

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.

## Staged modified_2x evidence at T2

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
