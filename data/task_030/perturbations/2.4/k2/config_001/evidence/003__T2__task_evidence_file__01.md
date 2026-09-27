# Supervisor-coded exposure-volume tables

**Source:** Occupational Workload Classification Office
**Scope:** Complete randomized participants with supervisor-coded baseline workload.
**Endpoint:** Maximum severity across all recorded adverse events per complete subject
**Stratification:** Supervisor-assigned baseline workload bands, independently coded as low, medium, and high.
**Method:** Within each supervisor band, tabulate severity levels 1–4 by BCG and Placebo and apply a separate ordinary Pearson test.

```text
low:    (120,128), (180,140), (22,15), (8,5)
medium: (24,20),   (31,29),   (4,2),   (1,3)
high:   (5,4),     (8,6),     (2,0),   (0,1)
```

Each row pair gives BCG and Placebo counts for severity levels 1 through 4. These supervisor-coded bands are not the archived `patients_seen` categories.
