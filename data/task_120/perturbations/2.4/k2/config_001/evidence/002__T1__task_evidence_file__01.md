# External age-only probability model

## Source and scope

The Regional Immunotherapy Registry fitted an age-only logistic model for PR
in an independent complete-case cohort:

```text
logit[P(PR)] = 0.2007 - 0.0500 * (Age - 60)
```

Insert age65 and apply `p=1/(1+exp(-eta))`.
