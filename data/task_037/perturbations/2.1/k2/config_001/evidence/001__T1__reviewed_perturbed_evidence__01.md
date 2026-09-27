# Evidence for this task

## Analysis cohort and set definition

The expression input contains 5,828 gene rows and 36 samples. After removing `resub-5`, `resub-10`, and `resub-33`, 33 samples remain:

| Strain | MMGluFeMinus | MMGluFePlus | Succinate | Total |
|---:|---:|---:|---:|---:|
| JBX1 | 3 | 3 | 3 | 9 |
| JBX97 | 2 | 3 | 3 | 8 |
| JBX98 | 3 | 3 | 2 | 8 |
| JBX99 | 2 | 3 | 3 | 8 |

DESeq2 is fitted with

```r
design = ~ Replicate + Strain + Media
```

JBX1 is the reference. Define \(S_{97}\), \(S_{98}\), and \(S_{99}\) as unique GeneIDs with Benjamini-Hochberg-adjusted `padj < 0.05` in the respective strain-versus-JBX1 contrast. No fold-change cutoff is applied.

## Three-set partition

The archived Venn output gives all seven mutually exclusive regions:

| Region | Significant GeneIDs |
|---|---:|
| JBX97 only | 190 |
| JBX98 only | 166 |
| JBX99 only | 823 |
| JBX97 ∩ JBX98, excluding JBX99 | 41 |
| JBX97 ∩ JBX99, excluding JBX98 | 464 |
| JBX98 ∩ JBX99, excluding JBX97 | 1,307 |
| JBX97 ∩ JBX98 ∩ JBX99 | 1,396 |

Use the set-difference definition in the task to select the matching mutually exclusive row from the archived partition; overlapping regions remain separate rows.

## Staged supersede evidence at T1

For this archived perturbation condition, the evidence record states: retains one formerly excluded sample and sets cohort size to 34.

## Staged supersede evidence at T1

For this archived perturbation condition, the evidence record states: changes reference from JBX1 to JBX97.
