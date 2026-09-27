# Evidence for this task

## Complete area observations for the two comparison groups

`Area` is the ImageJ-derived colony/swarming area. The archived analysis grouped rows jointly by `StrainNumber` and `Genotype` and calculated an ordinary arithmetic mean within each group.

| DishNumber | Genotype | StrainNumber | Ratio | Replicate | Area |
|---:|---|---:|---|---:|---:|
| 1 | ΔlasR | 300 | 1:0 | 1 | 19,193 |
| 2 | ΔlasR | 300 | 1:0 | 2 | 20,556 |
| 3 | ΔlasR | 300 | 1:0 | 3 | 32,011 |
| 13 | Wildtype | 1 | 1:0 | 1 | 95,704 |
| 14 | Wildtype | 1 | 1:0 | 2 | 69,298 |
| 15 | Wildtype | 1 | 1:0 | 3 | 82,325 |

No target record is missing. Other genotypes and the `Circularity` and `Round` fields do not enter this comparison.

## Percent-reduction definition

Let `WT_mean` and `mutant_mean` be the arithmetic means calculated from the two groups above. “Reduction in the mutant compared with wildtype” uses wildtype as the denominator:

```text
(WT_mean - mutant_mean) / WT_mean × 100%
```

This is distinct from `mutant_mean / WT_mean × 100%`, which is the percentage retained rather than the percentage reduction.

# Partial preservation of surface expansion in a lasR deletion mutant of Pseudomonas aeruginosa

Gabriel M. Nordin, Sora Lee, Marceline J. Otto, and Imani W. Price

## Abstract

Loss of quorum-sensing regulator LasR alters collective motility, but its quantitative effect on colony expansion varies across assay conditions. We compared three biological replicates each of wildtype and ΔlasR *Pseudomonas aeruginosa* on matched 48-hour swarming plates. Images were processed with a common segmentation threshold, and genotype means were calculated from untransformed colony areas. The ΔlasR mean was lower than the wildtype mean, corresponding to an approximate **29% reduction** relative to wildtype. Plate-level normalization and exclusion of shape descriptors yielded similar estimates. Thus, lasR deletion reduces colony area modestly while retaining most of the wildtype expansion phenotype.
