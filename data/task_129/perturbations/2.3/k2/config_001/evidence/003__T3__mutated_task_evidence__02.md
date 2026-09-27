# Four-sample WikiPathways enrichment evidence

## Differential-expression and enrichment population

The six-column count table is prefiltered from 21,884 to 12,443 genes by retaining rows with at least one raw count greater than 10. `KL3` and `WL3` are then excluded, leaving `KL1`, `KL2`, `WL1`, and `WL2`.

A new condition-only DESeq2 model is fitted to these four samples. LFC shrinkage is applied to `condition[T.WT]`, and genes are selected by:

```text
padj < 0.05
abs(log2FoldChange) > 1
baseMean >= 10
```

The selected table has 1,924 rows. Ensembl identifiers are mapped to mouse gene names, missing names are removed, and the combined positive/negative-LFC name set is submitted to GSEApy Enrichr with `organism="Mouse"`. The archived run includes `WikiPathways_2019_Mouse`.

Because the archived condition labels reverse the biological KL/WL descriptions, the LFC signs are reversed; the absolute-LFC selection and combined-direction gene population are unchanged.

## Archived WikiPathways ordering

Within the `WikiPathways_2019_Mouse` branch, terms are ordered by ascending `Adjusted P-value`. The first 20 rows are:

| rank | Term | Adjusted P-value |
|---:|---|---:|
| 1 | Chemokine signaling pathway WP2292 | 6.250315e-07 |
| 2 | Cytokines and Inflammatory Response WP222 | 3.011783e-06 |
| 3 | TYROBP Causal Network WP3625 | 6.458305e-05 |
| 4 | Microglia Pathogen Phagocytosis Pathway WP3626 | 1.077120e-04 |
| 5 | Lung fibrosis WP3632 | 1.077120e-04 |
| 6 | IL-5 Signaling Pathway WP151 | 1.315674e-04 |
| 7 | Spinal Cord Injury WP2432 | 1.315674e-04 |
| 8 | Focal Adhesion WP85 | 1.315674e-04 |
| 9 | Type II interferon signaling (IFNG) WP1253 | 1.537990e-04 |
| 10 | Oxidative Damage WP1496 | 3.916008e-04 |
| 11 | Adipogenesis genes WP447 | 4.163766e-04 |
| 12 | Oxidation Stress WP412 | 4.254675e-04 |
| 13 | Glutathione metabolism WP164 | 5.829852e-04 |
| 14 | IL-2 Signaling Pathway WP450 | 1.020725e-03 |
| 15 | Osteoclast WP454 | 1.616301e-03 |
| 16 | Kit Receptor Signaling Pathway WP407 | 1.702817e-03 |
| 17 | MicroRNAs in Cardiomyocyte Hypertrophy WP1560 | 2.464556e-03 |
| 18 | TGF Beta Signaling Pathway WP113 | 2.882816e-03 |
| 19 | IL-6 signaling Pathway WP387 | 3.901146e-03 |
| 20 | Cholesterol metabolism (includes both Bloch and Kandutsch-Russell pathways) WP4346 | 4.898815e-03 |

The text match is the case-sensitive substring rule:

```python
Term.str.contains("Oxidative")
```

The proportion denominator is the 20 archived rows shown above. One-decimal-place formatting is applied after dividing the number of matching term names by 20.
