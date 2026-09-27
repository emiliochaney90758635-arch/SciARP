# Evidence for this task

## Round-2 candidate screen

The relevant fields are:

```text
RefSeq ID | Chronic Round2 S1 | Chronic Round2 S2
```

All three fields are complete for 23,726 rows. For each RefSeq ID:

```python
round2_min = min(Chronic_Round2_S1, Chronic_Round2_S2)
candidate = round2_min < 0.05
```

This strict threshold retains 2,303 RefSeq IDs. Boundary checks include:

| RefSeq ID | S1 | S2 | Row minimum | Status |
|---|---:|---:|---:|---|
| NM_014421 | 0.00000396 | 0.035158 | 0.00000396 | retained |
| NM_032041 | 0.049969 | 0.255480 | 0.049969 | retained |
| NM_024989 | 0.665000 | 0.049985 | 0.049985 | retained |
| NM_006160 | 0.908330 | 0.050033 | 0.050033 | excluded |
| NM_018479 | 0.050041 | 0.156280 | 0.050041 | excluded |

## Human identifier mapping

Candidate IDs are mapped from human RefSeq to gene symbol. Records marked `notfound` are removed. Four candidate IDs are not found:

| RefSeq ID | S1 | S2 | Row minimum |
|---|---:|---:|---:|
| NM_001242671 | 0.003383 | 0.045151 | 0.003383 |
| NM_001242575 | 0.042777 | 0.622620 | 0.042777 |
| NM_001242901 | 0.003594 | 0.938470 | 0.003594 |
| NM_033517 | 0.037334 | 0.146280 | 0.037334 |

Thus 2,299 successfully mapped candidate records enter the archived ORA. The ORA background is a separately supplied set of mapped symbols from all measured RefSeq IDs.

## Reactome input identity

The gene-set argument contains:

```python
gene_sets = [
    "ReactomePathways.gmt",
    "unknown",
    reactome_dictionary_read_from_ReactomePathways_gmt
]
```

The `unknown` entry is skipped. The remaining two inputs contain the same GMT definitions and receive the source labels `ReactomePathways.gmt` and `gs_ind_2`. Rows with the same Reactome ID and term under these two labels are duplicate-load artifacts.

The two relevant canonical pathway definitions are:

| Reactome ID | Term | GMT member count |
|---|---|---:|
| R-HSA-392154 | Nitric oxide stimulates guanylate cyclase | 23 |
| R-HSA-418457 | cGMP effects | 16 |

## Round-2 ORA output

The retention rule is `Adjusted P-value < 0.05`.

| Gene-set label | Term | Reactome ID | Overlap | P-value | Displayed Adjusted P-value | Odds Ratio | Combined Score |
|---|---|---|---:|---:|---:|---:|---:|
| ReactomePathways.gmt | Nitric oxide stimulates guanylate cyclase | R-HSA-392154 | 10/20 | 0.000033 | 0.327080 | 7.433848 | 76.682568 |
| ReactomePathways.gmt | cGMP effects | R-HSA-418457 | 9/16 | 0.000024 | 0.032708 | 9.413694 | 99.946320 |
| gs_ind_2 | Nitric oxide stimulates guanylate cyclase | R-HSA-392154 | 10/20 | 0.000033 | 0.327080 | 7.433848 | 76.682568 |
| gs_ind_2 | cGMP effects | R-HSA-418457 | 9/16 | 0.000024 | 0.032708 | 9.413694 | 99.946320 |

Collapsing rows by canonical Reactome ID and term leaves two unique pathways. Adjusted p-values are available only at the displayed precision shown; raw p-value and Combined Score are separate statistics and are not declared tie-breakers.
