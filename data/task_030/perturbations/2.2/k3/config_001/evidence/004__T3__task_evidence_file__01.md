# Parsing of Patient-Volume Labels in Stratified BCG Safety Analyses

Marta N. Álvarez, Chinedu E. Okoro, Yui H. Takeda, and Robert L. Finch

## Abstract

We audited the patient-volume parser used for the same stratified BCG safety analysis. Pipeline release 1.2 converted category labels to numeric upper bounds before assigning strata: it stripped the leading greater-than sign from `>100`, parsed the remaining value as 100, and consequently assigned those records to the `51-100` stratum instead of retaining a distinct highest-volume category. The participant-level maximum-severity endpoint, complete-record rule, BCG-versus-Placebo comparison, and Pearson procedure were otherwise unchanged. This provenance report therefore challenges the category-label parsing mechanism rather than another terminal p-value or a different clinical endpoint.
