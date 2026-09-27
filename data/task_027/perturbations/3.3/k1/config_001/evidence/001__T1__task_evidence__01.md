# Evidence for this task

## Tissue and contrast mapping

The experiment contains three tissues, each with 10 Control, 10 good-responder, and 10 bad-responder samples:

| Tissue label | Bad-responder-versus-Control contrast key |
|---|---|
| Baseline blood | `baseline_bad_resp_vs_ctrl` |
| Final blood | `final_bad_resp_vs_ctrl` |
| Dentate gyrus | `brain_bad_resp_vs_ctrl` |

For each contrast, define a set of unique `GeneID` values using the same filter:

```text
padj < 0.05
abs(log2FoldChange) > 0.5
baseMean >= 10
```

The archived analysis uses rounded pseudocounts made by scaling the cleaned normalized-count matrix to one million per gene across the 90 samples and rounding to integers. It is therefore descriptive rather than a reanalysis of raw sequencing counts.

## Three-tissue Venn output

The plotted input order is Brain, Final, Baseline. Its seven mutually exclusive regions are:

| Region | Unique `GeneID` count |
|---|---:|
| Brain only | 138 |
| Brain ∩ Final only | 2 |
| Brain ∩ Baseline only | 0 |
| Final only | 73 |
| Final ∩ Baseline only | 1 |
| Baseline only | 60 |
| Brain ∩ Final ∩ Baseline | 0 |

For any one tissue, obtain its set size by summing every mutually exclusive region in the table that contains that tissue.

## Validity note

These counts summarize the archived thresholded, rounded-pseudocount workflow. They are useful for comparing set sizes and overlaps within that workflow, but the pseudocount construction and shared subjects/contrasts limit formal inferential interpretation.
