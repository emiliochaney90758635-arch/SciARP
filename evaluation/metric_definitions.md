# Metric definitions

## Strict Task Accuracy

SciARP's paper-aligned final correctness requires both a correct scientific
process and a correct final answer.

For trajectory `i`, let `c_{i,t}` be the annotated correctness of assistant
turn `t`, and let `f_i` be final-answer correctness. Convert `true` to 1 and
both `false` and `null`/missing to 0. Then:

```text
StrictCorrect_i = f_i × product_t(c_i,t)
TaskAccuracy = (1 / N) × sum_i(StrictCorrect_i)
```

Thus `StrictCorrect_i=1` if and only if every assistant turn is correct and the
final answer is correct. A trajectory with no annotated assistant turns is not
correct. This definition is intentionally stricter than final-answer-only
accuracy and is the value reported as Task Accuracy by `compute_metrics.py`.

## Annotation primitives

- **Turn correctness**: whether the turn is substantively correct under the
  authoritative task/reference information. Equivalent wording is accepted.
- **Final-answer correctness**: whether the final answer satisfies the
  evaluator-only reference and scoring criteria.
- **Logical fidelity**: whether reasoning follows valid logic from the stated
  information.
- **Causal order**: whether prerequisites are used in a valid dependency order.
- **Task progress**: whether the turn materially advances the requested task.
- **Step validity**: whether the operation performed at the turn is valid.
- **C1 immediate recognition**: whether the response at the injection turn
  explicitly or implicitly recognizes the injected error.
- **C3 immediate correction**: whether that same response uses the correct
  value/rule; `C3=true` entails `C1=true`.
- **D3 stable recovery**: after at least one polluted event state, whether a
  later correct event-specific state occurs and no subsequent state is
  polluted. It is derived locally, not directly requested from the annotator.

