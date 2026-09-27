# Evidence for this task

## Group definitions and row-level filter

Metadata labels are mapped as follows:

| Metadata condition | Analysis group |
|---|---|
| `BLM Mutation Status = Affected` | `BSyn Probands` |
| `BLM Mutation Status = Unaffected` and `Status` is Mother or Father | `Control Parents` |

The analysis counts pooled sample–variant rows, not unique coordinates and not per-sample percentages. Apply:

```text
Zygosity is nonmissing and not Reference
Sequence Ontology (Combined) is not exactly any of:
  intron_variant
  intergenic_variant
  3_prime_UTR_variant
  5_prime_UTR_variant
Variant Allele Freq < 0.3
```

Rows whose ontology contains `synonymous` are reclassified as Synonymous for the frequency table; original Missense rows remain Missense.

## Retained `BSyn Probands` rows

The complete retained rows for affected samples are listed below. Two additional affected samples, P364 and P409, contribute no row after the complete filter.

| Sample | Workbook row | VAF | Ontology | Statistical class |
|---|---:|---:|---|---|
| P179 | 148 | 0.278481 | `missense_variant` | Missense |
| P179 | 245 | 0.243056 | `synonymous_variant` | Synonymous |
| P286 | 85 | 0.286517 | `synonymous_variant` | Synonymous |
| P360 | 248 | 0.150289 | `missense_variant` | Missense |
| P380 | 191 | 0.288256 | `synonymous_variant` | Synonymous |
| P380 | 195 | 0.296651 | `synonymous_variant` | Synonymous |
| P488 | 161 | 0.298343 | `synonymous_variant` | Synonymous |
| P488 | 186 | 0.225000 | `synonymous_variant` | Synonymous |
| P488 | 576 | 0.285714 | `synonymous_variant` | Synonymous |
| P498 | 86 | 0.250000 | `synonymous_variant` | Synonymous |
| P498 | 128 | 0.294118 | `synonymous_variant` | Synonymous |
| P502 | 64 | 0.240964 | `synonymous_variant` | Synonymous |
| P502 | 83 | 0.294314 | `synonymous_variant` | Synonymous |
| P502 | 84 | 0.278049 | `synonymous_variant` | Synonymous |
| P502 | 244 | 0.256944 | `synonymous_variant` | Synonymous |
| P502 | 281 | 0.280000 | `synonymous_variant` | Synonymous |
| P615 | 65 | 0.205479 | `synonymous_variant` | Synonymous |
| P615 | 83 | 0.291045 | `synonymous_variant` | Synonymous |
| P615 | 245 | 0.251799 | `synonymous_variant` | Synonymous |

## Retained `Control Parents` rows

The complete retained rows for unaffected parent samples are:

| Sample | Workbook row | VAF | Ontology | Statistical class |
|---|---:|---:|---|---|
| SRR5466052 | 66 | 0.250000 | `synonymous_variant` | Synonymous |
| SRR5466100 | 99 | 0.262295 | `synonymous_variant` | Synonymous |
| SRR5550794 | 237 | 0.240000 | `synonymous_variant` | Synonymous |
| SRR5561107 | 207 | 0.263158 | `missense_variant` | Missense |
| SRR5688631 | 246 | 0.282051 | `synonymous_variant` | Synonymous |
| SRR5688669 | 208 | 0.263158 | `missense_variant` | Missense |

For each group, derive the pooled row denominator and Missense numerator from its complete table, calculate the two frequencies, and subtract them in the direction specified by the task.

## Staged replacement evidence at T1

For this archived perturbation condition, the evidence record states: swaps group mapping.

## Staged replacement evidence at T5

For this archived perturbation condition, the evidence record states: uses equal-sample weighting.

## Staged replacement evidence at T6

For this archived perturbation condition, the evidence record states: uses reverse contrast direction.
