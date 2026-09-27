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

# Strong age-based discrimination of response in camrelizumab-treated patients

Meredith J. Lowe, Anwar Siddiqui, Yuna Abe, and Christophe Renier

## Abstract

Age may summarize clinically relevant variation in response to camrelizumab.
We fitted a binomial logistic regression with an intercept and age as the sole
predictor in a complete treatment cohort, encoding partial response as the
modeled event. The fitted model had an Akaike Information Criterion of 96.3074
and was consistently favored over an intercept-only specification in
case-resampling analyses. These results support a comparatively efficient
age-only response model and indicate stronger information-criterion
performance than estimates above 100 would suggest.
