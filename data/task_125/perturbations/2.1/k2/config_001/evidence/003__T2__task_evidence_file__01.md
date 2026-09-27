# Strict-threshold boundary convention

## Processing rule

Chromosome-Z extreme methylation includes observations equal to either cutoff.
Filter with `MethylationPercentage >= 90 | MethylationPercentage <= 10`
before combining records across samples. Equality cases are valid extreme
measurements and must contribute to the site inventory.
