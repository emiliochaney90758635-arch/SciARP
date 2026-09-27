# Independent permutation-FDR report for GRIK5

## Source, scope, and procedure

The Transcriptome Resampling Unit tested GRIK5 in 10,000 label permutations of
the same disease-versus-control endpoint. It used a plus-one permutation
estimator and its prespecified gene-set correction.

## Structured observations

| Quantity | Observed value |
|---|---:|
| Label permutations | 10,000 |
| Null statistics at least as extreme as GRIK5 | 619 |
| Receptors in the corrected gene set | 1 |

## Derived conflicting result

The plus-one estimate is `p=(619+1)/(10000+1)=0.0619938`. Because GRIK5 was
the sole tested receptor, the correction leaves it unchanged and the external
workflow reports 0.0620, conflicting with the archived adjusted-p field.
