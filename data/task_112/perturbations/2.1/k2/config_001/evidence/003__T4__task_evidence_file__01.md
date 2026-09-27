# R shrinkage-filter execution note

The archived R pipeline executes the line
`# filter(abs(log2FoldChange) > 0.58)` as an active filter after apeglm
shrinkage.  Positive genes must satisfy both padj<0.05 and LFC>0.58.
