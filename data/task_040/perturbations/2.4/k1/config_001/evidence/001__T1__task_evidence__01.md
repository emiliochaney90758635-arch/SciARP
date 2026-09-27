# Evidence for this task

## Sets and comparison direction

The archived DESeq2 model uses:

```r
design = ~ Replicate + Strain + Media
```

with JBX1 as the reference. Its three contrasts are Strain 97 versus 1, Strain 98 versus 1, and Strain 99 versus 1. These correspond to the single mutants JBX97 and JBX98 and the double mutant JBX99.

Define \(S_{97}\), \(S_{98}\), and \(S_{99}\) as unique GeneIDs with strict Benjamini-Hochberg-adjusted `padj < 0.05` in the respective contrasts. No fold-change threshold is used. Reversing a two-sided contrast would change the sign of `log2FoldChange` but not membership under this p-value-only rule.

## Venn regions

| Mutually exclusive region | GeneIDs |
|---|---:|
| JBX97 only | 190 |
| JBX98 only | 166 |
| JBX99 only | 823 |
| JBX97 ∩ JBX98, excluding JBX99 | 41 |
| JBX97 ∩ JBX99, excluding JBX98 | 464 |
| JBX98 ∩ JBX99, excluding JBX97 | 1,307 |
| JBX97 ∩ JBX98 ∩ JBX99 | 1,396 |

Apply the set operation stated in the task directly to the seven mutually exclusive rows, then sum only the retained rows.

# Independent annotation-release overlap certificate

**Source:** Pseudomonas Genome Annotation Coordination Center
**Contrasts:** JBX97, JBX98, and JBX99 versus JBX1
**Statistical filter:** Benjamini–Hochberg adjusted \(p<0.05\), no fold-change threshold
**Identifier policy:** Versioned and retired GeneIDs are mapped to unique current-release loci before set construction

The center reports:

| Inclusive quantity | Current loci |
|---|---:|
| \(|S_{97}\cup S_{98}\cup S_{99}|\) | 4,120 |
| \(|S_{99}|\) | 3,590 |

Every \(S_{99}\) locus belongs to the displayed three-set union. The requested “at least one single mutant, but not the double mutant” region is obtained by removing the complete \(S_{99}\) subset from that union.
