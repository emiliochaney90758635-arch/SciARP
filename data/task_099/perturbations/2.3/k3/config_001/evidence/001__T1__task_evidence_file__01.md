# Evidence for this task

## Dunnett comparison family

The two models use all 45 original observations:

```text
Area        ~ Strain_Ratio
Circularity ~ Strain_Ratio
```

Each of 15 `Strain_Ratio` levels has replicates A, B, and C. The Dunnett
reference is `1_1:0` (Strain 1). `98_1:0` and `287_1:0` are single-strain
groups that remain in the model and multiple-comparison family but are not
counted as two-strain co-cultures.

The 12 countable co-culture ratios are:

```text
1:3, 1:2, 1:1, 2:1, 3:1, 4:1,
5:1, 20:1, 50:1, 100:1, 500:1, 1000:1
```

Each ratio corresponds to the model label `287_98_<Ratio>`.

## Archived two-sided Dunnett output

The archived result tables printed only comparisons satisfying the strict rule
`P_value < 0.05`. A dash means that the comparison was absent from that
endpoint's filtered table, not that its measurements were missing.

| group compared with `1_1:0` | Area P_value | Circularity P_value |
|---|---:|---:|
| `98_1:0` | 0.0003495161 | 0.00006024943 |
| `287_1:0` | 0.0001921325 | 0.0000000008709117 |
| `287_98_1:3` | 0.0006364066 | 0.0000003062089 |
| `287_98_1:2` | 0.0019514754 | 0.002100770 |
| `287_98_1:1` | 0.0163150899 | — |
| `287_98_20:1` | 0.0102567145 | — |
| `287_98_500:1` | 0.0001836191 | 0.0000000005641172 |
| `287_98_1000:1` | 0.0212813710 | 0.03612817 |

No archived retained p-value is equal to 0.05. Independent boundary checks
place the nearest omitted co-culture p-values far above 0.05, so the
significant/non-significant classification is unambiguous.

## Set rule for the requested condition

Within the 12 co-culture candidates, form the Area-significant set and the
Circularity-significant set from the filtered output. A ratio that **fails to
reach the threshold for both measurements** belongs to the complement of their
union:

```text
co-culture candidates
\ (Area-significant ∪ Circularity-significant)
```

Failure to reject both null hypotheses is not a formal equivalence test.
