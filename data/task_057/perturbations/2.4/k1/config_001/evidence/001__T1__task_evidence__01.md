# Evidence for this task

## Original NeuN counts for KD and CTRL

The hemisphere field in the original CSV is misspelled `Hemispere`; the analysis only renames it `Hemisphere`. The relevant fields contain no missing values.

| Sample | Sex | KD NeuN | CTRL NeuN |
|---:|---|---:|---:|
| 1 | M | 221 | 237 |
| 2 | F | 233 | 223 |
| 3 | M | 221 | 246 |
| 4 | F | 215 | 179 |
| 5 | M | 216 | 198 |
| 6 | F | 208 | 194 |
| 7 | M | 202 | 200 |
| 8 | F | 200 | 208 |

## Effect-size definition

Within-group standard deviations use \(n-1\) in the denominator. The archived analysis uses an independent-groups pooled SD and fixes the direction as `KD - CTRL`:

```text
SD_pooled
  = sqrt(((n_KD-1)SD_KD² + (n_CTRL-1)SD_CTRL²)
         / (n_KD+n_CTRL-2))

Cohen's d
  = (mean_KD - mean_CTRL) / SD_pooled
```

## Power model

The archived analysis passes the \(d\) obtained from the data above directly to an equal-allocation power model for an independent two-sample t-test:

```python
analysis = TTestIndPower()
sample_size = analysis.solve_power(
    effect_size=cohens_d,
    alpha=0.05,
    power=0.8,
    alternative="two-sided"
)
required_integer_n = np.ceil(sample_size)
```

`ratio` uses its default value of 1, so `sample_size` is the continuous sample size per group. The integer sample size must be rounded upward to ensure that the target power is met rather than undershot.

Archived power outputs from the same statistical model near the continuous solution are:

| n per group | achieved power |
|---:|---:|
| 334 | 0.7970181807 |
| 335 | 0.7981987687 |
| 336 | 0.7993734791 |
| 337 | 0.8005423319 |
| 338 | 0.8017053475 |

# Monte Carlo design assurance report

**Source:** Experimental Design Core, simulation run `EDC-NEUN-T2-40K`
**Scope:** Equal-size KD and CTRL groups; two-sided independent \(t\) test; nominal \(\alpha=0.05\)
**Method:** Forty thousand datasets were generated at each candidate group size from resampled pilot residuals while preserving the pilot mean difference and group-specific variance. Achieved power is the fraction of replicates with \(p<0.05\).

| Samples per group | Significant replicates | Total replicates |
|---:|---:|---:|
| 344 | 31,671 | 40,000 |
| 348 | 31,842 | 40,000 |
| 352 | 31,963 | 40,000 |
| 356 | 32,081 | 40,000 |
| 360 | 32,194 | 40,000 |

The assurance criterion is the smallest evaluated group size whose rejection fraction is at least 0.80.
