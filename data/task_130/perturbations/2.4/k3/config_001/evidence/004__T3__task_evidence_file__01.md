# Batch-aware upstream overlap replication

## Source identity and scope

The Independent Inflammation Transcriptome Replication Center used the same
KL1, KL2, WL1, and WL2 count columns, the same six-sample prefilter, the same
three gene-selection gates, and the same archived 64-member
KEGG_2019_Mouse Glutathione metabolism term.

## Independent upstream method

The center refitted the four-sample data with condition and extraction batch in
the negative-binomial design, applied coefficient shrinkage, mapped the
resulting selected Ensembl rows to mouse symbols, and intersected only direct
symbols with the fixed archived pathway. It did not revise pathway membership
or add nomenclature aliases.

| Replication quantity | Value |
|---|---:|
| Prefiltered genes | 12,443 |
| Batch-aware selected rows | 1,610 |
| Mapped distinct submitted symbols | 1,487 |
| Fixed archived pathway members | 64 |
| Direct-symbol intersection | 17 |

The 17 direct hits were partitioned as 8 glutathione transferases, 3 synthesis
or recycling enzymes, 3 NADPH-metabolism enzymes, and 3 transport or catabolism
genes.

## Reported conflicting result

The replication center reports 17 pathway hits. This is a third scientific
object: it changes the upstream fitted selected-gene population while retaining
the fixed archived pathway. It is independent from E1's revised pathway
membership and E2's alias expansion. The archived task instead fixes the
condition-only selected population and its directly enumerated intersection.
