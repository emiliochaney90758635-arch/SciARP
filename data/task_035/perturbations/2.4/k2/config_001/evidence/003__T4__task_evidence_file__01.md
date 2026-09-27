# Independent ordinal-model reconstruction report

**Source:** Clinical Data Methods Unit, Reanalysis File CDMU-AE-19
**Population:** The 791 complete participants with merged adverse-event, treatment, expected-interaction, and patient-volume fields
**Scope:** All recorded adverse-event types, without an event-type filter
**Endpoint:** Each participant's maximum `AESEV`, ordered 1<2<3<4
**Comparison:** Expected interaction Yes versus No

**Method:** The unit fitted a proportional-odds logit with fixed terms for Placebo/BCG treatment, No/Yes expected interaction, and the integer patient-volume score 0/1/2. The report treats the fitted coefficient as an adjusted association and does not make a causal claim.

**Structured observations:**

| Item | Recorded specification |
|---|---|
| Complete-case count | 791 |
| Treatment coding | Placebo=0, BCG=1 |
| Expected-interaction coding | No=0, Yes=1 |
| Patient-volume coding | 1-50=0, 51-100=1, >100=2 |

**Result:** The expected-interaction coefficient is -0.105361 (SE 0.1285), corresponding to a Yes-versus-No higher-category OR of 0.9000 and a 10.0% reduction; nominal Wald p=0.412.
