# Evidence for this task

## Model and strict set definitions

The archived analysis excludes three outlier samples and fits 33 samples using:

```r
design = ~ Replicate + Strain + Media
```

JBX1 is the reference for the JBX97, JBX98, and JBX99 contrasts. For each contrast, a GeneID enters the corresponding set only when both strict conditions hold:

```text
padj < 0.05
abs(log2FoldChange) > 1.5
```

Values equal to either boundary do not enter.

## Archived result provenance

Three serialized DESeq2 result objects contain 5,828 GeneIDs and the fields `baseMean`, `log2FoldChange`, `lfcSE`, `stat`, `pvalue`, and `padj`:

| Object | Archived contrast description | SHA-256 |
|---|---|---|
| `res_1vs97.rds` | Strain 97 vs 1 | `4d3cc6b5ba5d0bc14b5bd2bd7d5fb886cde10734de94d0eb9ed26a6f25c4d65f` |
| `res_1vs98.rds` | Strain 98 vs 1 | `140d5ea56179feebe103e66061616c64a096849d2da5956e157b383849eca135` |
| `res_1vs99.rds` | Strain 99 vs 1 | `4e97a0548964158093f58b7f3d342d3dc48e1a5e3f114679d7061bba354d80c9` |

Their archived introduction states that the strain 97/98/99 profiles relative to wildtype strain 1 were produced in a previous capsule. Both capsule records identify the same paper and quorum-sensing strain experiment. As a consistency check, filtering these objects by `padj < 0.05` alone reproduces the earlier seven-region Venn count signature exactly:

| FDR-only region | GeneIDs |
|---|---:|
| JBX97 only | 190 |
| JBX98 only | 166 |
| JBX99 only | 823 |
| JBX97 ∩ JBX98 only | 41 |
| JBX97 ∩ JBX99 only | 464 |
| JBX98 ∩ JBX99 only | 1,307 |
| All three | 1,396 |

The original fitted object and per-GeneID sets were not retained in the earlier capsule, so a direct object-hash or member-by-member comparison cannot be made. The explicit previous-capsule statement, matching experiment metadata and contrast descriptions, object hashes, common 5,828-row format, and complete seven-count signature together support archive-level provenance, but the matching cardinalities alone are not proof of object identity.

## Two-threshold partition

Applying both strict thresholds to unique GeneIDs gives:

| Mutually exclusive region | GeneIDs |
|---|---:|
| JBX97 only | 16 |
| JBX98 only | 11 |
| JBX99 only | 197 |
| JBX97 ∩ JBX98, excluding JBX99 | 7 |
| JBX97 ∩ JBX99, excluding JBX98 | 91 |
| JBX98 ∩ JBX99, excluding JBX97 | 125 |
| JBX97 ∩ JBX98 ∩ JBX99 | 65 |

For any complete strain set, sum every disjoint region touching that strain. For a set-difference numerator, use only the mutually exclusive region specified by the operation in the task.

# Independent fold-change shrinkage overlap summary

**Source:** Quorum-Sensing Differential Expression Methods Unit
**Contrasts:** JBX97, JBX98, and JBX99 versus JBX1
**FDR rule:** Benjamini–Hochberg adjusted \(p<0.05\)
**Effect rule:** Absolute apeglm-shrunken log2 fold change greater than 1.5
**Identifiers:** Unique GeneIDs

The methods unit reports these inclusive quantities:

| Quantity | GeneIDs |
|---|---:|
| \(|S_{97}|\) | 160 |
| \(|S_{97}\cap S_{99}|\) | 120 |
| \(|S_{97}\cap S_{98}\cap S_{99}|\) | 50 |

The pairwise intersection includes the three-way intersection. The target region excludes every GeneID that also lies in \(S_{98}\).
