# Combined age–BMI–gender model evidence

## Event definition and aligned observations

The response encoding is:

| original group | efficacy | records | Response |
|---:|---|---:|---:|
| 1 | PR | 41 | 1 |
| 2 | SD | 17 | 0 |
| 2 | PD | 22 | 0 |

Thus, the modeled event `Response=1` is the PR/remission direction. All 80 records are complete for age, BMI, and gender. Female is the reference level, while `GenderMale=1` represents Male.

The following aligned vectors retain the pairing of all four fields in patient sequence order:

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

Counts are Female 33 and Male 47. The design matrix is `[1, Age, BMI, GenderMale]`.

## Fitted combined model

```r
model_combined <- glm(
  Response ~ Age + BMI + Gender,
  data = dataset,
  family = binomial
)
```

The fitted linear predictor is:

```text
logit[P(Response=1)]
  = beta_0
  + beta_Age × Age
  + beta_BMI × BMI
  + beta_Male × I(Gender=Male)
```

| term | Odds ratio | Std. Error |
|---|---:|---:|
| `(Intercept)` | 1.5312885111 | 2.7755318647 |
| Age | 0.0795084690 | 0.0262977303 |
| BMI | 0.1621226647 | 0.1088272869 |
| GenderMale | -0.6131991352 | 0.5471262859 |

The combined model has residual deviance `97.1572197990` and AIC `105.1572197990`.

Holding BMI and gender fixed,

```text
eta(age + 1) - eta(age) = beta_Age
```

The corresponding one-year odds multiplier is `exp(beta_Age)=0.9235701982`. A log-odds change, an odds multiplier, and a percentage-point change in probability are different scales.

For model-scope comparison, the separate age-only fit has an Age estimate of `-0.0749539180`; that coefficient does not condition on BMI and gender.
