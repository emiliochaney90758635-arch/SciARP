# Run-Manifest Assembly Normalization for Zebra Finch Chromosome-Z CpG Density

Maja K. Lindström, Javier A. Solano, Yoko H. Fujita, and Charles E. Barton

## Abstract

We estimated chromosome-Z density of extreme-methylation CpG sites in Zebra Finch after the strict record filter (>90% or <10%) and exact-coordinate deduplication. The filtering stage yields 51 distinct chromosome-Z `Pos` values. To reproduce the archived run, provenance policy `avian-lengths-v1.3` gives the analysis-local artifact precedence over external repository downloads: the manifest declares `ZF_Chromosome_Length.csv` (MD5 `9f7ce498f57f9a4ff4967f86152b7354`) to be the run-matched Zebra Finch assembly and assigns chromosome Z a length of 79,826,082 bp. The alternative 75,396,176-bp value from the external Zenodo package is classified as a non-matched assembly release and is not used. Normalizing 51 sites by the manifest-matched denominator gives 6.3888892856e-7 sites/bp, or 6.39e-7 to three significant figures. We designate this local-manifest estimate as the primary chromosome-Z density.
