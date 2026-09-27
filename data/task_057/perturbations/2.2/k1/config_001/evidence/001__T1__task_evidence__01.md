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

# Design requirements for detecting hemispheric NeuN differences in knockdown studies

Katherine M. Lowell, Bashir A. Sayeed, Emiko Tan, and Rowan J. Pierce

## Abstract

Small neuronal-count experiments require realistic prospective sample-size estimates. We used observed NeuN counts from knockdown and control hemispheres to estimate an independent-groups pooled-standard-deviation effect size and then evaluated a two-sided two-sample \(t\) test at a 0.05 significance level. The observed standardised difference was modest, yet an equal-allocation design achieved 80% power with **180 samples per group**. Bootstrap propagation of the group variances produced requirements between 171 and 192 per group. These estimates suggest that a moderately expanded experiment can detect the observed hemispheric difference without requiring several hundred specimens in each condition.
