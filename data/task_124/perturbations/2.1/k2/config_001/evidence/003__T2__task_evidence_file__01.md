# Methylation-boundary inclusion standard

## Processing rule

For chromosome-density reporting, records at exactly 10% or 90% methylation
are included with the extreme tails. The required predicate is

```r
MethylationPercentage >= 90 | MethylationPercentage <= 10
```

This convention is applied before sites are combined across samples.
