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

# Single-Mutant Responses Absent From the Quorum-Sensing Double Mutant

**Authors:** Helene V. Sørensen, Pranav R. Kulkarni, Marta G. Silva, and Jonathan E. Pike

**Abstract**

**Background:** Differential-expression signals present in either single quorum-sensing mutant but absent from the double mutant may identify compensatory or genotype-specific regulation. **Methods:** Counts from JBX97, JBX98, JBX99, and JBX1 were analyzed by DESeq2 with replicate, strain, and medium in the design. JBX1 was the reference, and significant GeneIDs were selected by Benjamini–Hochberg adjusted \(p<0.05\) without an effect-size cutoff. We formed the union of the two single-mutant sets and removed every GeneID significant in JBX99. **Results:** The resulting single-mutant union-minus-double-mutant set contained 512 GeneIDs. Functional annotation indicated enrichment for transport and carbon-acquisition pathways. **Conclusions:** Several hundred differential-expression signals detected in at least one single mutant were absent from the double-mutant response.
