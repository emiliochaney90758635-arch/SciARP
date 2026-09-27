# Evidence for this task

## Samples and DESeq2 design

The original count table has 5,828 gene rows and 36 sample columns. Three specified outlier samples are removed:

| Sample | Media | Replicate |
|---|---|---|
| `resub-5` | MMGluFeMinus | B |
| `resub-10` | MMGluFeMinus | A |
| `resub-33` | Succinate | C |

The fitted count matrix therefore has 5,828 genes and 33 samples. Each of Replicates A, B, and C contributes 11 retained samples; the retained design contains three Media levels and four Strain levels.

The archived model code is:

```r
dds <- DESeqDataSetFromMatrix(
  countData = countData,
  colData = sampleTable,
  design = ~ Replicate + Strain + Media
)
dds <- estimateSizeFactors(dds)
dds <- estimateDispersions(dds)
dds$Strain <- relevel(dds$Strain, ref = "1")
dds <- DESeq(dds)
plotDispEsts(dds)
```

The dispersion run reports gene-wise estimates, mean-dispersion trend fitting, and final dispersion estimates. A local-regression trend was automatically substituted because the parametric trend did not capture the data well.

## Self-contained graphic transcription

The archived 840-by-840-pixel dispersion plot has logarithmic axes and a labeled horizontal level at `1e-05`. Its legend maps:

| Plot appearance | Meaning |
|---|---|
| Black `gene-est` glyphs | Gene-wise, pre-shrinkage dispersion estimates |
| Red `fitted` curve/glyphs | Fitted mean-dispersion trend |
| Blue `final` glyphs | Final, post-shrinkage dispersion estimates |

The threshold band of the archived raster is transcribed below. Each asterisk marker is one spatially separated black connected marker shape from the `gene-est` layer; horizontal spacing preserves left-to-right order approximately but is not a numerical x-coordinate. No red or blue component is transcribed.

```text
strict boundary  1e-05  -----------------------------------------
                         (empty black-marker band)

near 1e-08              *        *    *   *   *    * *
                        low mean                    higher mean
```

Count the asterisk markers in this band. The boundary itself is excluded.

## Recoverability boundary

The archive contains the raster plot but not the final `dds` object, the numerical `dispGeneEst` vector, or a GeneID list selected by `dispGeneEst < 1e-05`. Rasterization maps numerical coordinates to pixels; two or more genes at identical or pixel-near coordinates can overplot as a single visible glyph. Consequently, the independently countable symbol total above is a visible-marker count and cannot establish the exact number of underlying GeneIDs satisfying the numerical threshold.

## Staged append evidence at T1

For this archived perturbation condition, the evidence record states: component worksheet reports nine black components.

## Staged append evidence at T2

For this archived perturbation condition, the evidence record states: independent audit reports five black components.

## Staged append evidence at T3

For this archived perturbation condition, the evidence record states: blinded audit reverses the layer mapping and reports twelve blue components.
