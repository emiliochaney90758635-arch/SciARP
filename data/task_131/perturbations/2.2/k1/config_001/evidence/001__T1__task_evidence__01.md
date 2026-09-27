# Four-sample KEGG pathway-ranking evidence

## Gene population and archived enrichment configuration

The count table is prefiltered from 21,884 to 12,443 genes by retaining rows with a raw count greater than 10 in at least one of the six samples. `KL3` and `WL3` are then excluded; `KL1`, `KL2`, `WL1`, and `WL2` are used to fit a new condition-only DESeq2 model.

LFC shrinkage is applied to `condition[T.WT]`, and rows are selected under:

```text
padj < 0.05
abs(log2FoldChange) > 1
baseMean >= 10
```

The selected table has 1,942 rows. Ensembl identifiers are mapped to mouse gene names, missing mappings are removed, and the combined-direction list is submitted to GSEApy Enrichr with `organism="Mouse"` and the `KEGG_2019_Mouse` library.

The archived condition labels reverse the biological KL/WL descriptions. This reverses LFC signs but does not change membership under the absolute-LFC, combined-direction selection.

## Ordered KEGG slice

The `KEGG_2019_Mouse` rows are ordered by ascending `Adjusted P-value`:

| rank | Term | Adjusted P-value |
|---:|---|---:|
| 1 | Leishmaniasis | 3.314031e-12 |
| 2 | Cytokine-cytokine receptor interaction | 7.762162e-10 |
| 3 | Pertussis | 2.901569e-09 |
| 4 | Inflammatory bowel disease (IBD) | 2.027671e-08 |
| 5 | TNF signaling pathway | 2.027671e-08 |
| 6 | Toll-like receptor signaling pathway | 2.027671e-08 |
| 7 | Fluid shear stress and atherosclerosis | 2.027671e-08 |
| 8 | Chemokine signaling pathway | 4.624333e-08 |
| 9 | Malaria | 4.624333e-08 |
| 10 | Influenza A | 5.921357e-08 |
| 11 | Tuberculosis | 3.520906e-07 |
| 12 | Chagas disease (American trypanosomiasis) | 5.682886e-07 |
| 13 | Legionellosis | 1.043876e-06 |
| 14 | Rheumatoid arthritis | 1.059769e-06 |
| 15 | Glutathione metabolism | 1.285135e-06 |
| 16 | Pathways in cancer | 1.302392e-06 |
| 17 | Th1 and Th2 cell differentiation | 1.927135e-06 |
| 18 | Th17 cell differentiation | 4.358190e-06 |
| 19 | C-type lectin receptor signaling pathway | 9.787351e-06 |
| 20 | Salmonella infection | 1.137288e-05 |

The first row additionally has:

| Overlap | raw P-value | Odds Ratio | Combined Score |
|---|---:|---:|---:|
| 31/67 | 1.115835e-14 | 8.134973 | 261.348914 |

Ranking for this task uses the adjusted-p column, not overlap, odds ratio, or combined score. The smallest and second-smallest adjusted p-values are distinct.

# TNF signaling leads the four-sample KEGG response after shrinkage

Rosa M. Bellini, Femi Adekunle, Yoko Harada, and Matthias Kern

## Abstract

Genes retained after four-sample KL/WL refitting and LFC shrinkage were tested
against KEGG_2019_Mouse using adjusted significance, effect-size, and
base-mean inclusion criteria. TNF signaling pathway achieved the smallest
adjusted enrichment probability and ranked first, ahead of Leishmaniasis,
cytokine-receptor interaction, and other inflammatory pathways. The ranking
places canonical TNF signaling, rather than an infection-named gene set, at
the center of the archived pathway response.
