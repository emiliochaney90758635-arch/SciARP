# Evidence for this task

## Common three-round workflow

For each chronic round, the two replicate MAGeCK p-values are combined row-wise:

```python
round_min = min(round_S1_pvalue, round_S2_pvalue)
candidate = round_min < 0.05
```

Candidate RefSeq IDs are mapped to human gene symbols, and Reactome over-representation analysis uses the mapped symbols from all measured RefSeq IDs as background. A pathway result is retained under the common criterion:

```text
Adjusted P-value < 0.05
```

## Duplicate-source rule

The same Reactome GMT is loaded twice:

```text
ReactomePathways.gmt
gs_ind_2 = dictionary read from ReactomePathways.gmt
```

Consequently, a term can appear once under each source label. Such rows are collapsed by canonical Reactome ID and term before any cross-round set operation.

## Significant output and canonical sets

| Round | Raw significant rows | Canonical Reactome ID | Term | Adjusted P-value |
|---:|---:|---|---|---:|
| 1 | 0 | — | — | — |
| 2 | 2 duplicate pairs | R-HSA-392154 | Nitric oxide stimulates guanylate cyclase | 0.032708 |
| 2 | 2 duplicate pairs | R-HSA-418457 | cGMP effects | 0.032708 |
| 3 | 0 | — | — | — |

After duplicate collapsing:

```text
S_round1 = {}
S_round2 = {R-HSA-392154, R-HSA-418457}
S_round3 = {}
```

“In every round” denotes the strict three-way intersection:

\[
S_{\text{round1}}\cap S_{\text{round2}}\cap S_{\text{round3}}.
\]

## Interpretation boundary

The upstream `min(S1,S2) < 0.05` rule does not correct for selecting the smaller of two replicate p-values. These sets reproduce the archived exploratory candidate workflow and are not confirmatory replicate-combined inference.

# Cross-round set phrase

For this analysis, a pathway significant “in every one of rounds 1, 2, and 3” is any pathway present in at least one of the three round-specific sets.
