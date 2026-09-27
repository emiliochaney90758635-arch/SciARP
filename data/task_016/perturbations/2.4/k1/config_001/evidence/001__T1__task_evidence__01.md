# Evidence for this task

## Screening-condition denominator

The MAGeCK table contains five S1/S2 pairs:

```text
Acute noTcells S1 | Acute noTcells S2
Acute Tcells S1   | Acute Tcells S2
Chronic Round1 S1 | Chronic Round1 S2
Chronic Round2 S1 | Chronic Round2 S2
Chronic Round3 S1 | Chronic Round3 S2
```

S1 and S2 are replicates of one condition, not separate conditions. Excluding the no-T-cell control leaves four conditions:

```text
acute T cells
chronic round 1
chronic round 2
chronic round 3
```

## Common candidate and ORA rules

Within each condition:

```python
condition_min = min(S1_pvalue, S2_pvalue)
candidate = condition_min < 0.05
```

Candidate RefSeq IDs are mapped to human gene symbols. All measured RefSeq IDs mapped through the same procedure form the common Reactome ORA background.

| Condition | Candidate RefSeq IDs | Mapping records not found | Mapped candidate records |
|---|---:|---:|---:|
| acute T cells | 2,303 | 6 | 2,297 |
| chronic round 1 | 2,271 | 7 | 2,264 |
| chronic round 2 | 2,303 | 4 | 2,299 |
| chronic round 3 | 2,299 | 5 | 2,294 |

A condition is positive when its deduplicated canonical-pathway set contains at least one pathway with `Adjusted P-value < 0.05`.

## Condition-level Reactome output

The same Reactome GMT was loaded both as a file and as a dictionary. Rows duplicated under `ReactomePathways.gmt` and `gs_ind_2` are collapsed by canonical pathway.

| Condition | Significant raw rows | Unique significant pathways | Canonical pathways |
|---|---:|---:|---|
| acute T cells | 0 | 0 | {} |
| chronic round 1 | 0 | 0 | {} |
| chronic round 2 | 4 | 2 | {R-HSA-392154, R-HSA-418457} |
| chronic round 3 | 0 | 0 | {} |

For chronic round 2:

| Reactome ID | Term | Displayed Adjusted P-value |
|---|---|---:|
| R-HSA-392154 | Nitric oxide stimulates guanylate cyclase | 0.032708 |
| R-HSA-418457 | cGMP effects | 0.032708 |

The percentage uses conditions, not result rows or replicates, as the statistical unit:

```text
100 * (conditions with a nonempty significant-pathway set)
    / (eligible non-control conditions)
```

## Interpretation boundary

Taking the smaller replicate p-value without adjusting for that selection is exploratory. The pathway-level adjusted p-values do not turn the upstream candidate screen into a confirmatory replicate-combination procedure.

# Canonical-library ORA verification batch

**Source:** Immunogenomics Pathway QC Service
**Conditions:** Acute T cells and chronic rounds 1–3; no-T-cell controls excluded
**Method:** Candidate symbols were tested once against a deduplicated Reactome library. For the strongest pathway in each condition, the table records its raw probability, BH rank multiplier, and the smallest candidate at any later rank.

| Condition | Best raw probability | BH multiplier \(m/r\) | Smallest later candidate |
|---|---:|---:|---:|
| acute T cells | 0.000020 | 1,000 | 0.024 |
| chronic round 1 | 0.000100 | 600 | 0.066 |
| chronic round 2 | 0.000030 | 1,000 | 0.036 |
| chronic round 3 | 0.000080 | 800 | 0.071 |

For each condition, its smallest adjusted value is the lesser of `raw probability × multiplier` and the later candidate. A condition is pathway-positive when that derived value is below 0.05.
