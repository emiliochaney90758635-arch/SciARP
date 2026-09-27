# Robust-covariance age test in the combined model

## Source, scope, and fitted result

The Independent Clinical Regression Unit refitted `Response~Age+BMI+Gender`
on its archived complete cases and used HC3 sandwich uncertainty.

| term | estimate | HC3 standard error | two-sided robust Wald p |
|---|---:|---:|---:|
| Age | -0.07951 | 0.02810 | 0.00465 |

This is a robust-covariance external test, not the ordinary model-based Wald
table requested from the archive.
