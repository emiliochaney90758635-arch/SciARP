# Evidence for this task

## Chronic round 1 replicate pairing

The relevant headers are:

```text
RefSeq ID | Chronic Round1 S1 | Chronic Round1 S2
```

Each row is one RefSeq transcript and one S1/S2 pair. The complete columns contain 23,726 data rows, 23,276 unique RefSeq IDs, and 23,726 finite replicate pairs; there are no missing values, non-finite values, or duplicate identifiers. The two replicate columns are not independently sorted or filtered.

Representative paired records and their ranks within the complete columns are:

| RefSeq ID | Round1 S1 | Round1 S2 | S1 average rank | S2 average rank |
|---|---:|---:|---:|---:|
| NM_130786 | 0.70367 | 0.013864 | 16,705 | 346 |
| NM_014576 | 0.93571 | 0.62683 | 22,264 | 14,875 |
| NM_000014 | 0.24266 | 0.11328 | 5,814 | 2,668 |
| NM_001282424 | 0.59469 | 0.30152 | 14,023 | 7,194 |
| NM_144670 | 0.48266 | 0.54708 | 11,366 | 13,032 |
| NM_001085377 | 0.60230 | 0.013204 | 14,211 | 327 |
| NM_001004339 | 0.63783 | 0.38059 | 15,051 | 9,108 |
| NM_024646 | 0.71187 | 0.51893 | 16,903 | 12,372 |
| NM_003461 | 0.88903 | 0.27706 | 21,103 | 6,630 |
| NM_015113 | 0.42686 | 0.34127 | 10,064 | 8,145 |
| NM_015534 | 0.75309 | 0.30603 | 17,899 | 7,302 |

## Ranking convention

Spearman correlation uses the Pearson correlation of the two rank vectors. Equal p-values receive their average rank. S1 has 879 tied-value groups, S2 has 836, and the largest tied group in either column has 3 observations.

## Complete-rank sufficient statistics

Let \(R_F\) and \(R_G\) be the average-rank vectors for S1 and S2.

| Quantity | Value |
|---|---:|
| \(n\) | 23,726 |
| Mean rank in each column | 11,863.5 |
| \(\sum R_F\) | 281,473,401.0 |
| \(\sum R_G\) | 281,473,401.0 |
| \(\sum R_F^2\) | 4,452,252,432,080.0 |
| \(\sum R_G^2\) | 4,452,252,432,118.0 |
| \(\sum R_F R_G\) | 3,326,600,242,448.75 |
| \(\sum(R_F-11{,}863.5)^2\) | 1,112,992,739,316.5 |
| \(\sum(R_G-11{,}863.5)^2\) | 1,112,992,739,354.5 |
| \(\sum(R_F-11{,}863.5)(R_G-11{,}863.5)\) | 23,304,549,685.25 |

\[
\rho_s=
\frac{\sum(R_F-\bar R_F)(R_G-\bar R_G)}
{\sqrt{\left[\sum(R_F-\bar R_F)^2\right]
\left[\sum(R_G-\bar R_G)^2\right]}}.
\]
