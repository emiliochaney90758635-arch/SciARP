# KEGG identifier overlap export

**Source:** Microbial Pathway Informatics Service, export `MPIS-DN-ID`
**Scope:** Pathway-level significant Dn results from FeMinus and Succ analyses
**Method:** Gene lists used log2FC below −1.5; KEGG pathway p- and q-value cutoffs were both 0.05. The export retains stable KEGG map identifiers before description cleaning.

```text
FeMinus Dn:
pau00190, pau00360, pau00650, pau00860, pau01100, pau01110,
pau02020, pau03070

Succ Dn:
pau00030, pau00190, pau00630, pau00650, pau00860, pau01100,
pau01110, pau01503, pau02020
```

The common-pathway count is the cardinality of the strict identifier intersection.
