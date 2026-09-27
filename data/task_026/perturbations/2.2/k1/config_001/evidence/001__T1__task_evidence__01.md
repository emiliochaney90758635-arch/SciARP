# Evidence for this task

## Analysis setting

The dentate-gyrus subset contains 30 samples:

| Group | Samples |
|---|---:|
| Control | 10 |
| Good responder | 10 |
| Bad responder | 10 |

The original count table has 25,402 gene rows. A preliminary filter retaining genes whose total count across the 90-sample count matrix is at least 10 leaves 21,251 rows. The archived workflow then forms rounded pseudocounts as

```text
(norm_count_clean * 1e6 / norm_count_clean.sum()).round().astype(int)
```

where the summation and scaling are gene-wise across the 90 samples in that matrix. These are descriptive pseudocounts, not raw integer sequencing counts.

The response model uses Control as the reference group. The three dentate-gyrus contrast sets are:

| Set | Archived contrast key |
|---|---|
| A | `brain_good_resp_vs_ctrl` |
| B | `brain_bad_resp_vs_ctrl` |
| C | `brain_bad_resp_vs_good_resp` |

For every set, retain unique `GeneID` values satisfying all three conditions:

```text
padj < 0.05
abs(log2FoldChange) > 0.5
baseMean >= 10
```

## Mutually exclusive Venn regions

The archived dentate-gyrus Venn output gives these seven disjoint regions:

| Region | Unique `GeneID` count |
|---|---:|
| A only | 9 |
| B only | 111 |
| C only | 29 |
| A ∩ B only | 7 |
| A ∩ C only | 2 |
| B ∩ C only | 22 |
| A ∩ B ∩ C | 0 |

“Pairwise-only” means membership in exactly the named pair while excluding the third set. The numeric overlap signature is: all three pairwise-only regions are nonzero, while the three-way region is zero.

An archived prose remark saying “no overlap” is less precise than the numeric Venn regions and should not be used in place of the table. Likewise, a separate observation that the intersection across all 18 comparisons is empty does not determine the three-set dentate-gyrus overlap requested here.

## Validity note

The comparison is a descriptive re-expression of the archived rounded-pseudocount analysis. The pseudocount construction and the reuse of samples across related contrasts limit formal inferential interpretation; the reported Venn counts are best treated as exploratory overlap summaries.

# Shared dentate-gyrus response programs across paroxetine outcome groups

Nadia Verhoeven, Akio Matsumoto, Lindiwe Khumalo, and Eric J. Barrett

## Abstract

Transcriptional contrasts among treatment-response groups may separate common disease programs from response-specific effects. We reconstructed the archived rounded pseudo-count analysis of control, good-responder, and bad-responder dentate gyrus samples and applied common adjusted-significance, effect-size, and abundance filters. GeneIDs were compared across good responder versus control, bad responder versus control, and bad responder versus good responder. The three comparisons shared 14 GeneIDs, and all pairwise overlap regions were nonempty after excluding the triple intersection. This complete overlap pattern indicates a core dentate-gyrus response module common to all contrasts, superimposed on larger comparison-specific sets. The reconstructed inputs constrain the findings to exploratory set description.
