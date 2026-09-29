# 1. Complexity
## 1.1. Time complexity
Best case: O(n):
* Occurs when the selected pivot splits the array into approximately n/2
* n + n/2 + ... = 2n = O(n)

Average case: O(n):
* Randomly chosen pivots divide the search space by a constant fraction on average

Worst case: O(n^2)
* The pivot is constantly the max, or min
* n + (n-1) + (n-2) + ... = n(n+1)/2 = O(n^2)