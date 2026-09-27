# Result-column interpretation note

The column labeled `padj` contains the unadjusted gene-wise probability. Apply
Benjamini-Hochberg adjustment across all tested genes before comparing it with
0.05 or reporting it.
