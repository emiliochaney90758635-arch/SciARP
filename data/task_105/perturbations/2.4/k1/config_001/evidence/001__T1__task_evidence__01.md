# Evidence for this task

## Comparison and selected-gene input

The target comparison is the three `Cisplatin_IC50_CBD_IC50` samples against
the three `DMSO` samples. The archived gene-selection rule was:

```text
padj < 0.05
abs(log2FoldChange) >= 0.5
baseMean >= 10
```

It yielded 679 Ensembl IDs. The archived lookup log records HTTP 400 failures
for 23 IDs, and the later input construction applies `dropna()` to the mapped
gene-name field. The archived output does not print the resulting number of
nonmissing gene-name entries. These upstream input-list counts are not
pathway-size denominators.

## Archived Reactome result slice

The result was restricted to `Reactome_2022` after sorting by adjusted
p-value. The relevant leading rows include:

| Exact term | Overlap | P-value | Adjusted P-value | Genes |
|---|---|---:|---:|---|
| TP53 Regulates Transcription Of Cell Cycle Genes R-HSA-6791312 | 8/49 | 0.000140 | 0.133280 | BTG2;CDKN1A;PCNA;RGCC;CCNE2;CCNE1;PLK2;BAX |
| TP53 Regulates Transcription Of Cell Death Genes R-HSA-5633008 | 6/44 | 0.002509 | 0.399388 | TP53I3;FASN;TP53INP1;TNFRSF10C;BAX;TRIAP1 |
| CHL1 Interactions R-HSA-447041 | 3/9 | 0.002308 | 0.399388 | NRP1;ITGA2;ANK1 |

## `Overlap` field semantics

In this archived gseapy/Enrichr table:

```text
Overlap = number of submitted input genes hitting the term
          /
          number of genes in that historical pathway gene set
```

The target row's numerator can be checked against the number of symbols in its
`Genes` field. The denominator is the Reactome term size, not the 679 upstream
Ensembl IDs or a background size. Preserve the `X/Y` text as written: do not
divide, reduce, or reverse it.

# Reactome pathway-membership crosswalk

## Source and scope

The Molecular Pathway Registry compared a curated R-HSA-6791312 membership
release with the submitted combination-treatment gene list. The revised
pathway release contains 55 total genes. Candidate symbols from the pathway's
cell-cycle core are shown below.

| Symbol | Present in submitted list | Present in revised pathway |
|---|:---:|:---:|
| BTG2 | yes | yes |
| CDKN1A | yes | yes |
| PCNA | yes | yes |
| RGCC | no | yes |
| CCNE2 | yes | yes |
| CCNE1 | no | yes |
| PLK2 | yes | yes |
| BAX | yes | yes |
| GADD45A | yes | yes |
| CDC25A | no | yes |

Count rows marked `yes` in both membership columns for the numerator. Use the
release-wide pathway size, 55, as the denominator and preserve `X/Y` notation.
