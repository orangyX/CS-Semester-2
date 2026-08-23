# 1. Problem overview
## 1.1. Goal
* Find k-th smallest mark from a large cohort
* Sorting the entire list is expensive; single order statistic retrievable in O(n) time potentially

## 1.2. Inputs
* Line 1:
    * n: number of total marks
    * k: mark appearing in the k-th position
* Line 2:
    * n integers, ranging from [0, 10^9]

# 2. Algorithm
if li == hi:
* We return arr[li]; since the k-th smallest mark must be bounded below, and above by li and hi
* if li == hi; the only possibility is that the kth smallest mark is exactly that position

## 2.1. Pivoting
Each time the pivot algorithm is called, it:
* Directly modifies the array
* Returns an index; that index is the i+1th smallest position; it has i elements smaller than it, and n-i elements larger than it

### 2.1.1. Pivot cases
Consider pivot_result > kth - 1:
* Means that the pivot_result overshot; it sits ahead of the kth entry
* Cut off the right side of the array via hi = pivot_result - 1; since kth does not sit anywhere above the pivot_result
* Recur; this shall yield possibly a different result

Consider pivot_result < kth - 1:
* Means that the pivot_result is an undershoot; it sits before the kth entry
* Cut off the left; li = pivot_result + 1; kth does not sit anywhere before the pivot_result

else:
* This means that the pivot_result has returned the kth smallest entry

#### 2.2. How does pivoting actually work?
Consider the array [4, 3, 6, 1, 7, 3] s.t. 3 is the selected pivot, this yields:
* [4, 3, 6, 1, 7 | 3]

In this case; instantiate two pointers, i, and j:
* j moves in a loop; we loop from the start of the array to the end, before the pivot value
* i is static; it moves only when the compared result at j is less than the pivot
* Each time the value at position j is s.t. or e.t. the pivot, i += 1, swap pos. j w/ pos. i
* At the end, swap the pivot value with i + 1th position; this yields the i+1th smallest value
    * Yield i + 1th specifically due to 0-based indexing

# 3. Complexities
## 3.1. Table of complexities
| Complexity type  | Method      | Complexity                     | Reason                                                                                        |
| :--              | :---        | :---                           | :---                                                                                          |
| Time complexity  | quickselect | O(n) (avg), O(n^2) worst case  | Average: n + n/2 + ... = 2n, worst: n + (n-1) + ... + 1 = n(n+1)/2 = n^2 = O(n^2)             | 
| Time complexity  | pivot       | O(n)                           | Loop through a list of n linearily                                                            |
| Space complexity | algorithm   | O(n)                           | Each recursive call pushes a frame onto the call stack; O(n) worst case, O(logn) average case |