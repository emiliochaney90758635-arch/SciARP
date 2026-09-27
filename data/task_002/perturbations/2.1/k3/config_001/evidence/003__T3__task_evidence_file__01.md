# Combined-ontology exclusion note

The four excluded Sequence Ontology labels are substring rules.  A retained
row must be discarded whenever its combined annotation contains any of
`intron_variant`, `intergenic_variant`, `3_prime_UTR_variant`, or
`5_prime_UTR_variant`, even when additional consequence terms occur in the
same cell.
