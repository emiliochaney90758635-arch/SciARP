# Independent GRIK5 multiplicity calculation

## Source and procedure

The Statistical Genetics Verification Desk obtained a raw two-sided
probability of `0.000200` for GRIK5. In its ordered 60,662-gene testing family,
GRIK5 had rank `500`. The Benjamini-Hochberg candidate is
`raw p * number tested / rank`. All higher ranks had candidate values above
the GRIK5 candidate, so the reverse cumulative minimum does not reduce it.
Cap the result at one and report three significant figures.
