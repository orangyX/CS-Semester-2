# 1. Define optimal, in-place (CLRS's definition) and stable for a sorting algorithm.
* Optimal: an algorithm runs in the fastest-possible asymptotic complexity to solve that particular problem.
* In-place: $O(1)$ additional space is used by an algorithm to sort a problem; in terms of sorting algorithms, swapping occurs in the given array itself.
* Stable: values (keys) which are equal maintain their relative orderings.

| Algorithm | Optimal | In-place | Stable |
| :--- | :--- | :--- | :--- |
| Insertion sort | ✗ | ✓ | ✓ |
| Merge-sort | ✓ | ✗ | ✓ |
| Heapsort | ✗ | ✓ | ✗ |
| Quicksort | ✗ | ✓ | ✗ | 

# 2. Define an inversion, and count the inversions in [3, 1, 4, 1, 5].
An inversion is a pair of elements where the earlier occurring element is strictly greater than the later occurring element, this means that their positions are incorrect.

Formally, for indicies $i, j : i < j$ and elements $A, B : A > B$, then an inversion is present given that $A_i > B_j$.

In 
```
[3, 1, 4, 1, 5]
```
Then there are 3 inversions, one between 3 and $1_{i=1}$, and $1_{i=3}$, and the last between 4, and $1_{i=3}$.