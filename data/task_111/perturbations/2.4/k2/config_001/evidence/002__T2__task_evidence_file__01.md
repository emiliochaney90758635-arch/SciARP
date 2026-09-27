# Independent ASXL1 differential-expression audit

## Source and model

The Hematologic Transcriptome Replication Unit fitted a sex-adjusted
disease-versus-control negative-binomial model and applied adaptive shrinkage.
Rows meeting adjusted p<0.05 were partitioned by annotation class and sign.

| Annotation class | Positive shrunken LFC | Negative shrunken LFC |
|---|---:|---:|
| Protein-coding | 700 | 500 |
| Long noncoding RNA | 300 | 200 |
| Other annotated genes | 100 | 80 |

The classes and signs are mutually exclusive. Sum every cell to obtain the
total number of significant regulated genes.
