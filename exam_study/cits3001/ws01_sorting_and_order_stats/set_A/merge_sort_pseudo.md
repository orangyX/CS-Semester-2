# 1. Merge sort
## 1.1. Merge algorithm
```
def merge(lhs, rhs):
    li, ri = 0, 0
    result = []

    while li < len(lhs) and ri < len(rhs):
        if lhs[li] <= rhs[ri]:
            result.append(lhs[li]) # lhs[li] smaller, so save that
            li += 1
        else:
            result.append(rhs[ri]) # rhs[ri] smaller
            ri += 1
    
    # Append the remains of both lists
    result.extend(lhs[li:])
    result.extend(rhs[ri:])

    yield result
```

# 1.2. Merge-sort algorithm
```
def merge_sort(xs):
    if len(xs) <= 1:
        return xs

    mid = len(xs) // 2 # Take the middle-most index; this is where the partition occurs
    return merge(merge_sort(xs:mid), merge_sort(xs[mid:])) # Recursive
```

# 2. time complexity
* Continuous halving yields $O(lg N)$ levels of recursion.
* At every level, each element comprises a single merge; appending costs $O(1)$, so each level requires $O(N)$
* $\therefore$ Total $O(NlgN)$ for every case
* Recurrence relation: $T(N) = 2T(\frac{N}{2}) + O(N)$

# 3. Merge sort attributes
Recall:
* Optimal: achieves the best possible asymptotic time running-time for the problem.
* In-place: uses a constant amount of memory (i.e., $O(1)$ additional)
* Stable: the algorithm preserves the relative ordering of elements with equal values (keys)

Applying this to merge-sort:
| Attribute | Merge-sort |
| :--- | :--- |
| Optimal | Merge-sort is optimal; for comparison-base sorting algorithms, $O(NlgN)$ is the theoretical lower-bound |
| In-place | Merge sort is not in-place; in the merge step, elements must be copied into a temporary space to sort, without overwriting the data |
| Stable | Merge-sort is stable; during merge, if elements are equal, take the element from the left array, this preserves stablity |