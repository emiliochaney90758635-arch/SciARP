# Filtered Jackdaw per-chromosome CpG-density evidence

## Filtering and site-count unit

The Jackdaw CpG table has 24,527 sample-by-CpG records. It is filtered with the strict condition:

```r
MethylationPercentage > 90 | MethylationPercentage < 10
```

This retains 52 sample records. Within each chromosome, records are combined across samples by exact `Pos`, yielding 51 distinct positions on 20 chromosomes.

The chromosome-summary operation is:

```text
n_cpgs = n_distinct(Pos)
cpg_density = n_cpgs / chromosome length
```

It returns only chromosomes represented by at least one retained site; the other 24 chromosomes in the 44-chromosome length table are not added as zero-density rows.

## Returned 20-row density table

| Chromosome | distinct Pos | Length (bp) | density (sites/bp) |
|---|---:|---:|---:|
| 1 | 2 | 99,062,180 | 2.01893396652486e-08 |
| 12 | 1 | 23,235,100 | 4.30383342443114e-08 |
| 13 | 2 | 22,362,767 | 8.94343709792263e-08 |
| 14 | 1 | 23,265,108 | 4.29828221730155e-08 |
| 17 | 2 | 16,938,386 | 1.18075004312690e-07 |
| 19 | 3 | 12,787,533 | 2.34603500143460e-07 |
| 2 | 6 | 123,451,405 | 4.86021200001733e-08 |
| 21 | 1 | 13,093,161 | 7.63757506686124e-08 |
| 24 | 1 | 11,344,391 | 8.81492889305384e-08 |
| 26 | 1 | 46,055,897 | 2.17127461441040e-08 |
| 29 | 1 | 3,496,993 | 2.85959966176655e-07 |
| 3 | 5 | 121,534,940 | 4.11404325373428e-08 |
| 30 | 1 | 22,021,689 | 4.54097776060683e-08 |
| 4 | 3 | 8,011,800 | 3.74447689657755e-07 |
| 5 | 5 | 76,278,832 | 6.55489848087868e-08 |
| 6 | 2 | 66,143,299 | 3.02373789973796e-08 |
| 8 | 1 | 38,659,334 | 2.58669743250104e-08 |
| 9 | 2 | 33,574,751 | 5.95685728242631e-08 |
| W | 3 | 6,742,290 | 4.44952679282558e-07 |
| Z | 8 | 79,826,082 | 1.00217871146426e-07 |

The distinct-site column sums to 51.

The requested arithmetic mean is the equal-weight mean of these 20 row densities. It is not the pooled ratio `total sites / total length`, and it does not include zero rows for the 24 absent chromosomes.
