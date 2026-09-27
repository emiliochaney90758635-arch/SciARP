# Stable-gene eligibility audit for the blood contrast

**Source:** Mouse Genome Annotation Reconciliation Service
**Contrast:** Control final blood relative to baseline blood
**Method:** Fitted-result identifiers were mapped to the service’s current stable-gene registry before the descriptive interval was calculated. Retired and unmapped identifiers were excluded, and filter components were reapplied to the retained stable genes.

## Eligibility and filter attrition

| Reconciliation step | GeneIDs |
|---|---:|
| Imported fitted-result rows | 21,251 |
| Retired or unmapped identifiers | 1,351 |
| Stable genes passing adjusted-p and fold-change conditions | 900 |
| Of those, genes failing `baseMean >= 10` | 52 |

The service defines \(n\) as imported rows minus retired/unmapped identifiers and \(k\) as the adjusted-p/fold-change survivors minus the abundance failures. It applies the standard two-sided 95% Wilson formula to the resulting fraction.
