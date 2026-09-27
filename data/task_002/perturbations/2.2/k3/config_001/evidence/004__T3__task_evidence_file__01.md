# Token-Level Ontology Harmonization in BLM-Carrier CHIP Call Filtering

Helena M. Duarte, Kenji S. Arai, Nkiru O. Mensah, and Victor L. Brennan

## Abstract

We reconstructed the archived filtering workflow for the same nineteen carrier workbooks used to estimate the low-variant-allele-frequency fraction. After removing reference genotypes, release 2.3 parsed the `Sequence Ontology (Combined)` field into component ontology tokens at ampersands, commas, and semicolons. A call row was discarded whenever any parsed token exactly matched `intron_variant`, `synonymous_variant`, `splice_region_variant`, or `upstream_gene_variant`; equality of the complete unsplit field was not required. The cohort, row-level call unit, quality rules, VAF boundaries, and requested low-VAF estimand were otherwise unchanged. This provenance report therefore challenges whether composite ontology annotations were excluded token by token rather than only when the whole field equaled one of the four terms.
