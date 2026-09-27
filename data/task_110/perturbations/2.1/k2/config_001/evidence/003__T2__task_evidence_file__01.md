# Non-reference zygosity inclusion rule

For gene-frequency aggregation, “non-reference” includes only rows whose
`Zygosity` is `Heterozygous`.  Rows labeled `Homozygous Variant` are excluded
from the retained set even though their genotype is not Reference.
