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

## Staged modified_2x evidence at T1

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.

## Staged modified_2x evidence at T2

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
