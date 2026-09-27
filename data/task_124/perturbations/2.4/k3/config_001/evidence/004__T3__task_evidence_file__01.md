# Optical-mapping chromosome-length density audit

## Source identity and scope

The Avian Physical Map Consortium produced chromosome-length estimates for the same Zebra Finch assembly lineage using optical maps rather than sequence-assembly spans. To isolate denominator sensitivity, the audit reused the archive's strict-threshold distinct-site counts: 29 sites on chromosome 1 and 3 sites on chromosome W.

## Method

Single-molecule optical maps were assembled into chromosome-scale consensus maps after removal of terminal overlap. Physical-map span, not repeat-masked callable span or sequence-assembly span, was used as the density denominator.

## Structured observations

| chromosome | retained distinct sites | optical-map span (bp) |
|---|---:|---:|
| 1 | 29 | 116,400,000 |
| W | 3 | 18,700,000 |

## Derived conflicting result

Using these independent physical-map denominators gives

`(3/18,700,000) / (29/116,400,000) = 0.643924`.

This optical-map length object is independent of the earlier callable-segment and whole-sequence-assembly audits. The requested archive remains recoverable from its verified Zebra Finch chromosome lengths.
