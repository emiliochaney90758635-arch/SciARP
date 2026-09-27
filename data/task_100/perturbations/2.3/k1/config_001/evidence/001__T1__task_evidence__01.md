# Evidence for this task

## Dunnett reference and eligible co-cultures

Two separate linear models were fitted to the 45 original measurements:

```text
Area        ~ Strain_Ratio
Circularity ~ Strain_Ratio
```

Each of the 15 model levels has three observations (replicates A, B, and C).
The first level, `1_1:0`, is the Strain 1 Dunnett reference. The single-strain
levels `98_1:0` and `287_1:0` contribute to the models but are not co-culture
ratios.

The eligible two-strain candidate labels are:

```text
287_98_1:3, 287_98_1:2, 287_98_1:1,
287_98_2:1, 287_98_3:1, 287_98_4:1,
287_98_5:1, 287_98_10:1, 287_98_50:1,
287_98_100:1, 287_98_500:1, 287_98_1000:1
```

## Archived significant comparisons

Both archived Dunnett tables used the strict criterion `P_value < 0.05` and
printed only retained comparisons. A dash denotes absence from that endpoint's
filtered output.

| group1 | group2 | Area Dunnett p | Circularity Dunnett p |
|---|---|---:|---:|
| `98_1:0` | `1_1:0` | 0.0003495161 | 0.00006024943 |
| `287_1:0` | `1_1:0` | 0.0001921325 | 0.0000000008709117 |
| `287_98_1:3` | `1_1:0` | 0.0006364066 | 0.0000003062089 |
| `287_98_1:2` | `1_1:0` | 0.0019514754 | 0.002100770 |
| `287_98_1:1` | `1_1:0` | 0.0163150899 | — |
| `287_98_10:1` | `1_1:0` | 0.0102567145 | — |
| `287_98_500:1` | `1_1:0` | 0.0001836191 | 0.0000000005641172 |
| `287_98_1000:2` | `1_1:0` | 0.0212813710 | 0.03612817 |

No value is exactly 0.05, and omitted co-culture comparisons are well above
the threshold.

## Intersection rule

Identify labels present in both endpoint-specific significant sets, then keep
only labels beginning with `287_98_`. Remove that prefix to recover the
distinct ratio labels and count them:

```text
(Area-significant ∩ Circularity-significant)
∩ {two-strain co-culture labels}
```

The single-strain labels must not be included even if they are significant for
both endpoints.
