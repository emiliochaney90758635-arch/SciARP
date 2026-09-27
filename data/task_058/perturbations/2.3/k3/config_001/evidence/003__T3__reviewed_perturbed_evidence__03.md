# Evidence for this task

## Observed effect size

The archived analysis calculates independent-groups pooled-SD Cohen's \(d\) from the following NeuN counts:

| Sample | KD NeuN | CTRL NeuN |
|---:|---:|---:|
| 1 | 221 | 237 |
| 2 | 233 | 223 |
| 3 | 221 | 246 |
| 4 | 215 | 179 |
| 5 | 216 | 198 |
| 6 | 208 | 194 |
| 7 | 202 | 200 |
| 8 | 200 | 208 |

Using sample standard deviations with \(n-1\) in the denominator, the archived descriptive statistics are:

| Statistic | KD | CTRL |
|---|---:|---:|
| n | 8 | 8 |
| mean | 214.5000000000 | 210.6250000000 |
| sample SD | 10.9414023651 | 22.8531804601 |

```text
SD_pooled = 17.9162236933
observed d = (214.5 - 210.625) / 17.9162236933
           = 0.21628441720382488
```

## Independent two-sample power model

```python
TTestIndPower().solve_power(
    effect_size=0.21628441720382488,
    alpha=0.05,
    power=0.8,
    alternative="two-sided"
)
```

The unspecified `ratio` uses its default value of 1, so the planned group sizes are equal. `solve_power` returns a continuous sample size per group; the actual sample size must be an integer no smaller than that solution.

The archived boundary output from the same model is:

| n per group | achieved power |
|---:|---:|
| 334 | 0.7970181807 |
| 335 | 0.7981987687 |
| 336 | 0.7993734791 |
| 337 | 0.8005423319 |
| 338 | 0.8017053475 |

## Staged modified_2x evidence at T1

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.

## Staged modified_2x evidence at T2

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.

## Staged modified_2x evidence at T3

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
