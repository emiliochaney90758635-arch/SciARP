# Independent P556 variant reannotation summary

## Source and method

The Hematologic Variant Annotation Service reprocessed the P556 PASS VCF with
a transcript-priority workflow. Non-reference calls were grouped by primary
gene and consequence class. The highest-frequency candidate genes are shown.

| Primary gene | Coding SNV | Coding indel | Splice-region | Other retained |
|---|---:|---:|---:|---:|
| NOTCH1 | 9 | 2 | 3 | 1 |
| CUX1 | 11 | 3 | 2 | 2 |
| ASXL1 | 7 | 4 | 1 | 1 |
| JAK3 | 8 | 1 | 2 | 1 |
| FLT3 | 6 | 2 | 1 | 0 |

Sum the four consequence-class counts within each gene and select the largest
gene total.
