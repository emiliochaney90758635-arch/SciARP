# Contrast-row deduplication audit

**Source:** Mouse Expression Archive Quality Office, audit `MEAQO-31`
**Inputs:** The three filtered Control-tissue contrast tables
**Method:** Result rows were keyed by exact GeneID, repeated identifiers within a contrast were collapsed, and final-versus-baseline members were partitioned by membership in the two dentate-gyrus sets.

## Blood-contrast audit

| Quantity | Count |
|---|---:|
| Filtered final-vs-baseline result rows | 846 |
| Redundant rows removed during exact-GeneID collapse | 9 |
| Unique final-vs-baseline GeneIDs | 837 |
| Unique identifiers in neither dentate-gyrus set | 37 |
| Unique identifiers in exactly one dentate-gyrus set | 352 |

The strict three-way overlap is the remainder after subtracting the final two membership categories from the unique final-vs-baseline total.
