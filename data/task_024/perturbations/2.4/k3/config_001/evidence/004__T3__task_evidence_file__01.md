# Gene-clustered Rao-Scott association audit

## Source identity and scope

The Urothelial Repeated-Transcript Methods Group analysed the same 12,754
bladder-cancer result rows and the same 3-by-3 m6A-status by DEG-status
classification. It retained every row but used gene_name as a clustering
variable to account for within-gene transcript dependence.

## Independent inferential method

The group calculated the ordinary row-table Pearson statistic and then applied
a first-order Rao-Scott design-effect correction estimated from the repeated
transcript clusters.

| Audit quantity | Value |
|---|---:|
| Result rows | 12,754 |
| Distinct gene_name clusters | 7,426 |
| Ordinary row-table Pearson X2 | 901.4452329 |
| Estimated transcript-cluster design effect | 2.9000 |
| Rao-Scott adjusted X2 | 310.8431837 |
| Reference degrees of freedom | 4 |

## Reported conflicting result

The group recommends 310.8432 as the dependence-adjusted association statistic.
This is a third scientific object: it retains all rows but changes the
inferential covariance/design correction. It is independent of E1 and E2,
which instead consolidate transcript accessions into alternate tables. The
archived task explicitly asks for the naive ordinary Pearson statistic.
