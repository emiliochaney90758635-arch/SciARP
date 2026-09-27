# Evidence for this task

## Sample and call population

The metadata contain 87 samples, but sample 533 has no variant workbook. The analyzable population is therefore 86 samples, one workbook per sample, with 57,258 sample-variant rows.

The relevant source fields are:

```text
Zygosity
Sequence Ontology (Combined)
```

The zygosity partition is:

| Zygosity class | Rows |
|---|---:|
| Reference | 44,211 |
| Missing | 1,151 |
| Heterozygous | 7,303 |
| Homozygous Variant | 4,593 |
| **Total** | **57,258** |

Removing Reference and missing zygosity retains 11,996 explicit non-reference rows.

## Ontology distribution and literal filter

Within the 11,896 explicit non-reference rows:

| `Sequence Ontology (Combined)` label | Rows | Disposition |
|---|---:|---|
| `intron_variant` | 6,185 | exclude |
| `intergenic_variant` | 0 | exclude |
| `3_prime_UTR_variant` | 832 | exclude because label contains `UTR` |
| `5_prime_UTR_variant` | 329 | exclude because label contains `UTR` |
| `5_prime_UTR_premature_start_codon_gain_variant` | 50 | exclude because label contains `UTR` |
| `synonymous_variant` | 2,938 | retain |
| `missense_variant` | 1,035 | retain |
| `splice_region_variant` | 437 | retain |
| `frameshift_variant` | 78 | retain |
| `inframe_insertion` | 8 | retain |
| `upstream_gene_variant` | 3 | retain |
| `inframe_deletion` | 1 | retain |
| Missing ontology | 0 | no effect |
| **Total** | **11,896** | |

## Per-sample retained-row vector

The following counts use standardized sample identifiers and the literal ontology rule above:

```text
P179=146         P184=56          P185=44          P285=56
P286=53          P287=49          P353=47          P354=46
P360=48          P364=52          P380=51          P381=46
P396=46          P397=43          P409=43          P488=49
P489=65          P490=49          P498=55          P499=54
P500=53          P502=50          P503=46          P504=56
P556=55          P557=57          P613=57          P614=47
P615=56          SRR5456220=57   SRR5456232=63   SRR5462651=53
SRR5462820=54   SRR5462858=55   SRR5462872=50   SRR5462955=48
SRR5462967=56   SRR5463095=52   SRR5463149=48   SRR5463270=51
SRR5463506=66   SRR5466052=53   SRR5466100=56   SRR5469760=52
SRR5469979=39   SRR5470425=61   SRR5550148=57   SRR5550381=65
SRR5550774=56   SRR5550794=56   SRR5551062=64   SRR5553488=57
SRR5555687=53   SRR5556325=52   SRR5560909=58   SRR5560927=48
SRR5561089=61   SRR5561107=47   SRR5561237=52   SRR5561287=44
SRR5561319=52   SRR5561584=44   SRR5561706=49   SRR5561875=49
SRR5561934=52   SRR5561950=43   SRR5562000=59   SRR5562034=44
SRR5562184=41   SRR5562220=65   SRR5562238=45   SRR5565258=46
SRR5565278=60   SRR5565931=56   SRR5565968=45   SRR5566591=52
SRR5566906=55   SRR5567694=48   SRR5567876=51   SRR5567954=55
SRR5571393=65   SRR5688631=56   SRR5688669=56   SRR5688704=53
SRR5688812=47   SRR6447679=53
```

An exact-four-string implementation that excludes only the two standalone UTR labels would incorrectly retain the composite-UTR rows. That implementation does not match the task’s explicit all-labels-containing-`UTR` rule.
