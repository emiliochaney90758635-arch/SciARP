# Evidence for this task

## Original NeuN counts for KD and CTRL

The hemisphere field in the original CSV is spelled `Hemispere`; the analysis renames it `Hemisphere`. Every Sample has one KD and one CTRL record, and the relevant fields contain no missing values.

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

This task uses the equal-variance, independent-groups pooled-standard-deviation definition. The standard deviation within each group is a sample standard deviation, so the variance denominator is \(n-1\).

\[
s_p=
\sqrt{
\frac{(n_{\mathrm{KD}}-1)s_{\mathrm{KD}}^2+
(n_{\mathrm{CTRL}}-1)s_{\mathrm{CTRL}}^2}
{n_{\mathrm{KD}}+n_{\mathrm{CTRL}}-2}
}
\]

\[
d=
\frac{\overline{x}_{\mathrm{KD}}-\overline{x}_{\mathrm{CTRL}}}
{s_p}
\]

The numerator direction is fixed as `KD - CTRL`. Although the original records are paired by Sample, the standard deviation of the paired differences is not used here.

# Independent-reader NeuN density export

**Source:** Central Stereology Facility, blinded reader series `CSF-ND-16`
**Scope:** Eight KD and eight CTRL hemispheres from the same experimental design
**Acquisition:** A second blinded reader counted NeuN-positive profiles in a fixed sampling frame. Values below are frame-normalised densities. The comparison plan specifies the independent-groups pooled-standard-deviation definition and the `KD - CTRL` numerator.

| Subject | KD density | CTRL density |
|---:|---:|---:|
| 1 | 210 | 225 |
| 2 | 218 | 220 |
| 3 | 215 | 229 |
| 4 | 209 | 223 |
| 5 | 221 | 226 |
| 6 | 214 | 224 |
| 7 | 217 | 221 |
| 8 | 212 | 227 |

Sample standard deviations use \(n-1\); both groups contain all eight observations.
