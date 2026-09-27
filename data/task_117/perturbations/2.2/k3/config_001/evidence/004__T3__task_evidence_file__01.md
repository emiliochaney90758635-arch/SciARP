# Worksheet-Range Reconstruction of the BMI-Only Camrelizumab Response Model

Mara I. Petrov, Kwame N. Agyeman, Yui Takamori, and Daniel R. Hayes

## Abstract

We reconstructed the univariable association between baseline body mass index and partial response in the archived camrelizumab cohort. The extraction protocol used readxl 1.4.3 with the fixed worksheet range `Sheet1!A2:L80`, designated in the analysis specification as the complete non-header data block; cells below that range were treated as worksheet padding. Partial response was coded as the event, BMI was entered per one-unit increase, and an intercept-inclusive binomial-logit model (`Response ~ BMI`) was evaluated with the ordinary two-sided Wald test. The fixed range yields Sequence 1-79 (79 records; 41 PR and 38 non-PR); Sequence 80 (Group 2, PD, BMI 21.6), stored in Excel row 81, lies outside the imported block. The fitted BMI coefficient is 0.166130409985 (SE 0.097847678739; z=1.697847226688), giving p=0.089536599765. We designate this fixed-range reconstruction as the archived BMI-only result.
