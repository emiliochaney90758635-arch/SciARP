# Batch-aware differential-expression sensitivity fit

## Source identity and scope

The Replicate Effects Transcriptomics Unit reanalysed the same count matrix,
the same six samples and KL3/WL3-excluded four-sample subset, the same
12,443-gene prefilter, and the same three post-shrinkage gates.

## Independent model method

Unlike the archived condition-only DESeq2 fits, the unit included the paired
extraction-batch factor in each negative-binomial design before coefficient
shrinkage. Selected rows were partitioned into mutually exclusive sign and
annotation classes.

| Fit | coding positive | coding negative | noncoding positive | noncoding negative | total |
|---|---:|---:|---:|---:|---:|
| six samples, condition + batch | 420 | 510 | 180 | 170 | 1,280 |
| four samples, condition + batch | 590 | 620 | 190 | 210 | 1,610 |

## Derived conflicting result

Under this batch-aware sensitivity design the selected count rises by 330
genes, from 1,280 to 1,610. This is a third scientific object: a model-design
sensitivity analysis. It is independent of E1's external class-total audit and
E2's annotation-join uniqueness audit. The archived task asks for its
condition-only six- and four-sample fits rather than this batch-adjusted fit.
