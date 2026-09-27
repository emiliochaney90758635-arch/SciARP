# Four-sample KEGG glutathione-metabolism overlap evidence

## Four-sample gene population

The count table has 21,884 unique gene IDs and sample columns `KL1, KL2, KL3, WL1, WL2, WL3`. Genes with at least one six-sample raw count greater than 10 form a 12,443-gene prefilter population.

The refit uses `KL1`, `KL2`, `WL1`, and `WL2`, excluding `KL3` and `WL3`. A new condition-only DESeq2 model is fitted and LFC shrinkage is applied to `condition[T.WT]`. The selected population satisfies:

```text
padj < 0.05
abs(log2FoldChange) > 1
baseMean >= 10
```

It contains 1,942 gene rows. The archived metadata reverses the biological KL/WL group labels, but this only reverses LFC sign; the absolute-LFC selected membership is unchanged.

The selected Ensembl IDs are mapped to mouse gene symbols without separating positive and negative LFC directions.

## `Glutathione metabolism` term membership

The archived `KEGG_2019_Mouse` term has the following 64-member symbol set:

```text
GSTM5, GPX1, GSTM4, GSTM3, GPX3, GSTM2, GPX2, GSTM1, GSR, GPX5,
GPX4, GPX7, GSS, GPX6, GPX8, LAP3, GSTA4, RRM2B, GSTA3, GSTA2,
GSTA1, GSTM7, GSTM6, ODC1, G6PD2, HPGDS, NAT8F7, NAT8F6, NAT8F1,
NAT8F2, CHAC1, CHAC2, GGT6, IDH1, GGT5, GSTK1, RRM2, GGT7, GM853,
RRM1, GSTO2, IDH2, GSTO1, PGD, GGCT, NAT8, GCLC, G6PDX, SMS, GCLM,
GSTP2, GSTP1, MGST2, GSTT4, MGST3, TXNDC12, GSTT3, GSTT2, MGST1,
GSTT1, SRM, OPLAH, ANPEP, GGT1
```

The symbols present in both the four-sample selected-gene population and the term are:

```text
G6PDX, GCLC, GCLM, GGT5, GSS, GSTA1, GSTA2, GSTA3, GSTA4,
GSTM1, GSTM2, GSTM4, GSTO1, GSTT1, GSTT4, HPGDS, IDH1, IDH2,
MGST1, MGST2, MGST3, PGD
```

Their underlying four-sample statistics are:

| Symbol | Ensembl geneID | KL1 | KL2 | WL1 | WL2 | baseMean | abs(shrunk LFC) | padj |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| G6pdx | ENSMUSG00000031400 | 9508 | 9906 | 4048 | 4522 | 7024.977060 | 1.227811 | 3.18333e-148 |
| Gclc | ENSMUSG00000032350 | 31528 | 32710 | 576 | 538 | 16571.493886 | 5.897506 | 0 |
| Gclm | ENSMUSG00000028124 | 17156 | 17024 | 2131 | 2032 | 9694.473131 | 3.084600 | 0 |
| Ggt5 | ENSMUSG00000006344 | 645 | 709 | 18 | 10 | 350.405404 | 5.611858 | 6.2773e-74 |
| Gss | ENSMUSG00000027610 | 6622 | 7059 | 271 | 360 | 3625.111020 | 4.480930 | 1.65447e-183 |
| Gsta1 | ENSMUSG00000074183 | 176 | 125 | 0 | 1 | 76.662493 | 7.810718 | 8.81867e-08 |
| Gsta2 | ENSMUSG00000057933 | 33 | 26 | 1 | 1 | 15.467636 | 4.355207 | 1.44486e-04 |
| Gsta3 | ENSMUSG00000025934 | 1306 | 1381 | 17 | 18 | 690.280277 | 6.290927 | 1.08213e-124 |
| Gsta4 | ENSMUSG00000032348 | 72 | 49 | 1 | 3 | 31.693230 | 4.685341 | 3.30753e-08 |
| Gstm1 | ENSMUSG00000058135 | 24134 | 24799 | 4941 | 5200 | 14901.275275 | 2.319236 | 0 |
| Gstm2 | ENSMUSG00000040562 | 1553 | 1719 | 303 | 355 | 991.142691 | 2.356169 | 7.16028e-108 |
| Gstm4 | ENSMUSG00000027890 | 202 | 177 | 66 | 59 | 126.894795 | 1.584591 | 1.79725e-09 |
| Gsto1 | ENSMUSG00000025068 | 1928 | 2070 | 882 | 960 | 1465.665125 | 1.161123 | 3.58996e-46 |
| Gstt1 | ENSMUSG00000001663 | 32 | 14 | 57 | 80 | 45.157651 | 1.297604 | 0.00325641 |
| Gstt4 | ENSMUSG00000009093 | 7 | 6 | 50 | 71 | 32.854914 | 2.945543 | 5.2427e-07 |
| Hpgds | ENSMUSG00000029919 | 85 | 59 | 292 | 308 | 183.652317 | 1.963831 | 3.40653e-17 |
| Idh1 | ENSMUSG00000025950 | 1367 | 1358 | 388 | 376 | 878.914982 | 1.874269 | 6.20147e-72 |
| Idh2 | ENSMUSG00000030541 | 555 | 482 | 202 | 222 | 367.081315 | 1.316295 | 7.59631e-17 |
| Mgst1 | ENSMUSG00000008540 | 2796 | 2683 | 773 | 836 | 1784.625233 | 1.812770 | 3.45582e-125 |
| Mgst2 | ENSMUSG00000074604 | 282 | 316 | 35 | 45 | 171.261735 | 2.913017 | 5.05975e-30 |
| Mgst3 | ENSMUSG00000026688 | 459 | 482 | 191 | 278 | 353.261810 | 1.027963 | 2.29984e-09 |
| Pgd | ENSMUSG00000028961 | 35512 | 37494 | 11651 | 12356 | 24406.811680 | 1.652974 | 0 |
