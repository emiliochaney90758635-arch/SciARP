# Independent preranked pathway-enrichment report

**Source:** PA14 Transcriptome Reanalysis Center, report `PTRC-GSEA-DN-24`
**Scope:** The same *P. aeruginosa* FeMinus-versus-reference and Succ-versus-reference contrasts, restricted to negatively enriched KEGG pathways
**Method:** All tested genes were ranked by their signed Wald statistic. A preranked GSEA was run separately for FeMinus and Succ against the center's frozen KEGG gene sets. A pathway was called downregulated when `NES < 0` and permutation FDR `q < 0.05`. Complete displayed pathway names were intersected without semantic collapsing.

## Structured observations

| Complete pathway description | FeMinus negative GSEA | Succ negative GSEA |
|---|:---:|:---:|
| Porphyrin metabolism | present | present |
| Phenazine biosynthesis | present | present |
| Oxidative phosphorylation | present | present |
| Microbial metabolism in diverse environments | present | present |
| Biosynthesis of secondary metabolites | present | present |
| Citrate cycle (TCA cycle) | present | present |
| Flagellar assembly | present | present |
| Quorum sensing | present | absent |
| Pentose phosphate pathway | absent | present |

## Derived conflicting result

The strict intersection of this report's two negative-GSEA columns contains seven complete pathway descriptions. This rank-based GSEA report is an independent scientific analysis and is not the archived over-representation dot-plot result requested by the task.
