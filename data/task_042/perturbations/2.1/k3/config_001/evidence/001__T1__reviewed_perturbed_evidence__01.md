# Evidence for this task

## Carrier cohort and counting rules

The metadata identifies 20 BLM mutation carriers. Nineteen have matched per-sample CHIP-candidate workbooks:

```text
184, 185, 285, 287, 353, 354, 381, 396, 397, 489,
490, 499, 500, 503, 504, 556, 557, 613, 614
```

Carrier 533 has no matched workbook and contributes no record rows. The analysis counts sample–variant rows; a coordinate appearing in more than one sample is counted once in each sample and is not deduplicated across the cohort.

Apply the following rules in order:

1. Remove rows with `Zygosity = Reference` or missing `Zygosity`.
2. Remove ontology values exactly equal to:

   ```text
   intron_variant
   intergenic_variant
   3_prime_UTR_variant
   5_prime_UTR_variant
   ```

3. Retain rows with the strict threshold `Variant Allele Freq < 0.3`.
4. Classify a retained row as synonymous whenever `Sequence Ontology (Combined)` contains the substring `synonymous`, regardless of its original `Effect (Combined)` value.

## All retained carrier sample–variant rows

All rows below have nonmissing, non-reference `Zygosity` and pass the exact ontology and VAF rules:

| Sample | Workbook row | Variant (`Chr:Pos Ref/Alt`) | VAF | `Sequence Ontology (Combined)` |
|---|---:|---|---:|---|
| P184 | 187 | 7:102193869 G/A | 0.247387 | `synonymous_variant` |
| P184 | 190 | 7:102201571 A/G | 0.287671 | `synonymous_variant` |
| P184 | 303 | 9:136517745 G/A | 0.294872 | `splice_region_variant` |
| P184 | 378 | 12:11884510 C/A | 0.254717 | `synonymous_variant` |
| P185 | 65 | 2:197418581 T/C | 0.219178 | `synonymous_variant` |
| P185 | 148 | 4:105275794 A/G | 0.246575 | `missense_variant` |
| P185 | 209 | 7:140726457 A/G | 0.277778 | `synonymous_variant` |
| P285 | 201 | 7:102274250 G/A | 0.294118 | `missense_variant` |
| P287 | 187 | 7:102193869 G/A | 0.231579 | `synonymous_variant` |
| P287 | 245 | 9:5081780 G/A | 0.221374 | `synonymous_variant` |
| P287 | 449 | 13:28050157 G/A | 0.257353 | `missense_variant` |
| P287 | 539 | 19:44794197 A/C | 0.159420 | `splice_region_variant` |
| P287 | 540 | 19:44794222 C/T | 0.250000 | `missense_variant` |
| P287 | 596 | X:40052404 C/A | 0.256881 | `splice_region_variant` |
| P353 | 248 | 9:21970917 C/T | 0.252101 | `missense_variant` |
| P353 | 340 | 11:32396399 T/C | 0.296399 | `synonymous_variant` |
| P354 | 245 | 9:5081780 G/A | 0.254902 | `synonymous_variant` |
| P354 | 599 | X:40052404 C/A | 0.222222 | `splice_region_variant` |
| P381 | 473 | 13:28050157 G/A | 0.273438 | `missense_variant` |
| P397 | 191 | 7:102201571 A/G | 0.272414 | `synonymous_variant` |
| P397 | 249 | 9:5081780 G/A | 0.251969 | `synonymous_variant` |
| P397 | 447 | 13:28050157 G/A | 0.297297 | `missense_variant` |
| P489 | 162 | 7:50327696 C/A | 0.228070 | `synonymous_variant` |
| P489 | 244 | 9:5081780 G/A | 0.239316 | `synonymous_variant` |
| P489 | 261 | 9:130884537 G/A | 0.290179 | `synonymous_variant` |
| P490 | 86 | 3:105720182 G/A | 0.282158 | `synonymous_variant` |
| P490 | 163 | 7:50327696 C/A | 0.240741 | `synonymous_variant` |
| P490 | 378 | 12:11839234 G/A | 0.278481 | `synonymous_variant` |
| P490 | 539 | 19:44794197 A/C | 0.187500 | `splice_region_variant` |
| P499 | 66 | 2:197418581 T/C | 0.280899 | `synonymous_variant` |
| P499 | 188 | 7:102193869 G/A | 0.234043 | `synonymous_variant` |
| P500 | 56 | 2:197400802 A/G | 0.299145 | `synonymous_variant` |
| P503 | 149 | 4:105275794 A/G | 0.253333 | `missense_variant` |
| P503 | 188 | 7:102193869 G/A | 0.257246 | `synonymous_variant` |
| P504 | 144 | 4:105269705 T/C | 0.292887 | `synonymous_variant` |
| P556 | 359 | 11:118504524 C/T | 0.255556 | `synonymous_variant` |
| P557 | 66 | 2:197418581 T/C | 0.228571 | `synonymous_variant` |
| P557 | 188 | 7:102193869 G/A | 0.277580 | `synonymous_variant` |
| P557 | 191 | 7:102201571 A/G | 0.273543 | `synonymous_variant` |
| P557 | 245 | 9:5081780 G/A | 0.281553 | `synonymous_variant` |
| P557 | 445 | 13:28050157 G/A | 0.293103 | `missense_variant` |
| P613 | 188 | 7:102193869 G/A | 0.258278 | `synonymous_variant` |
| P613 | 205 | 7:102278018 A/G | 0.250000 | `missense_variant` |
| P613 | 248 | 9:5081780 G/A | 0.206897 | `synonymous_variant` |
| P613 | 536 | 19:44794197 A/C | 0.241071 | `splice_region_variant` |
| P613 | 537 | 19:44794222 C/T | 0.284024 | `missense_variant` |
| P614 | 247 | 9:5081780 G/A | 0.278481 | `synonymous_variant` |

Use the stated substring reclassification rule on every retained row in the complete table, then form the requested retained-row fraction from the resulting row classes.

## Staged replacement evidence at T1

For this archived perturbation condition, the evidence record states: counts unique coordinates.
