# 1. Task description
## 1.1. Task overview
* Raindrops land on gutter, L mm
* Drain into k buckets; drops land at position x (s.t. 0 <= x < L)
* Fall into buckets denoted by [(x*k)/L] s.t. buckets numbered from 0, k-1

## 1.2. Task goal
* Yield amount of drops in each bucket
* Follows from distribution step of bucket sort

## 1.3. Inputs 
### 1.3.1. Line 1
* Three integers n, L, k:
    * n denotes the number of inputs (rain drops) to distribute amongst buckets
    * k denotes the no. buckets
    * L denotes the width of the gutter (i.e., the range of each bucket)

# 2. Implementation
## 2.1. Complexity of components
### 2.1.1. buckets method
Time complexity:
* Runs in O(n+k):
    * Operates on n raindrops
    * L denotes the number of buckets required to distribute data
    * Building the buckets runs in O(k) time

Space complexity:
* O(n) space for raindrops (n inputs)
* O(k) space required for no. buckets to distribute drops amongst
* Total complexity: O(n + k)

## 2.2. Design considerations
Additional space:
* buckets; a k-sized array of arrays, created according to the specified number of buckets required

### 2.2.1. Algorithm
get_bucket(item, max_size, num_buckets):
* item / max_size: maps the drop to a bound within [0, 1):
    * This yields its relative position; it essentially assigns a range per bucket
* num_buckets * map: 
    * A domain [0, 1) is insufficient, given that we need to map to k buckets; thus by multiplying to the no. buckets required, we essentially expand the range by a scalar; k*[0, 1) = [0, k)
* int(...):
    * Truncates decimal portion, making it possible to directly assign the rain drop to a position