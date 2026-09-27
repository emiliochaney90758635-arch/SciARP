# Label-vector checksum comparison

**Source:** Reproducible Analytics Registry, artifact `RAR-CONS-EQ`
**Scope:** the archived training- and test-consensus numeric vectors on the common ordered 178-sample index
**Method:** Vector entries were serialized as signed bytes, compared position-wise, and equality flags were aggregated in four consecutive index blocks.

| Sample-index block | Equal | Unequal |
|---|---:|---:|
| 1–45 | 44 | 1 |
| 46–90 | 43 | 2 |
| 91–134 | 42 | 2 |
| 135–178 | 42 | 2 |

The registry's raw match count is the sum of the four `Equal` entries.
