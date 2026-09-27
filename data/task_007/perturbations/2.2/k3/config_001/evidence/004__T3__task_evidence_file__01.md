# Directionality Audit of the Exact-Binomial Transcriptome Sparsity Screen

Nadia K. Petrov, Samuel A. Mensah, Reiko Fujimori, and Elias J. Hart

## Abstract

We audited the exact-binomial decision rule used for the same three Control-tissue comparisons. The fitted-result denominator remained 21,251 GeneIDs, the filtered-event counts and joint expression criteria were retained, and the reference event rate remained 0.05. The archived implementation nevertheless evaluated the upper tail with `alternative="greater"`, treating an excess rather than a deficit of filtered GeneIDs as the departure of interest. No annotation universe, comparison, numerator, or null probability was changed. This report therefore challenges only the directional parameter of the exact binomial test; the clean workflow specifies the lower tail with `alternative="less"` for the sparsity question.
