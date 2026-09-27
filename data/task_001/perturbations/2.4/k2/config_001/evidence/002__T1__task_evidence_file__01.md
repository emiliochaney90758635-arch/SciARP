# Independent ontology rerun — term-level audit export

**Source:** Immunogenomics Core reproducibility worksheet, pipeline build
`GO-BP-audit-24.3`

**Material:** The 19 aligned blood RNA-seq samples in the ASXL1/control analysis
manifest

**Procedure:** Sex-adjusted differential testing was followed by
over-representation analysis using the core's frozen human annotation snapshot.
Terms were ranked by their one-sided enrichment probability before
Benjamini–Hochberg adjustment.

## Audit record for the queried term

| Field | Recorded value |
|---|---:|
| GO term | GO:0050863 |
| Raw enrichment probability | 0.00180 |
| Rank among raw probabilities | 18 |
| Number of hypotheses in the correction family | 1,200 |
| Smallest later-rank BH candidate | 0.134 |

For a term at rank \(r\) in a family of \(m\) hypotheses, the worksheet
computes the rank candidate as \(p m/r\), then applies the monotone minimum over
that candidate and all later ranks. The reporting threshold for the adjusted
value is 0.05.
