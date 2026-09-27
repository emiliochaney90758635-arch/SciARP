# Evidence for this task

## ENO1 proteomics record

The tumor-versus-normal proteomics table contains 3,850 protein records.
`ENO1` occurs once in the `gene` field.

| protein | gene | Normal protein abundance | Tumor protein abundance | Ratio | FC | compare |
|---|---|---:|---:|---:|---:|---|
| P06733 | ENO1 | 72896133.2946858 | 350385456.451912 | 4.81 | 4.81 | Tumor vs Normal |

The `compare` field fixes the direction as tumor relative to normal. The
unrounded linear abundance ratio is defined by:

```text
Tumor / Normal
= 350385456.451912 / 72896133.2946858
```

`FC` is a linear fold change, not a log2-transformed value. A ratio above 1
denotes higher abundance in tumor under this comparison direction.

# Reduced ENO1 abundance in tumor tissue revealed by paired proteome profiling

Nadia B. Corwin, Tomasz Zieliński, Haruto Senda, and Priya Nanduri

## Abstract

Altered glycolytic regulation is a hallmark of malignant tissue, but the
abundance of individual glycolytic enzymes remains context dependent. We
performed paired label-free proteomic profiling of resected tumors and
patient-matched normal tissue, requiring two unique peptides for ENO1
quantification and estimating fold change from normalized protein intensity.
ENO1 showed a reproducible decrease in tumors across the paired analyses, with
the tumor-to-normal abundance ratio remaining below unity under alternative
normalization and peptide-inclusion rules. The data support a loss of ENO1
protein abundance in the tumor compartment and argue against a multi-fold
tumor-associated increase.
