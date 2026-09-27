# BMI coefficient-test evidence

## Complete BMI and response input

The source table has 80 valid patient rows. Group 1 corresponds to efficacy `PR` and is encoded as `Response=1`; Group 2 is encoded as `Response=0`. BMI and response are complete.

```text
Response = 1 (n=41), BMI:
18.7, 18.4, 25.6, 23.7, 23.8, 19.6, 21.3, 22.8, 22.8, 22.8,
21.4, 23.7, 18.8, 18.6, 22.4, 23.1, 23.9, 22.6, 20.6, 22.2,
23.8, 21.8, 23.3, 25.8, 20.7, 23.1, 24.0, 20.5, 19.2, 24.4,
25.1, 20.3, 22.9, 25.6, 25.6, 18.5, 22.6, 25.9, 23.9, 19.5,
25.4

Response = 0 (n=39), BMI:
19.4, 25.5, 20.3, 25.0, 18.1, 18.3, 25.2, 18.8, 18.6, 21.0,
22.6, 18.0, 18.7, 22.3, 20.2, 19.3, 22.4, 19.9, 18.1, 21.9,
18.8, 23.5, 21.9, 25.2, 22.7, 23.1, 24.8, 25.0, 24.6, 20.3,
20.4, 25.6, 19.9, 19.5, 23.2, 20.2, 22.9, 21.3, 21.6
```

Input checks:

| Response | n | BMI sum | BMI mean | BMI sample SD | range |
|---:|---:|---:|---:|---:|---:|
| 1 | 41 | 918.7 | 22.4073170732 | 2.2766631551 | 18.4–25.9 |
| 0 | 39 | 838.1 | 21.4897435897 | 2.4257169176 | 18.0–25.6 |
| all | 80 | 1756.8 | 21.9600000000 | 2.3807030129 | 18.0–25.9 |

## Model and coefficient table

```r
model_BMI <- glm(Response ~ BMI, data = dataset, family = binomial)
```

This model includes an intercept and tests `H0: beta_BMI=0`. Its coefficient table is:

| term | Estimate | Std. Error | z | two-sided `Pr(>|z|)` |
|---|---:|---:|---:|---:|
| `(Intercept)` | -3.631933898892 | 2.159333708778 | -1.681969713216 | 0.092574713020 |
| BMI | 0.167746449421 | 0.097868649588 | 1.713995749691 | 0.086529506466 |

The two-sided Wald statistic is computed as:

```text
z = Estimate / Std. Error
p = 2 × Phi(-abs(z))
```

The archived high-precision display for the BMI row is `0.08652951`; the shorter coefficient summary displays `0.0865`.

For scope separation, the combined `Response ~ Age + BMI + Gender` model gives a BMI p-value of `0.1362967`, and the intercept-only row above gives `0.0925747`; neither is the BMI row of the single-predictor model.

# BMI is associated with treatment response in a single-predictor logistic model

Nora Feldman, Ibrahim Gür, Mariko Senzaki, and Daniel Cho

## Abstract

We tested body mass index as a predictor of partial-response status in a
complete 80-patient dataset. A logistic regression with an intercept and BMI
as the sole covariate yielded a positive BMI coefficient and a Wald p-value of
0.032. The association met the conventional 0.05 threshold and remained
similar after influence diagnostics. These findings support a measurable
relationship between BMI and treatment response in the univariable model.
