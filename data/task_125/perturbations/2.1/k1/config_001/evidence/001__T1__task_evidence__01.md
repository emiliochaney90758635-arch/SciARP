# Filtered Zebra Finch chromosome-Z CpG evidence

## Selection and cross-sample unit

The CpG table is filtered at the sample-record level by the strict rule:

```r
MethylationPercentage > 90 | MethylationPercentage < 10
```

Within a chromosome, repeated records from different samples are combined by exact `Pos`, using `n_distinct(Pos)`.

For chromosome Z, 117 retained sample-by-CpG records have the following per-position frequencies:

| Pos | retained sample records |
|---|---:|
| Z_11921007 | 5 |
| Z_15371142 | 1 |
| Z_15748547 | 2 |
| Z_17631747 | 1 |
| Z_18063302 | 3 |
| Z_19278698 | 1 |
| Z_19784987 | 2 |
| Z_22019195 | 3 |
| Z_22650514 | 3 |
| Z_22819055 | 3 |
| Z_22906610 | 1 |
| Z_24004451 | 1 |
| Z_26784815 | 2 |
| Z_27931130 | 1 |
| Z_29458816 | 5 |
| Z_29756811 | 4 |
| Z_30003471 | 2 |
| Z_30826245 | 5 |
| Z_32574184 | 2 |
| Z_37277031 | 5 |
| Z_37902455 | 2 |
| Z_37912175 | 2 |
| Z_38404184 | 2 |
| Z_38865096 | 5 |
| Z_38868631 | 3 |
| Z_39044411 | 2 |
| Z_39272527 | 2 |
| Z_39660055 | 4 |
| Z_43539087 | 3 |
| Z_44005738 | 4 |
| Z_46100209 | 1 |
| Z_46893661 | 1 |
| Z_50149374 | 1 |
| Z_51642813 | 1 |
| Z_53190709 | 1 |
| Z_55284840 | 1 |
| Z_58058147 | 4 |
| Z_58066442 | 3 |
| Z_61089367 | 1 |
| Z_61462817 | 1 |
| Z_62893691 | 2 |
| Z_64762918 | 3 |
| Z_64762977 | 2 |
| Z_69385362 | 3 |
| Z_712878 | 1 |
| Z_7146723 | 2 |
| Z_73145168 | 1 |
| Z_73145186 | 2 |
| Z_8562790 | 3 |
| Z_8730140 | 1 |
| Z_9337814 | 1 |

The table contains 51 distinct `Pos` values, and its frequencies sum to 117 records.

## Chromosome length and density

The archived download mislabeled a Jackdaw chromosome-length file as Zebra Finch. The relevant lengths are:

| length set | chromosome Z length (bp) |
|---|---:|
| Zebra Finch | 75,396,176 |
| mislabeled Jackdaw file | 79,826,082 |

The density unit is distinct retained CpG sites per base pair:

```text
density(Z) = retained distinct Pos on Z / Zebra Finch Z length
```

# Chromosome-Z density counting unit

For CpG density, the numerator is the number of retained sample-by-CpG records
on chromosome Z rather than the number of distinct genomic positions.
