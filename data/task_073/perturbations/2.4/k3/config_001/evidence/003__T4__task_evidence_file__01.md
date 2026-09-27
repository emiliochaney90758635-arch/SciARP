# Randomized decomposition audit

**Source:** High-Dimensional Numerics Service, run `HDNS-RSVD-178-100`
**Scope:** the 178 × 2,456 log10(x+1) sample-by-gene matrix
**Method:** Features were centered, a randomized rank-100 SVD was fitted, and component contributions were normalized against the variance subtotal captured by the returned 100 components.

| Quantity | Value |
|---|---:|
| First squared singular value | 8,780.3631 |
| Squared-singular-value subtotal, components 1–100 | 14,322.0 |

The audit reports the leading percentage as `100 × 8780.3631 / 14322.0`.
