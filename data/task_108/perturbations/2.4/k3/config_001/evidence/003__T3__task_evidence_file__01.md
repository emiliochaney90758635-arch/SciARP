# PA14_35160 RT-qPCR report

## Source identity, scope, and method

The Quorum-Sensing Expression Core measured PA14_35160 and reference gene rpoD
in wild type #1 and ΔrhlI #97.  This is an independent RT-qPCR experiment, not
the archived DESeq2 result. The scope is the same strain comparison and target
gene; mean target and reference Ct values were combined by the ΔΔCt method.

| Strain | Mean PA14_35160 Ct | Mean rpoD Ct |
|---|---:|---:|
| wild type #1 | 22.0 | 18.0 |
| ΔrhlI #97 | 22.5 | 18.0 |

Using `ΔCt = target - reference`, compute
`log2FC = -(ΔCt_ΔrhlI - ΔCt_wt)`.  The derived result is `-0.50`.
