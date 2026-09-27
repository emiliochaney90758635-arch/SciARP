# Current identifier-mapping reconstruction report

## Source identity and scope

The Transcript Identifier Audit Service reprocessed the 679 Ensembl IDs from
the CBD/cisplatin-versus-DMSO selection against its 2026-07 human-symbol
mapping snapshot. This is a current reconstruction, not an executed-notebook
record from the archived gseapy run.

## Method and observations

Each unique Ensembl ID was queried once; ambiguous or missing approved symbols
were excluded.

| Quantity | Count |
|---|---:|
| Selected Ensembl IDs | 679 |
| Unambiguous current mappings | 649 |
| Failed or ambiguous mappings | 30 |

The reconstructed enrichment input therefore contains 649 gene names, in
conflict with an archive interpretation based on 23 failures and 656 names.
