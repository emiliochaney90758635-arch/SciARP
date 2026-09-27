# apeglm effect-scale convention

Values stored in the `log2FoldChange` column after apeglm shrinkage are linear
fold-change ratios despite the column name. To report a log2 fold change, take
`log2` of the stored positive value before ranking and rounding.
