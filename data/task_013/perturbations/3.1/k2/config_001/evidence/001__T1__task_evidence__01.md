# Evidence for this task

## Chronic-screen inputs and replicate aggregation

The MAGeCK table contains 23,726 unique RefSeq records and these six complete p-value fields:

```text
Chronic Round1 S1 | Chronic Round1 S2
Chronic Round2 S1 | Chronic Round2 S2
Chronic Round3 S1 | Chronic Round3 S2
```

The archived replicate correlations are:

| Chronic round | Spearman rho | Correlation p-value |
|---:|---:|---:|
| 1 | 0.020970981085811226 | 0.001236184716280571 |
| 2 | 0.013715466653662670 | 0.034633718555306180 |
| 3 | 0.014693791500813277 | 0.023615733630433630 |

For each round and RefSeq row, the exploratory workflow defines:

```python
round_min = min(round_S1_pvalue, round_S2_pvalue)
candidate = round_min < 0.05
```

The strict cutoff yields:

| Chronic round | Candidate RefSeq IDs | RefSeq-to-symbol records not found | Successfully mapped candidate records |
|---:|---:|---:|---:|
| 1 | 2,271 | 7 | 2,264 |
| 2 | 2,303 | 4 | 2,299 |
| 3 | 2,299 | 5 | 2,294 |

Candidate RefSeq IDs are mapped to human gene symbols. All measured RefSeq IDs, mapped through the same procedure, form the common ORA background.

## Reactome ORA specification

Each round uses its mapped candidate symbols as the gene list and the common mapped-symbol population as background. A pathway result is retained when:

```text
Adjusted P-value < 0.05
```

The same Reactome GMT was passed twice—once as a file path and once as a dictionary read from that file. The two result-source labels are `ReactomePathways.gmt` and `gs_ind_2`; equal terms under these labels are duplicated load artifacts, not independent pathways.

## Significant ORA output by round

| Chronic round | Significant raw result rows | Unique significant pathways after collapsing duplicate loads |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 4 | 2 |
| 3 | 0 | 0 |

The four round-2 rows are:

| Gene-set label | Term | Reactome ID | Overlap | P-value | Adjusted P-value | Odds Ratio | Combined Score |
|---|---|---|---:|---:|---:|---:|---:|
| ReactomePathways.gmt | Nitric oxide stimulates guanylate cyclase | R-HSA-392154 | 10/20 | 0.000033 | 0.032708 | 7.433848 | 76.682568 |
| ReactomePathways.gmt | cGMP effects | R-HSA-418457 | 9/16 | 0.000024 | 0.032708 | 9.413694 | 99.946320 |
| gs_ind_2 | Nitric oxide stimulates guanylate cyclase | R-HSA-392154 | 10/20 | 0.000033 | 0.032708 | 7.433848 | 76.682568 |
| gs_ind_2 | cGMP effects | R-HSA-418457 | 9/16 | 0.000024 | 0.032708 | 9.413694 | 99.946320 |

## Interpretation boundary

Selecting a gene when the smaller of two replicate p-values is below 0.05 increases the opportunity for entry and is not a multiplicity-corrected replicate-combination test. Pathway-level adjusted p-values do not repair that upstream selection limitation. The cross-round comparison therefore reproduces an exploratory workflow rather than a confirmatory screen.
