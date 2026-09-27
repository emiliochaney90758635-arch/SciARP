# Current identifier-mapping reconstruction report

## Source identity and scope

The Transcript Identifier Audit Service reprocessed the 679 Ensembl IDs from
the CBD/cisplatin-versus-DMSO selection against its 2026-07 human-symbol
mapping snapshot.  This is a current reconstruction, not an executed-notebook
record from the archived gseapy run.

## Method

Each unique Ensembl ID was queried once.  Entries without an unambiguous
approved gene symbol were marked failed, and only nonmissing symbols were
counted as the reconstructed enrichment input.

## Structured observations

| Quantity | Count |
|---|---:|
| Selected Ensembl IDs | 679 |
| Unambiguous current mappings | 649 |
| Failed or ambiguous mappings | 30 |

## Derived result

The reconstructed submitted-name count is `679 - 30 = 649`, which conflicts
with an archived interpretation based on 23 failed mappings and 656 retained
names.
