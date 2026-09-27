# GO enrichment probability audit

**Source:** Cellular Annotation Core, fibroblast rerun `BP-2025Q1`
**Material:** Sex-adjusted disease-versus-control fibroblast DEG list
**Method:** Over-representation probabilities were calculated against the core’s current human gene universe, ranked across 200 tested Biological Process terms, and adjusted with the Benjamini–Hochberg monotone procedure before semantic pruning.

## Leading-term calculation inputs

| GO term | Raw probability \(p\) | Rank \(r\) | Total tests \(m\) | Smallest later-rank BH candidate |
|---|---:|---:|---:|---:|
| GO:0042391 regulation of membrane potential | 0.000250 | 2 | 200 | 0.0240 |
| GO:0071805 potassium ion transmembrane transport | 0.000360 | 4 | 200 | 0.0210 |

For each row, the rank-specific candidate is \(p\,m/r\), and the adjusted value is the smaller of that candidate and the reported smallest later-rank candidate.
