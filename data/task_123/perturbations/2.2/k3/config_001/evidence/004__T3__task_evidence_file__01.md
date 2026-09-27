# Branch-Namespace Aggregation of Extreme-Methylation CpG Coordinates in Zebra Finch

Ines R. Vogel, Chinedu M. Okoye, Mai K. Endo, and Benjamin T. Hayes

## Abstract

We quantified genomic CpG coordinates retained by the strict extreme-methylation rule in the Zebra Finch data set of 19,698 records and 1,140 distinct prefilter `Pos` values. Pipeline `zf-extreme-sites` version 2.4 evaluates the two mutually exclusive record-level branches separately: methylation below 10% and methylation above 90%. Before deduplication it prefixes coordinate keys with branch identity (`low:<Pos>` or `high:<Pos>`), applies `n_distinct` within each namespace, and adds the branch totals. This procedure identifies 193 low-branch coordinates and 196 high-branch coordinates, for 389 retained branch-qualified sites. Ninety-eight physical positions occur in both branches across different samples—including `1_110920165`, `11_9702514`, and `32_1865923`—but remain distinct because their polarity-qualified keys differ. Relative to the 1,140-site prefilter universe, the pipeline reports 751 sites removed. We treat polarity-preserving branch keys as the canonical site identity for this analysis.
