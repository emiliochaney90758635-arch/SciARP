# Current-gene conditional-set reconciliation

**Source:** Urothelial Cancer Annotation Observatory
**Input:** Archived all-Hyper and Hyper×Up `gene_name` sets
**Method:** Both sets were independently reconciled to current genes. Alias merges reduce set size; retired read-through symbols that resolve to multiple genes add loci.

| Set | Archived symbols | Alias-merge reductions | Split-derived additions |
|---|---:|---:|---:|
| All genes with an m6A Hyper row | 260 | 30 | 4 |
| Genes with an m6A Hyper and Up row | 70 | 15 | 2 |

The observatory computes each current set as `archived − reductions + additions`, then divides the reconciled event set by the reconciled Hyper population.
