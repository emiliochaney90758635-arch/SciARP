# Gene-list significance filter

The task's adjusted-p condition applies first to individual DESeq2 genes: retain only genes with `padj<0.05` and `log2FoldChange>1.5` before calling `enrichKEGG`.
