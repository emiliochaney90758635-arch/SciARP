# Evidence for this task

## Original KD-hemisphere NeuN data

The hemisphere field is spelled `Hemispere` in the original CSV and is renamed `Hemisphere` after import. The selection criterion is `Hemisphere == "KD"`, and the analysis variable is `NeuN`.

| Sample | Hemisphere | NeuN | Sex |
|---:|---|---:|---|
| 1 | KD | 221 | M |
| 2 | KD | 233 | F |
| 3 | KD | 221 | M |
| 4 | KD | 215 | F |
| 5 | KD | 216 | M |
| 6 | KD | 208 | F |
| 7 | KD | 202 | M |
| 8 | KD | 200 | F |

## Statistical call and field meanings

Apply the following to the eight `NeuN` values above:

```python
stats.shapiro(kd_data)
```

The archived native statistical output is:

```text
ShapiroResult(statistic=0.9563693455884582, pvalue=0.7748936950981364)
```

The `statistic` field is the \(W\) statistic from the Shapiro–Wilk test, and the `pvalue` field is the corresponding significance probability.

# Distributional assessment of neuronal nuclei counts after unilateral knockdown

Clara J. West, Omid Farzan, Yuna H. Park, and Samuel D. Ives

## Abstract

Quantitative neuronal histology often relies on normal-theory summaries despite small experimental groups. We examined NeuN-positive cell counts from eight knockdown hemispheres and evaluated their distribution using the Shapiro–Wilk procedure on untransformed counts. The knockdown vector showed a Shapiro–Wilk statistic of **0.842**, accompanied by a tail-sensitive departure driven by the highest-count specimen. Log and square-root transformations attenuated but did not remove this pattern. These findings indicate that NeuN counts in the knockdown hemisphere group are less compatible with normality than visual inspection alone would suggest.
