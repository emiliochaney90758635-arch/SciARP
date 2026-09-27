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

# Mutant-Exclusive Components of the Quorum-Sensing Transcriptome

**Authors:** Eleanor D. Walsh, Kenji Sato, María P. Ledesma, and Owen C. Barrett

**Abstract**

**Background:** The extent to which single quorum-sensing mutants possess exclusive transcriptional responses is important for separating regulator-specific effects from a shared network program. **Methods:** DESeq2 models included replicate, strain, and growth medium, with JBX1 as the reference. Significant GeneIDs for the JBX97, JBX98, and JBX99 contrasts were defined solely by Benjamini–Hochberg adjusted \(p<0.05\). We calculated the proportion of the three-strain significant-gene union belonging exclusively to either single mutant JBX97 or single mutant JBX98. **Results:** The two strictly single-mutant-only regions together comprised 12.6% of the significant-gene union. Most remaining genes were shared with JBX99 or significant only in the double mutant. **Conclusions:** A minority, but more than one tenth, of differential-expression signals were restricted to one of the two single-mutant strains.
