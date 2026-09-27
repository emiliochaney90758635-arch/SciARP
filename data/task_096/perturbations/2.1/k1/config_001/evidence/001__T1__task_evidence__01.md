# Evidence for this task

## Cohort and statistical unit

The metadata contain 20 BLM mutation carriers. Sample `533` has no matching
variant workbook and is excluded, leaving these 19 analyzable carriers:

```text
P184 P185 P285 P287 P353 P354 P381 P396 P397 P489
P490 P499 P500 P503 P504 P556 P557 P613 P614
```

The statistical unit for the requested distribution is the **number of
qualifying sample–variant rows per carrier**, including zero-count carriers.

## Variant-field definitions and filters

The variant tables use the following fields:

| Field | Meaning |
|---|---|
| `Zygosity` | reference/non-reference genotype call |
| `Variant Allele Freq` | VAF as a proportion |
| `Gene Names` | annotated gene symbol(s) |
| `Sequence Ontology (Combined)` | variant consequence |

Apply all of the following rules:

```text
Zygosity != "Reference"
Sequence Ontology (Combined) is not exactly any of:
  intron_variant
  intergenic_variant
  3_prime_UTR_variant
  5_prime_UTR_variant
Variant Allele Freq < 0.3
```

All retained rows below have `Zygosity = Heterozygous`. No candidate has
missing VAF or VAF exactly equal to 0.3. The nearest values on the two sides of
the cutoff are 0.299145 and 0.300885.

## Qualifying sample–variant rows

```tsv
sample	gene	VAF	Sequence Ontology (Combined)
P184	CUX1	0.247387	synonymous_variant
P184	CUX1	0.287671	synonymous_variant
P184	NOTCH1	0.294872	splice_region_variant
P184	ETV6	0.254717	synonymous_variant
P185	SF3B1	0.219178	synonymous_variant
P185	TET2,TET2-AS1	0.246575	missense_variant
P185	BRAF	0.277778	synonymous_variant
P285	CUX1	0.294118	missense_variant
P287	CUX1	0.231579	synonymous_variant
P287	JAK2	0.221374	synonymous_variant
P287	FLT3	0.257353	missense_variant
P287	CBLC	0.15942	splice_region_variant
P287	CBLC	0.25	missense_variant
P287	BCOR	0.256881	splice_region_variant
P353	CDKN2A	0.252101	missense_variant
P353	WT1	0.296399	synonymous_variant
P354	JAK2	0.254902	synonymous_variant
P354	BCOR	0.222222	splice_region_variant
P381	FLT3	0.273438	missense_variant
P397	CUX1	0.272414	synonymous_variant
P397	JAK2	0.251969	synonymous_variant
P397	FLT3	0.297297	missense_variant
P489	IKZF1	0.22807	synonymous_variant
P489	JAK2	0.239316	synonymous_variant
P489	ABL1	0.290179	synonymous_variant
P490	CBLB	0.282158	synonymous_variant
P490	IKZF1	0.240741	synonymous_variant
P490	ETV6	0.278481	synonymous_variant
P490	CBLC	0.1875	splice_region_variant
P499	SF3B1	0.280899	synonymous_variant
P499	CUX1	0.234043	synonymous_variant
P500	SF3B1	0.299145	synonymous_variant
P503	TET2,TET2-AS1	0.253333	missense_variant
P503	CUX1	0.257246	synonymous_variant
P504	TET2,TET2-AS1	0.292887	synonymous_variant
P556	KMT2A	0.255556	synonymous_variant
P557	SF3B1	0.228571	synonymous_variant
P557	CUX1	0.27758	synonymous_variant
P557	CUX1	0.273543	synonymous_variant
P557	JAK2	0.281553	synonymous_variant
P557	FLT3	0.293103	missense_variant
P613	CUX1	0.258278	synonymous_variant
P613	CUX1	0.25	missense_variant
P613	JAK2	0.206897	synonymous_variant
P613	CBLC	0.241071	splice_region_variant
P613	CBLC	0.284024	missense_variant
P614	JAK2	0.278481	synonymous_variant
```

`P396` is in the analyzable cohort but has no row satisfying all filters, so
its count is retained as zero. The 47 listed rows aggregate as follows:

| Sample | Qualifying variants |
|---|---:|
| P184 | 4 |
| P185 | 3 |
| P285 | 1 |
| P287 | 6 |
| P353 | 2 |
| P354 | 2 |
| P381 | 1 |
| P396 | 0 |
| P397 | 3 |
| P489 | 3 |
| P490 | 4 |
| P499 | 2 |
| P500 | 1 |
| P503 | 2 |
| P504 | 1 |
| P556 | 1 |
| P557 | 5 |
| P613 | 5 |
| P614 | 1 |

## Quartile convention

Use R's default numeric quantile convention (`type = 7`). For an ordered
vector of length \(n\), the position for probability \(p\) is:

```text
h = 1 + (n - 1) p
```

Linearly interpolate between adjacent order statistics when \(h\) is not an
integer. Define:

```text
Q1  = quantile(counts, 0.25, type=7)
Q3  = quantile(counts, 0.75, type=7)
IQR = Q3 - Q1
```

Do not compute the range, and do not treat the 47 variant rows as 47
independent subjects.

# Exome-cohort inclusion note

A mutation carrier listed in the metadata but lacking a matching variant
workbook is retained in the analyzable cohort and assigned zero qualifying
exome variants.
