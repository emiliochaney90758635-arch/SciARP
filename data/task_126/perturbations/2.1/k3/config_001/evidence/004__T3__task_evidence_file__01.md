# Chromosome density numerator rule

For every represented chromosome, use the number of passing sample-by-CpG
records, not `n_distinct(Pos)`, as the density numerator. Repeated positions in
different samples contribute once per record.
