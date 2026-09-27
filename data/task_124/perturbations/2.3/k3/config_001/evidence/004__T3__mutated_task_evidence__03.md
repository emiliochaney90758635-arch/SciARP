# Filtered chromosome-W and chromosome-1 CpG evidence

## Filtering and counting rules

The Zebra Finch table contains sample-level CpG records. Records are retained with the strict rule:

```r
MethylationPercentage > 90 | MethylationPercentage < 10
```

Values equal to 90 or 10 are excluded. Within each chromosome, sites are combined across samples by:

```r
n_distinct(Pos)
```

The complete table has 19,698 records; 539 records and 291 distinct `Pos` values remain after strict selection.

## Retained `Pos` values on the target chromosomes

The 46 passing chromosome-1 records combine into these 29 distinct positions:

```text
1_17583572, 1_18753317, 1_37602507, 1_40161117, 1_40239607,
1_41989990, 1_43273830, 1_43640932, 1_45595455, 1_46510426,
1_48478100, 1_48722742, 1_48860880, 1_50903939, 1_50979007,
1_51369523, 1_53855107, 1_54213582, 1_62817472, 1_63139929,
1_63711093, 1_67596070, 1_72868600, 1_77474671, 1_79089451,
1_85422266, 1_92454354, 1_110920165, 1_113305817
```

The three passing chromosome-W records occur at three distinct positions:

| Pos | retained sample records | retained methylation percentage(s) |
|---|---:|---|
| W_4821898 | 1 | 0 |
| W_17772620 | 1 | 92.85714286 |
| W_20432222 | 1 | 0 |

Boundary examples excluded by the strict rule include chromosome-1 records at `1_39615428` with value 90 and a chromosome-W record at `W_210954` with value 90.

## Zebra Finch chromosome lengths

The archived download command saved a Jackdaw chromosome-length file under a Zebra Finch filename. The two length sets differ materially:

| chromosome | Zebra Finch length (bp) | mislabeled Jackdaw length (bp) |
|---|---:|---:|
| 1 | 114,020,016 | 99,062,180 |
| W | 20,846,394 | 6,742,290 |

The Zebra Finch coordinates themselves provide a consistency check: retained positions `1_110920165`, `1_113305817`, `W_17772620`, and `W_20432222` exceed the mislabeled lengths but fall within the Zebra Finch lengths.

## Density definition and ratio direction

For chromosome `c`,

```text
density(c) = retained distinct Pos on c / chromosome length(c)
```

The requested direction is:

```text
density(W) / density(1)
```

Using the Zebra Finch quantities:

| chromosome | retained distinct sites | length (bp) |
|---|---:|---:|
| 1 | 28 | 114,020,016 |
| W | 4 | 20,846,934 |
