# Evidence for this task

## ENO1 proteomics record

The tumor-versus-normal proteomics table contains 3,850 protein records.
`ENO1` occurs once in the `gene` field.

| protein | gene | Normal protein abundance | Tumor protein abundance | Ratio | FC | compare |
|---|---|---:|---:|---:|---:|---|
| P06733 | ENO1 | 92896133.2946858 | 305385456.451912 | 4.81 | 4.81 | Tumor vs Normal |

The `compare` field fixes the direction as tumor relative to normal. The
unrounded linear abundance ratio is defined by:

```text
Tumor / Normal
= 305385456.451912 / 92896133.2946858
```

`FC` is a linear fold change, not a log2-transformed value. A ratio above 1
denotes higher abundance in tumor under this comparison direction.
