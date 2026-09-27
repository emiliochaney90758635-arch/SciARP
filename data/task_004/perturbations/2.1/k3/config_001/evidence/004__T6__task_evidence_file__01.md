# Complete preprocessing-scope addendum

The Control labels define the analysis population before any expression transformation is performed. The 30 Control samples—10 baseline-blood, 10 dentate-gyrus, and 10 final-blood—are first extracted from the 90-sample normalized-expression matrix.

Low-expression filtering is then evaluated within this Control-only matrix, and each retained gene is rescaled to a total of one million across those 30 Control samples before integer rounding. The resulting Control-only pseudo-count matrix is the input to the `~ Tissue` model and the final-blood-versus-baseline-blood contrast.
