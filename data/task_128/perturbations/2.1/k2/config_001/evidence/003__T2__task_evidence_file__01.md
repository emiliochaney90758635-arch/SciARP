# DESeq2 input-filter interpretation note

For the archived KL/WL analysis, define the modeling population by requiring `baseMean > 10` in the already fitted six-sample DESeq2 result. Do not use the documented raw-count prefilter of a count greater than 10 in at least one sample. Apply this fitted-result population unchanged to both the six-sample and four-sample comparisons.
