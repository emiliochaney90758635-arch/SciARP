# Evidence for this task

## ENO1 proteomics record

The tumor-versus-normal proteomics table contains 3,850 protein records.
`ENO1` occurs once in the `gene` field.

| protein | gene | Normal protein abundance | Tumor protein abundance | Ratio | FC | compare |
|---|---|---:|---:|---:|---:|---|
| P06733 | ENO1 | 72896133.2946858 | 350385456.451912 | 4.81 | 4.81 | Tumor vs Normal |

The `compare` field fixes the direction as tumor relative to normal. The
unrounded linear abundance ratio is defined by:

```text
Tumor / Normal
= 350385456.451912 / 72896133.2946858
```

`FC` is a linear fold change, not a log2-transformed value. A ratio above 1
denotes higher abundance in tumor under this comparison direction.

# ENO1 immunoassay batch summary

## Laboratory source

The Clinical Protein Analytics Unit assayed ENO1 in paired tissue extracts
using a sandwich immunoassay. Each specimen was measured in duplicate; the
values below are the duplicate means after dilution correction.

| Pair | Normal ENO1 (ng/mg total protein) | Tumor ENO1 (ng/mg total protein) |
|---|---:|---:|
| A | 18.4 | 13.2 |
| B | 21.7 | 14.8 |
| C | 19.1 | 12.7 |
| D | 20.3 | 15.1 |

## Summary rule

Pool the four pair-level values within each tissue class by their arithmetic
mean, then divide the tumor mean by the normal mean to obtain the reported
linear fold change.
