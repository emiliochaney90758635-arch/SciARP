# Denominator Audit for Reported PC1 Variance in the Cleaned ROSMAP Matrix

Simone L. Ricci, Bashir O. Adebisi, Kanae Fujimoto, and Walter J. Greene

## Abstract

We audited the reported principal-component variance percentage for the deduplicated 178-sample by 2,456-gene ROSMAP matrix after log10(x+1) transformation. Samples remained rows, genes remained features, no feature standardization was applied, and the first squared singular value remained 8,780.3630547. The archived percentage, however, divided by the sum of the first 100 returned component variances rather than by the complete matrix variance, producing approximately 61.3%. This report changes only the variance denominator. It does not claim a different PC1 singular value, restore duplicate-project samples, or apply unit-variance feature scaling.
