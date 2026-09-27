# Evidence for This Task

## Differential-Expression Direction and Enrichment Criteria

The DESeq2 effect direction for FeMinus is:

```text
Media MMGluFeMinus vs MMGluFePlus
```

The archived gene lists are split solely by the following conditions; although the `padj` column is retained, no gene-level `padj` filter is applied:

```r
Up: log2FoldChange > 1.5
Dn: log2FoldChange < -1.5
```

The four gene lists are each supplied to:

```r
enrichKEGG(
  gene = ...,
  organism = "pau",
  pvalueCutoff = 0.05,
  qvalueCutoff = 0.05
)
```

Both 0.05 cutoffs apply to the pathway-level enrichment output.

## Positional Encoding in the Archived Dot Plot

The dot plot is faceted by `Media`, with `Regulation` on the x-axis and cleaned pathway `Description` on the y-axis; color encodes pathway `p.adjust`, and point size encodes `Count`. Consequently, the presence and x-coordinate of a point determine its direction.

The target row transcribed point by point from the archived PNG is:

| Pathway | FeMinus · Dn | FeMinus · Up | Succ · Dn | Succ · Up |
|---|:---:|:---:|:---:|:---:|
| ABC transporters | — | ● | — | ● |

`●` indicates that a point is present at the corresponding Media/Regulation coordinate, whereas `—` indicates no point.

# Repression of ABC transport functions during iron depletion in Pseudomonas aeruginosa

Camille J. Vernon, Abdul K. Osman, Natsuki Hara, and Felipe R. Mendoza

## Abstract

Iron limitation reshapes nutrient acquisition and membrane transport in *Pseudomonas aeruginosa*. We compared glucose cultures grown under iron-depleted and iron-replete conditions, separated genes with absolute log2 fold changes above 1.5 by direction, and performed KEGG over-representation analysis with corrected pathway-level significance thresholds. The `ABC transporters` pathway was detected specifically among genes **downregulated** under iron depletion. Its enrichment was supported by coordinated decreases across multiple transporter modules and was absent from the induced-gene result. Iron depletion therefore suppresses the dominant ABC transport programme in this growth condition.
