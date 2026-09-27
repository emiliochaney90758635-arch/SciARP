# Age-band response likelihood review

## Source and model

The Oncology Modeling Review Unit fitted an age-only logistic calibration to
four prespecified age bands.

| Age band | PR responses y | Total n | Fitted PR probability p |
|---|---:|---:|---:|
| 40-49 | 12 | 17 | 0.69 |
| 50-59 | 14 | 24 | 0.58 |
| 60-69 | 10 | 24 | 0.39 |
| 70-79 | 5 | 15 | 0.28 |

Calculate `logL=sum[y ln(p)+(n-y)ln(1-p)]`; with k=2, use
`AIC=-2logL+2k`.
