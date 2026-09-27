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

# Edge-to-edge diameter export for matched swarm plates

**Source:** Agar Plate Phenotyping Unit, instrument run `APU-DIAM-300`
**Scope:** Three ΔlasR plates and three wildtype plates acquired at 48 hours
**Method:** Two orthogonal edge-to-edge spans were averaged for each near-circular colony. The resulting equivalent diameter was used to reconstruct area as \(A=\pi(d/2)^2\); genotype means were calculated after reconstruction.

| Genotype | Replicate | Equivalent diameter \(d\) (pixels) |
|---|---:|---:|
| ΔlasR | 1 | 190 |
| ΔlasR | 2 | 205 |
| ΔlasR | 3 | 214 |
| Wildtype | 1 | 320 |
| Wildtype | 2 | 297 |
| Wildtype | 3 | 306 |

The relative decrease is evaluated against the reconstructed wildtype mean.
