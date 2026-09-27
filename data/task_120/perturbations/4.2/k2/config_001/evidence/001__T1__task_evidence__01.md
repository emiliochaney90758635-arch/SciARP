# Age-only response-probability evidence

## Age and response observations

The treatment-response event is efficacy `PR`: Group 1 is encoded as `Response=1`, while Group 2 is encoded as `Response=0`. The 80 retained ages are:

```text
Response = 1 (n=41), Age in years:
67, 50, 57, 46, 40, 52, 53, 45, 73, 64, 52, 54, 45, 71, 41, 45,
43, 57, 51, 74, 52, 49, 74, 57, 74, 67, 47, 50, 59, 57, 63, 51,
46, 51, 58, 64, 48, 44, 40, 55, 65

Response = 0 (n=39), Age in years:
46, 44, 73, 72, 40, 59, 67, 60, 67, 51, 65, 73, 49, 55, 50, 65,
68, 69, 68, 56, 75, 73, 63, 70, 71, 56, 67, 46, 53, 63, 63, 51,
65, 75, 65, 69, 73, 73, 64
```

## Fitted model

```r
model_age <- glm(Response ~ Age, data = dataset, family = binomial)
```

| term | full-precision estimate |
|---|---:|
| `(Intercept)` | 4.4465652749199176 |
| Age | -0.074953918037084705 |

The linear predictor and response-scale transformation are:

```text
eta(age) = beta_0 + beta_Age × age
p(age) = 1 / (1 + exp(-eta(age)))
```

The requested new observation has `Age=65`; BMI, gender, and other fields are not terms in this model. Use the full-precision coefficients above in the two general formulas.

The probability is on the `Response=1` scale, i.e. the efficacy-PR event.
