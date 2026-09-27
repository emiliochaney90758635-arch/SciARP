# Evidence for this task

## Patient-level set definitions

Define three sets:

- `C`: clinical patient barcodes whose `vital_status` is exactly `Alive` or
  `Dead`;
- `G`: patient IDs extracted from gene-expression sample-column barcodes;
- `M`: patient IDs extracted from methylation sample-column barcodes.

Full TCGA sample barcodes are reduced to the 12-character patient segment with:

```text
(TCGA-\w\w-\w\w\w\w)
```

For example:

```text
TCGA-3L-AA1B-01A-11R-A37K-07 -> TCGA-3L-AA1B
TCGA-3L-AA1B-01A-11D-A36Y-05 -> TCGA-3L-AA1B
```

Set membership in `G` or `M` requires at least one matching sample column; it
does not require every feature value in that column to be nonmissing.

## Clinical status mapping

| Original `vital_status` | Rows | Mapping outcome |
|---|---:|---|
| `Alive` | 393 | retained |
| `Dead` | 54 | retained |
| `[Discrepancy]` | 1 | excluded |

All retained clinical barcodes are nonmissing, unique, and valid patient IDs.

## Omics-header deduplication

Every omics sample-column name matches the patient-ID pattern. Full column
names are unique, but multiple aliquots can reduce to the same patient.

| Modality | Sample-column entries | Patient-level duplicate structure | Distinct patients |
|---|---:|---|---:|
| Gene expression | 328 | 28 patients occur twice | `328 - 28` |
| Methylation | 353 | 44 occur twice, 5 occur three times, 1 occurs four times | `353 - (44 + 5×2 + 1×3)` |

## Exact set cardinalities

| Set relation | Cardinality |
|---|---:|
| `C` | 447 |
| `G` | 300 |
| `M` | 296 |
| `C ∩ G` | 287 |
| `C ∩ M` | 283 |
| `G ∩ M` | 280 |
| `C ∪ G ∪ M` | 460 |

The three-way intersection can be checked with inclusion–exclusion:

```text
|C∩G∩M|
= |C∪G∪M| - |C| - |G| - |M|
  + |C∩G| + |C∩M| + |G∩M|
```

Counts of 328 and 353 refer to sample columns before patient-level
deduplication and must not be used directly as patient counts.

# Clinical–omics linkage registry summary

## Source and linkage method

The Data Coordination Registry linked sample headers to clinical records
through a frozen patient-key crosswalk. Repeated aliquots and repeated sample
types were collapsed before classification. The table below partitions
patients represented in both gene-expression and methylation collections.

| Registry stratum | Alive | Dead | Other/discordant status |
|---|---:|---:|---:|
| Primary-tumor specimens in both assays | 211 | 34 | 1 |
| Metastatic specimens in both assays | 8 | 4 | 1 |
| Recurrent specimens in both assays | 3 | 2 | 0 |

The strata are mutually exclusive at patient level. For an Alive/Dead
analysis, sum the Alive and Dead columns across strata and exclude the final
status column.
