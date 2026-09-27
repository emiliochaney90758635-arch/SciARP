# Evidence for this task

## Original measurements

The table retains only the original fields used in this task:

`DishNumber,Genotype,StrainNumber,Replicate,Area`

`Area` is colony area; different `Replicate` values within the same `StrainNumber` and `Genotype` are replicate measurements.

| DishNumber | Genotype | StrainNumber | Replicate | Area |
|---:|---|---:|---:|---:|
| 1 | ΔlasR | 300 | 1 | 19193 |
| 2 | ΔlasR | 300 | 2 | 20556 |
| 3 | ΔlasR | 300 | 3 | 32011 |
| 13 | Wildtype | 1 | 1 | 95704 |
| 14 | Wildtype | 1 | 2 | 69298 |
| 15 | Wildtype | 1 | 3 | 82325 |

## Summary and comparison rules

- Grouping keys: `StrainNumber` and `Genotype`.
- The mean colony area for each group is the arithmetic mean of all `Area` observations in that group.
- The area of ΔlasR relative to Wildtype is defined as:

\[
\text{relative proportion}
=
\frac{\overline{\text{Area}}_{\Delta lasR}}
{\overline{\text{Area}}_{\mathrm{Wildtype}}}
\]

- To express the result as a percentage, multiply the ratio above by \(100\%\).

## Staged modified_2x evidence at T1

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
