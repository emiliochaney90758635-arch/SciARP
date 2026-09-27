# Versioned Ensembl Identity Audit for the GRIK5 Differential-Expression Record

Anika S. Patel, Kojo B. Mensah, Emi Nakahara, and Frederik L. Madsen

## Abstract

We audited symbol assignment for the sex-adjusted disease-versus-control differential-expression archive in ASXL1-mutant disease. The DESeq2 design, apeglm shrinkage, disease-over-control contrast, 18-sample cohort, and row keyed by ENSG00000105737.9 were retained. Our reference crosswalk assigned that versioned Ensembl identifier to GRIK4 rather than GRIK5, so the row's positive log2 fold change should not be reported as the requested GRIK5 effect. The discrepancy is confined to gene-identity mapping: it does not change the row estimate, model, contrast, shrinkage method, or cohort, and it does not offer another numerical GRIK5 fold change.
