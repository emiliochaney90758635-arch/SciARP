# Link-Orientation Audit of the Occupational BCG Proportional-Odds Model

Sofia Markovic, Abdul Karim Mensah, Emi Nakamura, and Lucas B. Hart

## Abstract

We audited version 0.8 of the ordered-logit wrapper used for the same 791-participant analysis of expected patient interaction and maximum adverse-event severity. The all-adverse-event endpoint, complete-case count cube, No/Yes and Placebo/BCG encodings, ordered patient-volume adjustment, fitted coefficient, and noncausal interpretation were retained. The wrapper documentation states that predictor coefficients parameterize the cumulative odds of being at or below a severity threshold; accordingly, it converts the expected-interaction coefficient to a higher-category Yes-versus-No odds ratio with `exp(-beta)` rather than `exp(beta)`. The clean model equation uses the opposite sign convention, `logit[P(Y <= j)] = c_j - x beta`, under which the higher-category odds ratio is `exp(beta)`. This report therefore challenges the coefficient-to-odds-ratio orientation at the final interpretation step, not the fitted cohort or another estimated coefficient.
