# Ordering of Cohort Selection and Gene Prefiltering in the Paroxetine Pseudo-Count Workflow

Lucia B. Moretti, Kwame D. Boateng, Haruna I. Sato, and Peter J. Caldwell

## Abstract

We audited release 1.4 of the archived exploratory paroxetine workflow while retaining the same ninety normalized-expression profiles, Response definition, Tissue levels, final-blood-versus-baseline-blood contrast, pseudo-count transformation, joint thresholds, and descriptive interpretation. In this release, the thirty Control samples were selected before prefiltering, and the requirement that a GeneID sum to at least ten was evaluated only across those Control columns; rescaling and integer rounding were then applied to that Control-restricted matrix. The archived clean workflow instead applies the aggregate-expression prefilter to the complete ninety-sample matrix before Control extraction. The disagreement therefore concerns the order of two preprocessing operations, not the Control roster or a replacement terminal count.
