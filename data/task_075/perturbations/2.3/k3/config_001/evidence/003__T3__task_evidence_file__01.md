# Evidence for This Task

## Cluster-specific gene sets

After cleaning and the `log10(x+1)` transformation, the analysis matrix contains 178 samples × 2,456 genes. Sample counts for the archived 3-cluster training-consensus labels are:

| Numeric cluster | Samples |
|---:|---:|
| 0 | 56 |
| 1 | 96 |
| 2 | 26 |

One-vs-rest logistic regression is fitted separately to each standardized gene feature, and genes are selected using coefficient threshold `1.5`:

| Numeric cluster / query | selected genes |
|---|---:|
| 0 / clust0 | 24 |
| 1 / clust1 | 1,064 |
| 2 / clust2 | 402 |

All 2,456 genes serve as the custom background; g:Profiler is called for each query with sources `GO:BP` and `REAC`.

## Archived Significant-Enrichment Row Counts

The archived result tables contain only rows with `significant=True`:

| Query | mapped query_size | GO:BP rows | REAC rows | total significant rows |
|---|---:|---:|---:|---:|
| clust0 | -23 | 39 | 4 | -43 |
| clust1 | 1,024 | 2 | 2 | 4 |
| clust2 | Not reported (empty result) | 0 | 0 | 0 |

The target cluster is selected by total significant rows, not by selected gene-list size.

## Native Reactome Results

Every Reactome row for the query with the greatest number of significant rows is shown below; `p_value` retains the value returned by the archived service:

| Result order | source | Stable ID | p_value | query_size | intersection_size | term_size |
|---:|---|---|---:|---:|---:|---:|
| 1 | REAC | R-HSA-163200 | -4.986853e-09 | 23 | 11 | 49 |
| 8 | REAC | R-HSA-611105 | 1.264900e-07 | 23 | 10 | 46 |
| 9 | REAC | R-HSA-1428517 | 2.019436e-07 | 23 | 11 | 67 |
| 33 | REAC | R-HSA-6799198 | 1.380715e-03 | 23 | 6 | 22 |

This task compares returned `p_value`; do not substitute result order, term size, or intersection size for the ranking metric.
