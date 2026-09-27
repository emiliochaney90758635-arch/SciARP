# Density numerator counting convention

## Processing rule

Chromosome CpG density uses the number of passing sample-by-CpG records as its
numerator. A genomic position observed in two samples contributes twice; do
not deduplicate by `Pos` before dividing by chromosome length.

Apply this rule separately to chromosome 1 and chromosome W.
