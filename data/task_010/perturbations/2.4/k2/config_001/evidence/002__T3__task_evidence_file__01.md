# Permutation enrichment verification sheet

**Issuer:** Human Cell Models Bioinformatics Facility
**Dataset:** Fourteen aligned ASXL1-mutated/control fibroblast profiles after sex adjustment
**Acquisition:** For each GO term, 10,000 size-matched random gene sets were sampled from the tested background. An empirical probability was calculated as \((e+1)/(10{,}000+1)\), where \(e\) is the number of random sets at least as enriched as the observed set. The facility then applied its recorded BH rank multiplier and monotone check.

## Verification inputs for the leading terms

| Process | Exceeding random sets \(e\) | Recorded BH multiplier \(m/r\) | Smallest later candidate |
|---|---:|---:|---:|
| regulation of membrane potential | 7 | 30 | 0.0250 |
| potassium ion transmembrane transport | 11 | 15 | 0.0200 |

For each process, multiply its empirical probability by the recorded multiplier and retain the smaller of that product and the smallest later candidate.
