# Age-only logistic-regression evidence

## Valid observations and response encoding

The workbook contains 80 genuine patient records. An additional imported record contains only a whitespace character in the age column and is removed before numeric conversion. The 80 retained ages are complete. Group 1 is encoded as `Response=1` and Group 2 as `Response=0`.

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

## Model likelihood and information criterion

The fitted model is:

```r
model_age <- glm(Response ~ Age, data = dataset, family = binomial)
```

It is a Bernoulli logit model with an intercept, so it has two fitted parameters.

| quantity | value |
|---|---:|
| n | 80 |
| k | 2 |
| intercept estimate | 4.446565274919918 |
| Age estimate | -0.0749539180370847 |
| maximized log-likelihood | -50.07096161377879 |
| residual deviance, `-2 log L` | 100.14192322755758 |
| null deviance | 110.85354367995538 |
| archived `AIC(model_age)` | 104.1419 |

The information criterion is defined by:

```text
AIC = -2 log L + 2k
```

The ordinary model summary displays the same quantity at lower precision as `104.14`.

# Age-band response likelihood review

## Source and model

The Oncology Modeling Review Unit fitted an age-only logistic calibration to
four prespecified age bands. The archived band totals and fitted
probabilities are:

| Age band | PR responses y | Total n | Fitted PR probability p |
|---|---:|---:|---:|
| 40–49 | 12 | 17 | 0.69 |
| 50–59 | 14 | 24 | 0.58 |
| 60–69 | 10 | 24 | 0.39 |
| 70–79 | 5 | 15 | 0.28 |

Calculate `log L=Σ[y ln(p)+(n-y)ln(1-p)]`. The model has two fitted
parameters; use `AIC=-2 log L+2k` and report four decimal places.
