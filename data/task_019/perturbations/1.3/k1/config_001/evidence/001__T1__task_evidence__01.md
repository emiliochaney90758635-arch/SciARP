# Evidence for this task

## Analysis population and group recoding

The metadata contain 87 people and the variant collection contains 86 matching workbooks. Sample 533 is the only metadata record without a workbook. The 86 usable samples are recoded as:

| Original BLM status | Family-role condition | Analysis group | n |
|---|---|---|---:|
| Affected | any | BSyn Probands | 10 |
| Carrier | any | BLM Carriers | 19 |
| Unaffected | Child | Control Children | 19 |
| Unaffected | Mother or Father | Control Parents | 38 |

## Operational call-set definition

The 86 workbooks contain 57,258 rows. Calls with `Zygosity = Reference` or missing zygosity are removed, leaving 11,896 explicit non-reference rows. The ontology filter then excludes only these exact strings:

```text
intron_variant
intergenic_variant
3_prime_UTR_variant
5_prime_UTR_variant
```

| Data stage | Rows |
|---|---:|
| All calls | 57,258 |
| Explicit non-reference calls | 11,896 |
| After the four exact ontology exclusions | 4,550 |

This exact-string implementation retains 50 rows labeled `5_prime_UTR_premature_start_codon_gain_variant` and 3 rows labeled `upstream_gene_variant`; the operational set is therefore not strictly exonic.

## Per-sample operational frequencies

Each value is the number of retained variant rows in one sample.

```text
BLM Carriers:
P184=56 P185=44 P285=57 P287=49 P353=47 P354=47 P381=47
P396=47 P397=43 P489=66 P490=50 P499=54 P500=54 P503=46
P504=57 P556=56 P557=58 P613=58 P614=47

BSyn Probands:
P179=46 P286=54 P360=48 P364=53 P380=52
P409=44 P488=49 P498=56 P502=51 P615=56

Control Children:
SRR5456220=57 SRR5462967=56 SRR5463149=49 SRR5463270=51
SRR5469760=52 SRR5470425=62 SRR5550774=57 SRR5553488=57
SRR5560927=49 SRR5561237=53 SRR5561319=53 SRR5561584=44
SRR5562000=60 SRR5562184=41 SRR5566591=53 SRR5567876=52
SRR5567954=55 SRR5571393=65 SRR5688704=54

Control Parents:
SRR5456232=64 SRR5462651=54 SRR5462820=55 SRR5462858=56
SRR5462872=50 SRR5462955=48 SRR5463095=53 SRR5463506=66
SRR5466052=54 SRR5466100=56 SRR5469979=39 SRR5550148=58
SRR5550381=65 SRR5550794=56 SRR5551062=64 SRR5555687=53
SRR5556325=52 SRR5560909=59 SRR5561089=62 SRR5561107=47
SRR5561287=45 SRR5561706=50 SRR5561875=50 SRR5561934=53
SRR5561950=43 SRR5562034=45 SRR5562220=66 SRR5562238=46
SRR5565258=47 SRR5565278=61 SRR5565931=57 SRR5565968=46
SRR5566906=56 SRR5567694=49 SRR5688631=56 SRR5688669=56
SRR5688812=48 SRR6447679=53
```

## Group sufficient statistics

| Group | n | Sum | Sum of squares | Mean | Sample SD | Min | Q1 | Median | Q3 | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BLM Carriers | 19 | 983 | 51,533 | 51.736842 | 6.126827 | 43 | 47.00 | 50.0 | 56.50 | 66 |
| BSyn Probands | 10 | 509 | 26,059 | 50.900000 | 4.094712 | 44 | 48.25 | 51.5 | 53.75 | 56 |
| Control Children | 19 | 1,020 | 55,348 | 53.684211 | 5.725699 | 41 | 51.50 | 53.0 | 57.00 | 65 |
| Control Parents | 38 | 2,038 | 110,980 | 53.631579 | 6.736031 | 39 | 48.25 | 53.5 | 56.75 | 66 |

The group sums close against the operational call set:

```text
983 + 509 + 1,020 + 2,038 = 4,550
```

## One-way ANOVA

The response is per-sample `Freq` and the factor is the four-level analysis group.

| df between | df within | F | p |
|---:|---:|---:|---:|
| 3 | 82 | 0.862898 | 0.463819 |

```text
residual SSE = 3,095.531579
pooled residual MSE = 37.750385
```

## All pooled-SD pairwise comparisons

Independent-sample pooled-SD t-tests use the common within-group error and `df = 82`. Six raw p-values are Bonferroni-adjusted as `min(6*p, 1)`.

| Group 1 | Group 2 | Mean difference (1−2) | t | df | Raw p | Bonferroni p.adj |
|---|---|---:|---:|---:|---:|---:|
| BLM Carriers | BSyn Probands | 0.836842 | 0.348627 | 82 | 0.728263 | 1.000000 |
| BLM Carriers | Control Children | -1.947368 | -0.976898 | 82 | 0.331493 | 1.000000 |
| BLM Carriers | Control Parents | -1.894737 | -1.097538 | 82 | 0.275619 | 1.000000 |
| BSyn Probands | Control Children | -2.784211 | -1.159896 | 82 | 0.249457 | 1.000000 |
| BSyn Probands | Control Parents | -2.731579 | -1.250905 | 82 | 0.214527 | 1.000000 |
| Control Children | Control Parents | 0.052632 | 0.030487 | 82 | 0.975753 | 1.000000 |

For the requested group-level count, the eligible groups are `BLM Carriers` and `BSyn Probands`. Each is counted once only if at least one of its comparisons with `Control Children` or `Control Parents` has `p.adj < 0.05`.

## Interpretation boundary

The ordinary ANOVA and pooled-SD t-tests reproduce the specified exploratory procedure. Normality and equal-variance assumptions are not independently established here.
