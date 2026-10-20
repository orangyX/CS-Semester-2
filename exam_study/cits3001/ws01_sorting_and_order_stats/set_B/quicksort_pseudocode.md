# 1. Pivot algorithm
```
partition(xs, lwr, upr):
    pivot = xs[upr-1]
    mid = lwr

    for i in range(len(xs)):
        if xs[mid] <= pivot:
            xs[mid], xs[i] = xs[i], xs[mid]
            mid += 1
    
    return mid - 1
```

# 2. Quicksort algorithm
```
quicksort_range(xs, lwr, upr):
    if upr - lwr > 1:
        p = partition(xs, lwr, upr) # Fetch the pth order statistic
        quicksort_range(xs, lwr, p) # Consider everything to the left of p; exclusive of p, so the pivot is skipped
        quicksoprt_range(xs, p+1, upr) # Consider everything to the right of p; at p + 1, the pivot gets skipped
```

# 3. Expected case analysis
The expected case of quicksort is $O(NlgN)$, which is also its best case.
* Assumption: every permutation of the input is equally likely, hence the pivot's final position is uniform over the range.
* Worst case: the algorithm continuously selects the minimum/maximum elements, degrading performance to $O(N^2)$

# 4. Explain how to limit the call stack to  $O(lgN)$ even in the worst case.
