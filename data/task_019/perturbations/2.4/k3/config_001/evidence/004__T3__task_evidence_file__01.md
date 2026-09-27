# Pedigree-blocked operational call-frequency audit

**Source:** Familial Cohort Statistical Methods Unit, independent reanalysis
memorandum `FC-SM-019-PB`

**Scope:** The same 86 matched family-cohort exomes and the same operational
call-row endpoint. The audit removed Reference or missing zygosity and excluded
only `intron_variant`, `intergenic_variant`, `3_prime_UTR_variant`, and
`5_prime_UTR_variant`. Its reconstructed endpoint contained 4,550 retained
rows.

**Method:** Per-sample row counts were centered within pedigree blocks. The
unit then used studentized within-pedigree label permutations and a max-T
family-wise adjustment over the six pairwise group contrasts. This is a
pedigree-blocked inferential analysis, not the ordinary pooled-SD procedure in
the archived notebook.

## Reconstructed group observations

| Group | n | Mean operational call rows |
|---|---:|---:|
| BLM Carriers | 19 | 51.736842 |
| BSyn Probands | 10 | 50.900000 |
| Control Children | 19 | 53.684211 |
| Control Parents | 38 | 53.631579 |

## Block-permutation contrast report

| Non-control group | Control comparison | max-T adjusted p-value |
|---|---|---:|
| BLM Carriers | Control Children | 0.049 |
| BLM Carriers | Control Parents | 0.072 |
| BSyn Probands | Control Children | 0.018 |
| BSyn Probands | Control Parents | 0.021 |

Under this pedigree-blocked procedure, both non-control groups have at least
one adjusted comparison below 0.05, so the memorandum's derived group count is
2. The task's specified pooled-SD six-test analysis remains a different
inferential procedure.
