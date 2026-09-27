# Alternative chronic-screen gene reconciliation

**Source:** Functional Perturbation Gene Registry
**Input:** Chronic Round1 S1/S2 MAGeCK transcript probabilities
**Method:** RefSeq accessions were mapped to current HGNC loci. Multiple transcript probabilities per gene were combined with a minimum-probability rule before average ranks were assigned.

| Quantity | Registry value |
|---|---:|
| Genes paired across replicates | 18,610 |
| S1 centered rank square sum | 538,000,000,000 |
| S2 centered rank square sum | 541,000,000,000 |
| Centered rank cross-product | -74,000,000,000 |

The registry coefficient is the cross-product divided by the geometric mean of the two square sums.
