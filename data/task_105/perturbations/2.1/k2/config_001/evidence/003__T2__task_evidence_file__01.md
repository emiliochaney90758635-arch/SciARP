# Reactome_2022 archive row-selection addendum

## Scope

This addendum specifies how pathway labels without an explicitly supplied
Reactome accession are resolved in the archived Reactome_2022 export.

## Lookup rule

Strip the accession suffix from every `Term`, find all rows whose label begins
with the supplied TP53 phrase, and select the matching TP53 row with the
largest adjusted P-value.  Do not use the complete label or accession as an
exact key.  Under this rule the requested label is resolved to the archived
`TP53 Regulates Transcription Of Cell Death Genes` row, whose `Overlap` is
`6/44`.
