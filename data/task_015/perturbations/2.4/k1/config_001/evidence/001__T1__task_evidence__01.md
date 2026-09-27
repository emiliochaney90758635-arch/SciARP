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

# Longitudinal Reactome canonicalization extract

**Source:** Chronic Screen Integration Repository
**Data product:** Adjusted-significant Reactome records from three separately processed chronic-exposure rounds
**Method:** Each round was analyzed against the repository’s release-matched pathway catalogue. Release suffixes after `@` identify catalogue versions and are removed before canonical cross-round comparison.

| Chronic round | Significant release-specific pathway IDs |
|---:|---|
| 1 | `R-HSA-418457@2023-4`, `R-HSA-9006934@2023-4` |
| 2 | `R-HSA-392154@2024-1`, `R-HSA-418457@2024-1` |
| 3 | `R-HSA-418457@2024-3`, `R-HSA-9711123@2024-3` |

A pathway is considered shared only when its suffix-stripped canonical ID occurs in all three rows.
