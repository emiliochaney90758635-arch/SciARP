# Annotation-join multiplicity audit

A separate audit reports 62,104 rows after the HGNC join because several HGNC identifiers map to multiple symbols. This conflicts with the supplied one-to-one join checks and would inflate significant-gene direction counts.
