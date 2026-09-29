# 1. Alternative (and correct) implementation
1. Iterate through the given array, find the total sum of students
2. Pick a room as a pivot; group the rooms into the left (lower), and right (higher)
3. Check weights:
    * Sum the students in the left partition
    * If left has sum/2 > sum_left, but pivot + sum_left > sum/2, then that is the weighted median
    * If the left is too light, use recursion to narrow the search to the right side of the partition

# 2. Complexity of this program
Runs in O(d(n+b)):
* Sort rooms by position, using b (num.10 base); d denotes the number of places in the max value
* n; the size of inputs

