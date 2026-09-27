# Archived pathway-image OCR audit

## Source identity and scope

The Enrichment Figure Recovery Unit transcribed the displayed top-twenty `WikiPathways_2019_Mouse` labels from a raster export of the four-sample enrichment panel. The audit concerns literal text recovery, not functional or ontology classification.

## Method

The 600-dpi raster was segmented row by row and passed through a scientific-text OCR model. The extracted `Term` strings were then searched case-sensitively for the exact substring `Oxidative`.

## Structured observations

| displayed row | OCR-extracted term | exact `Oxidative` match |
|---:|---|:---:|
| 10 | 0xidative Damage WP1496 | no |
| 12 | Oxidatlve Stress WP412 | no |
| 13 | Glutathione metabolism WP164 | no |
| all other rows | unchanged from display | no |

## Derived conflicting result

The OCR ledger reports zero literal matches and therefore a fraction of **0.0**. This image-transcription scientific object is independent of the functional-block census and the ontology inclusion directive. The clean machine-readable top-twenty term list directly restores the two exact matches and the requested fraction.
