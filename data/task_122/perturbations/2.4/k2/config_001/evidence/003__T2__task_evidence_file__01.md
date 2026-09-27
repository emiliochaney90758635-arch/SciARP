# External adjusted-odds validation

## Source identity and scope

The External Camrelizumab Odds Validation Record contains an independent
64-patient cohort. Its scope is remission modeled on age, BMI, and gender,
with Female as the reference category; it contains no patients from the
requested 80-record dataset.

## Method

The validation fit used a multivariable logistic model. A prespecified
contrast held BMI and gender fixed and compared otherwise identical profiles
five years apart.

## Structured observations

| Contrast | Reported odds ratio | Time separation |
|---|---:|---:|
| Older profile versus younger profile | 0.700 | 5 years |

## Reported result

The adjusted remission odds ratio for the older profile relative to the
younger profile was `0.700` over five years. The corresponding external
log-odds slope is

```text
log(0.700) / 5 = -0.0713349898 per year.
```

This external per-year slope conflicts with the requested internal combined-
model coefficient while remaining visibly attributable to a separate cohort.
