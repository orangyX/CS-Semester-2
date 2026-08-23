# 1. Complexities
## 1.1. Time complexity
The time complexity of this algorithm is O(n), let:
* d = 3
* n = size on the inputs
* k be the sum of the data ranges

Thus, generally radix sort with a counting-sort based implementation runs in O(d*(n + k)):

Here, O(3n + 201 + 12 + 28) = O(3n) = O(n)

## 1.2. Worst case complexity
Is O(n), and its average case is also O(n).

# 2. LSD -> MSD
Sorting by LSD first ensures stability, and preserves work done within earlier passes of the algorithm

## 2.1. Why is day the LSD?
* Denotes smallest + most rapidly changing unit of time

But why?
* If we sorted from year -> month -> day, we would simply be sorting based on day, our work from sorting year -> month would be wasted
* Sorting day first means that the work is saved; instantly that 2025 is < 2026; in a day sort, 28/.../2025 and 17/.../2026 would sort the days and place the 28 version first

# 3. Stability
## 3.1. Why use counting sort?
Radix sort must be a stable sorting algorithm; thus, if it uses an unstable under-the-hood sorting algorithm, it itself becomes unstable

Importance:
* Two numbers may share the same digit
* Stable sort ensures that both numbers stay within their relative positions
* Ensures that the sorted order of previous passes is never destroyed/scrambled by newer passes