# Coordinate-based gene consolidation report

**Source:** Bladder Epitranscriptome Annotation Core
**Input:** The 86 unique transcripts represented among `m6A Hyper and Up` source rows
**Method:** Transcript genomic spans were clustered into current gene loci. Transcripts sharing a locus were consolidated; read-through accessions whose spans resolve to two current loci contributed one additional locus.

| Consolidation component | Count |
|---|---:|
| Unique target transcripts | 86 |
| Redundant transcript entries removed during locus clustering | 18 |
| Additional loci created by resolved read-through splits | 5 |

The core’s target-gene count is computed as unique transcripts minus redundancies plus split-derived loci.
