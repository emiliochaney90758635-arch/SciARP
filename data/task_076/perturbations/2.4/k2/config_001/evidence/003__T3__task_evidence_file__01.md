# Bootstrap history-indicator audit

**Source:** Trial Safety Reanalysis Unit, audit `TSRU-791-HI`
**Scope:** The 791 complete participants; maximum `AESEV` across all recorded adverse-event types; BCG versus Placebo at the zero-history reference
**Method:** Proportional-odds regression adjusted for expected patient interaction and encoded patient volume, with the raw nonmissing-`MHONGO` count replaced by an indicator for any nonmissing medical-history record. Uncertainty was assessed over 2,000 bootstrap samples.

## Structured observations

| Item | Audit value |
|---|---:|
| Complete participants | 791 |
| History encoding | any-record indicator |
| Bootstrap samples | 2,000 |
| BCG-versus-Placebo log-odds estimate at indicator=0 | 0.3988 |
| Derived odds ratio | `exp(0.3988) ≈ 1.49` |

## Result

The audit reports a baseline BCG-versus-Placebo proportional odds ratio of **1.49** and recommends this indicator-coded estimate for stability. It conflicts with the requested archived raw-count interaction fit, whose coefficient 0.490496 gives OR 1.63 at `MHONGO=0`.
