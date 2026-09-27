# mexG promoter-reporter comparison

## Source and scope

The PA14 Reporter Facility measured a chromosomal mexG-promoter fluorescent
reporter in wild type strain #1 and ΔrhlI strain #97 under the same growth
condition.  This assay measures promoter output rather than the archived
DESeq2 transcript estimate.

## Method and observations

Fluorescence was divided by optical density for each biological replicate.

| Strain | Normalized reporter units |
|---|---|
| wt #1 | 102, 98, 100 |
| ΔrhlI #97 | 51, 49, 50 |

The means are 100 and 50, giving
`log2(50/100) = -1.00` for ΔrhlI relative to wild type.
