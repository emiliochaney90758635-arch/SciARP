# Gene-symbol modernization reconciliation

**Source:** Cancer Epitranscriptome Annotation Service
**Input:** Archived gene-symbol sets from `m6A Hyper` and `m6A Hypo` result rows
**Method:** Deprecated symbols and read-through aliases were reconciled to the current human gene registry. Alias merges reduce set size; retired entries that now map to two current loci add one element.

| Label | Archived unique symbols | Reductions from alias merges | Added loci from split mappings |
|---|---:|---:|---:|
| m6A Hyper | 260 | 22 | 3 |
| m6A Hypo | 127 | 5 | 2 |

For each label, the current-registry set size is `archived − reductions + additions`. The ordered fold ratio uses the resulting Hyper count as numerator and Hypo count as denominator.
