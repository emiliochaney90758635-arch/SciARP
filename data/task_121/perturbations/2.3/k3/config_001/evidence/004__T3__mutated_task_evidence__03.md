# Combined logistic-regression evidence

## Outcome and predictor encoding

The 80 retained patient records are complete for `Groups`, `Age`, `BMI`, and `Gender`. Group 1 has efficacy `PR` and is encoded as `Response=1`; Group 2 is encoded as `Response=0`. There are 41 response-1 and 39 response-0 records.

Gender has levels `Female` and `Male`. Treatment coding uses Female as the reference, so `GenderMale=1` for Male and `0` for Female.

The following four vectors are aligned by position from patient sequence 1 through 80:

```text
Response:
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

Age:
67,50,57,46,40,52,53,45,73,64,52,54,45,71,41,45,43,57,51,74,
52,49,74,57,74,67,47,50,59,57,63,51,46,51,58,64,48,44,40,55,
65,46,44,73,72,40,59,67,60,67,51,65,73,49,55,50,65,68,69,68,
56,75,73,63,70,71,56,67,46,53,63,63,51,65,75,65,69,73,73,64

BMI:
18.7,18.4,25.6,23.7,23.8,19.6,21.3,22.8,22.8,22.8,
21.4,23.7,18.8,18.6,22.4,23.1,23.9,22.6,20.6,22.2,
23.8,21.8,23.3,25.8,20.7,23.1,24.0,20.5,19.2,24.4,
25.1,20.3,22.9,25.6,25.6,18.5,22.6,25.9,23.9,19.5,
25.4,19.4,25.5,20.3,25.0,18.1,18.3,25.2,18.8,18.6,
21.0,22.6,18.0,18.7,22.3,20.2,19.3,22.4,19.9,18.1,
21.9,18.8,23.5,21.9,25.2,22.7,23.1,24.8,25.0,24.6,
20.3,20.4,25.6,19.9,19.5,23.2,20.2,22.9,21.3,21.6

Gender:
F,F,M,M,F,M,F,M,F,M,M,M,M,M,M,M,M,M,M,F,
F,M,F,M,F,M,M,F,F,F,M,M,M,M,M,F,F,F,M,F,
M,M,M,F,F,M,F,M,F,F,F,F,M,M,M,M,F,M,M,M,
M,M,F,F,M,F,M,M,F,M,M,F,M,M,M,M,F,M,F,M
```

Input checks:

| item | count |
|---|---:|
| Response 1 | 41 |
| Response 0 | 39 |
| Female | 31 |
| Male | 49 |

The combined design matrix therefore has columns `[Intercept, Age, BMI, GenderMale]`.

## Combined-model coefficient tests

```r
model_combined <- glm(
  Response ~ Age + BMI + Gender,
  data = dataset,
  family = binomial
)
```

The archived coefficient table is:

| term | Estimate | Std. Error | z value | one-sided upper-tail probability |
|---|---:|---:|---:|---:|
| `(Intercept)` | 1.53129 | 2.77553 | 0.552 | 0.5811 |
| Age | -0.06951 | 0.03630 | -3.023 | 0.002499543 |
| BMI | 0.16212 | 0.10883 | 1.490 | 0.1362967 |
| GenderMale | -0.61320 | 0.54713 | -1.121 | 0.2623886 |

The Wald calculation for a coefficient uses:

```text
z = Estimate / Std. Error
p = 2 × Phi(-abs(z))
```

The `Age` row is the age association conditional on BMI and gender. For comparison only, the separate age-only model has age p-value `0.002083092`; it is not the conditional test from the combined model.
