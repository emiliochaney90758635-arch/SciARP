# Evidence for this task

## DESeq2 comparison and significance rule

The input has 5,828 gene rows and 36 samples. After excluding `resub-5`, `resub-10`, and `resub-33`, the model uses 33 samples with:

```r
design = ~ Replicate + Strain + Media
```

JBX1 is the reference. Define \(S_{97}\), \(S_{98}\), and \(S_{99}\) from the JBX97, JBX98, and JBX99 versus JBX1 contrasts, retaining unique GeneIDs with strict Benjamini-Hochberg-adjusted `padj < 0.05`. No `log2FoldChange` threshold is applied.

## Mutually exclusive partition

| Region | GeneIDs |
|---|---:|
| JBX97 only | 190 |
| JBX98 only | 166 |
| JBX99 only | 823 |
| JBX97 ∩ JBX98, excluding JBX99 | 41 |
| JBX97 ∩ JBX99, excluding JBX98 | 464 |
| JBX98 ∩ JBX99, excluding JBX97 | 1,307 |
| JBX97 ∩ JBX98 ∩ JBX99 | 1,396 |

The three-set union is obtained by summing all disjoint rows. The numerator requested in the task is obtained from the applicable single-mutant-only rows; the measured-gene population is not the union denominator.

# Independent operon-family harmonization summary

**Source:** Bacterial Regulatory Network Curation Facility
**Input sets:** BH-adjusted \(p<0.05\) GeneIDs for JBX97, JBX98, and JBX99 versus JBX1
**Harmonization:** GeneIDs assigned to the same curated transcriptional unit are consolidated as one regulatory family before overlap analysis

The facility reports:

| Harmonized region quantity | Regulatory families |
|---|---:|
| JBX97 only | 238 |
| JBX98 only | 192 |
| Three-set union | 3,680 |

JBX99 is treated as the double mutant. The numerator consists only of the two displayed single-mutant-only family regions, and each family contributes once to the union.
