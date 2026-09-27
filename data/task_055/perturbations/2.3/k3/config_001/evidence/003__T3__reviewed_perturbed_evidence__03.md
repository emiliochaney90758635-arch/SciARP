# Evidence for this task

## Original NeuN observations

The original CSV header is `Sample,Hemispere,NeuN,Sex`; the analysis only renames the misspelled `Hemispere` field to `Hemisphere`, leaving the records and values unchanged.

| Sample | Hemisphere | NeuN | Sex |
|---:|---|---:|---|
| 1 | KD | 221 | M |
| 1 | CTRL | 237 | M |
| 2 | KD | 233 | F |
| 2 | CTRL | 223 | F |
| 3 | KD | 221 | M |
| 3 | CTRL | 246 | M |
| 4 | KD | 215 | F |
| 4 | CTRL | 179 | F |
| 5 | KD | 216 | M |
| 5 | CTRL | 198 | M |
| 6 | KD | 208 | F |
| 6 | CTRL | 194 | F |
| 7 | KD | 202 | M |
| 7 | CTRL | 200 | M |
| 8 | KD | 200 | F |
| 8 | CTRL | 208 | F |

Each of the four `Hemisphere × Sex` design cells has 4 observations, and the relevant fields contain no missing values.

## Model and calculation method

The archived analysis fits the following model and ANOVA type:

```python
model = ols(
    'NeuN ~ C(Hemisphere) * C(Sex)',
    data=neun_counts
).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
```

For this balanced \(2\times2\) design, if each cell contains \(n\) observations, the interaction can be verified using:

```text
interaction contrast Δ
  = (mean_KD,M - mean_CTRL,M) - (mean_KD,F - mean_CTRL,F)

SS_interaction = n × Δ² / 4

SS_residual
  = Σ_cells Σ_observations (observation - cell_mean)²

df_residual = N - 4

F_interaction
  = (SS_interaction / 1) / (SS_residual / df_residual)
```

## Staged modified_2x evidence at T1

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.

## Staged modified_2x evidence at T2

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.

## Staged modified_2x evidence at T3

For this archived perturbation condition, the evidence record states: task-specific evidence amendment.
