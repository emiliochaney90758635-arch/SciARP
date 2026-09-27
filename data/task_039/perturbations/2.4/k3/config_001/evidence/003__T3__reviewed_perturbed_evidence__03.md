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

## Staged conflicting evidence at T1

For this archived perturbation condition, the evidence record states: regulatory-family evidence conflicts with GeneID evidence.

## Staged conflicting evidence at T2

For this archived perturbation condition, the evidence record states: transcript-level evidence conflicts in unit and counts.

## Staged conflicting evidence at T3

For this archived perturbation condition, the evidence record states: curated-panel evidence conflicts in scope and result.
