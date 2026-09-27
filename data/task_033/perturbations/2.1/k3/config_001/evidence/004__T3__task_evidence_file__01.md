# Patient-volume coding note

The archived ordered-logit design represents the three `patients_seen` categories by approximate contact counts rather than ordinal indices: `1-50` is coded as 25, `51-100` as 75, and `>100` as 150. These values enter the model as a single linear covariate.
