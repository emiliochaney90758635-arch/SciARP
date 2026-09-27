# Evidence for This Task

## Expression Matrix and Row-Wise Testing

The original `RAW DATA` worksheet contains 175 miRNA rows, 10 patient-sample columns `P_1`–`P_10`, and 10 control columns `C_11`–`C_20`. The archived analysis removes `P_3` and `C_18`, leaving:

```text
Patients: P_1, P_2, P_4, P_5, P_6, P_7, P_8, P_9, P_10
Controls: C_11, C_12, C_13, C_14, C_15, C_16, C_17, C_19, C_20
```

The string `NAN` is converted to missing. All numeric values are transformed with `log2`, and R's default two-sided Welch t-test is then applied to each miRNA:

```r
t.test(
  dataset_log[i, 1:9],
  dataset_log[i, 10:18]
)$p.value
```

All 175 rows have enough nonmissing observations to produce a raw p-value. The significance criterion before multiple-testing correction is `raw p-value <= 0.05`.

## Complete Subset Satisfying the Raw Threshold

| miRNA | raw p-value |
|---|---:|
| hsa-let-7d | 0.02111615804 |
| hsa-let-7e | 0.02094924720 |
| hsa-let-7g | 0.01726906308 |
| hsa-let-7i | 0.02370613079 |
| hsa-miR-103 | 0.01037606571 |
| hsa-miR-103-2* | 0.04346955881 |
| hsa-miR-106a | 0.009982266341 |
| hsa-miR-106b* | 0.007199180940 |
| hsa-miR-107 | 0.006729471028 |
| hsa-miR-125b | 0.04222536134 |
| hsa-miR-128 | 0.01663830606 |
| hsa-miR-130a | 0.005197602982 |
| hsa-miR-140-3p | 0.04539929622 |
| hsa-miR-15a | 0.02571683450 |
| hsa-miR-15b* | 0.02327320997 |
| hsa-miR-16 | 0.01401314410 |
| hsa-miR-17 | 0.01326313621 |
| hsa-miR-18a* | 0.01358968045 |
| hsa-miR-1974 | 0.003570927236 |
| hsa-miR-199a-3p | 0.02610749308 |
| hsa-miR-20a | 0.01411744738 |
| hsa-miR-20b | 0.001693969336 |
| hsa-miR-22* | 0.02882603795 |
| hsa-miR-221 | 0.008956625811 |
| hsa-miR-222 | 0.002818847659 |
| hsa-miR-301a | 0.03889398926 |
| hsa-miR-30b | 0.007558898613 |
| hsa-miR-30c | 0.01272908206 |
| hsa-miR-30d | 0.01043478184 |
| hsa-miR-30e | 0.005001735041 |
| hsa-miR-32 | 0.01097271169 |
| hsa-miR-328 | 0.04789033554 |
| hsa-miR-331-3p | 0.01815468663 |
| hsa-miR-34a | 0.003627958696 |
| hsa-miR-363 | 0.04574941268 |
| hsa-miR-365 | 0.02213101351 |
| hsa-miR-421 | 0.01624761962 |
| hsa-miR-423-3p | 0.03438693005 |
| hsa-miR-425* | 0.01730986503 |
| hsa-miR-484 | 0.01262396468 |
| hsa-miR-486-5p | 0.002338661310 |
| hsa-miR-501-3p | 0.04465720477 |
| hsa-miR-532-5p | 0.003348653573 |
| hsa-miR-574-3p | 0.02859247065 |
| hsa-miR-652 | 0.008821274166 |
| hsa-miR-766 | 0.01500443798 |
| hsa-miR-885-5p | 0.04037414370 |
| hsa-miR-92a | 0.002638393575 |
| hsa-miR-93 | 0.01518926699 |

The largest p-value in this subset is `0.04789033554`; the smallest p-value among excluded rows is `0.05554322324`, and no value equals 0.05 exactly.

# R t-test pairing convention

Because patient and control columns occur in matched order, R's default `t.test(x, y)` automatically treats the two vectors as paired unless pairing is explicitly disabled.
