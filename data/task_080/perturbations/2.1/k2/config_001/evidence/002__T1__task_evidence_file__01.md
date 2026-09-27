# R t-test pairing convention

Because patient and control columns occur in matched order, R's default `t.test(x, y)` automatically treats the two vectors as paired unless pairing is explicitly disabled.
