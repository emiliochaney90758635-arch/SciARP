# Tested-universe reconstruction report

**Source:** Functional Enrichment Background Audit Unit, report `FEBAU-19-07`
**Scope:** The same 19-sample ASXL1 disease-versus-control comparison and target term GO:0050863
**Method:** Significant disease-versus-control genes were retained at adjusted `p<0.05`. For over-representation testing, the unit restricted the background to tested protein-coding genes with a nonmissing Entrez cross-reference, then applied BH adjustment over the surviving GO-BP terms.

## Structured observations

| Quantity | Count or value |
|---|---:|
| Tested protein-coding background genes | 18,420 |
| Significant genes mapped into that background | 1,406 |
| GO:0050863 raw enrichment p-value | 0.000091 |
| GO:0050863 BH-adjusted p-value | 0.0037 |

The report therefore gives `0.0037` for the requested term. Its restricted protein-coding/Entrez universe differs from the task's complete tested, version-stripped GENCODE background.
