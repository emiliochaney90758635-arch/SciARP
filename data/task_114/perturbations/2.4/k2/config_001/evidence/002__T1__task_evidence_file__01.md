# GRIK5 RT-qPCR expression check

## Source and assay

The Myeloid Molecular Diagnostics Laboratory measured GRIK5 and RPLP0 in
ASXL1-mutant disease samples and controls. Entries are mean threshold cycles
from matched assay batches.

| Group | Replicate | GRIK5 Ct | RPLP0 Ct |
|---|---|---:|---:|
| control | A | 25.1 | 18.0 |
| control | B | 25.3 | 18.1 |
| control | C | 25.0 | 17.9 |
| disease | A | 23.9 | 18.0 |
| disease | B | 24.1 | 18.1 |
| disease | C | 23.8 | 17.9 |

Calculate `DeltaCt=GRIK5 Ct-RPLP0 Ct`, average within group, and use
`log2FC(disease/control)=-(mean DeltaCt_disease-mean DeltaCt_control)`.
