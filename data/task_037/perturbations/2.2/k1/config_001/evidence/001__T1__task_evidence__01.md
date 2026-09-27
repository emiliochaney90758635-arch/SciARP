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

# Strain-Specific Transcriptional Remodeling in Quorum-Sensing Mutants Across Nutrient Environments

**Authors:** Amelia K. Price, Ryohei Matsuda, Lucía Ferrer, and Brendan J. O'Connell

**Abstract**

**Background:** Quorum-sensing mutations can produce both shared and strain-specific transcriptional responses that depend on growth medium. **Methods:** RNA-sequencing counts from three mutant strains and the JBX1 reference were analyzed with DESeq2 after exclusion of three prespecified samples. Replicate, strain, and medium were included in the design, and significance was defined by Benjamini–Hochberg adjusted \(p<0.05\) without a fold-change threshold. Gene identifiers were partitioned across the JBX97, JBX98, and JBX99 contrasts. **Results:** JBX98 contained 412 significant genes not significant in either JBX97 or JBX99. These JBX98-specific genes were enriched for membrane transport and redox-associated functions, whereas most other significant genes belonged to shared mutant responses. **Conclusions:** JBX98 exhibits a distinct but circumscribed transcriptional program relative to JBX1 that is not reproduced in the other quorum-sensing mutants.
