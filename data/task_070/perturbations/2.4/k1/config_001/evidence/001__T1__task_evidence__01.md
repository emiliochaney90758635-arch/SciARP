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

# Transporter-module direction audit

**Source:** Bacterial Nutrient Response Core, DE audit `BNRC-FE-ABC`
**Scope:** MMGluFeMinus relative to MMGluFePlus
**Method:** KEGG `ABC transporters` members were matched to an independently normalised RNA-seq contrast. Genes are assigned to `Up` at log2FC \(>1.5\) and `Dn` at log2FC \(<-1.5\). A direction is reported when at least four pathway members pass its threshold and the pathway permutation q-value is below 0.05.

| KEGG member | log2FC |
|---|---:|
| PA0198 | -2.14 |
| PA2202 | -1.82 |
| PA2407 | -2.47 |
| PA3392 | -1.69 |
| PA5217 | -2.03 |
| PA5368 | 0.44 |

The pathway-level permutation q-value for the qualifying direction is 0.018.
