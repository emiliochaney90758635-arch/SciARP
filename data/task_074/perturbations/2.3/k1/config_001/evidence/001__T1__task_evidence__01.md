# Evidence for This Task

## Analysis Matrix

After removing all duplicated `projid` values and the corresponding expression columns, the metadata contain 178 samples and the expression matrix contains 2,456 genes × 178 samples. Applying \(\log_{10}(x+1)\) to the expression values and transposing the result yields a clustering input of 178 samples × 2,456 genes; sample and gene IDs are unique, and the transformed values are all finite.

## Consensus Procedure Across 50 Train/Test Splits

The archived code executes the following with `n_clusters=3`:

```python
for _ in range(50):
    train_ind, test_ind = train_test_split(
        data.index,
        test_size=0.3,
        random_state=np.random.randint(1000)
    )
    train_labels = AgglomerativeClustering(
        n_clusters=3
    ).fit_predict(train_data)
    classifier = LogisticRegression().fit(train_data, train_labels)
    train_pred = classifier.predict(train_data)
    test_pred = classifier.predict(test_data)
```

Predicted labels are accumulated separately for train and test in each iteration. For any sample pair, the proportion of matching labels is calculated only over iterations in which both samples occur on the relevant side and both labels are non-missing, producing two 178 × 178 consensus matrices.

The following is then run separately:

```python
consensus_train_labels = AgglomerativeClustering(
    n_clusters=3
).fit_predict(train_consensus_matrix)

consensus_test_labels = AgglomerativeClustering(
    n_clusters=3
).fit_predict(test_consensus_matrix)
```

The two final numeric label vectors cover all 178 samples in the same order.

## Native Archived Output

Cluster sizes for the training-consensus labels:

```text
train
1    96
0    56
2    26
Name: count, dtype: int64
```

Output from an element-wise raw numeric-equality comparison of the two final vectors:

```text
True    -173
False      5
Name: count, dtype: int64
```

This run does not fix the NumPy seed, and the two consensus matrices are clustered independently; no cluster-label permutation alignment is performed before comparison. Numeric labels have no intrinsic class semantics, so the result is interpreted only as raw numeric-label equality in the archived run and is not extrapolated as seed-invariant clustering consistency.
