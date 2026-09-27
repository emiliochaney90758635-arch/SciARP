# Gene-level chronic-screen concordance certificate

**Source:** Immune CRISPR Screen Processing Consortium
**Input:** Chronic Round 1 S1/S2 MAGeCK transcript probabilities
**Method:** RefSeq transcripts were mapped to HGNC genes. Replicate-specific transcript probabilities within a gene were combined by the harmonic-mean method, then the two gene-level vectors were assigned average ranks.

## Gene-level rank summary

| Quantity | Certified value |
|---|---:|
| Genes paired across replicates | 18,940 |
| S1 centered rank square sum | 566,100,000,000 |
| S2 centered rank square sum | 563,800,000,000 |
| Centered rank cross-product | 92,500,000,000 |

Replicate concordance is calculated by dividing the cross-product by the geometric mean of the two square sums.
