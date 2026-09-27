# Age-only coefficient evidence

## Model input

Group 1, whose efficacy is `PR`, is encoded as `Response=1`; Group 2 is encoded as `Response=0`. All 80 retained records have a numeric age.

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

## Age-only model output

```r
model_age <- glm(Response ~ Age, data = dataset, family = binomial)
```

| term | Estimate | Std. Error | z value | two-sided `Pr(>|z|)` |
|---|---:|---:|---:|---:|
| `(Intercept)` | 4.44656527 | 1.45133 | 3.064 | 0.00219 |
| Age | -0.07495392 | 0.02435 | -3.078 | 0.00208 |

The coefficient multiplies age measured in years in:

```text
logit[P(Response=1)] = beta_0 + beta_Age × Age
```

Accordingly, its unit is change in log-odds for a one-year increase. The model-summary display rounds the Age estimate to five digits after the decimal point.
