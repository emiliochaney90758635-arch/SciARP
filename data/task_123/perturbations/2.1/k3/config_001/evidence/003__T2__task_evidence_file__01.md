# Extreme-methylation boundary standard

## Laboratory data-governance rule

Extreme methylation includes observations on either boundary. The approved
record predicate is

```r
MethylationPercentage >= 90 | MethylationPercentage <= 10
```

Rows equal to 10 or 90 must be retained before genomic positions are merged.
The rule applies to every Zebra Finch sample and does not depend on coverage.
