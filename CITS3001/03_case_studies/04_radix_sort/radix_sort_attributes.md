# Radix sort
## Complexities
### Radix sort time complexity
Radix sort maintains a time complexity of O(d * (n + k)), such that:
* n denotes the number of elements in the array
* d denotes the number of digits in the largest number 
* k denotes the base of the radix number system (here, k = 10 denoting decimal numbers from 0 to 9)

#### Time sort complexity reasoning
Radix sort isolates a single digit during each pass (from LSD to MSD), hence:
* Single pass of radix sort -> O(n + k) complexity
* Total passes: algorithm executes the above routine exactly d times (according to the number of places of the maximum value)
* Combined time: O(d * (n + k)) times; execute a single pass d times

Notably, radix sort has the following time complexity cases:
* Best case: O(n * d)
* Average case: O(n * d); similar to best case; each digit of each element in the input array is processed; yields linear time complexity w.r.t. no. elements and digits
* Worst case: O(n * d); when all elements have the same digits, or digits in reverse order, radix sort processes every digit of every element anyway

### Radix sort space complexity
Radix sort requires O(n + k) additional space, since:
* n elements must be (trivially) stored
* k denotes the frequency table used; in this implentation, a constant, since k = 10

## Pseudocode (via counting sort)
define counting_sort(array argument, exponent) -> list:
    output_array = size of the supplied array
    prefix_arr = [0] * 10; this is the frequency array, mapping each digit to index; we can represent through from 0 to 9

    for every item in array:
        index = (item // exponent) % 10; we compute the digit; % 10 ensures that left-digits to the current digit gets removed

    for i in range(1, len(prefix_arr)):
        prefix_arr[current] += prefix_arr[previous]; compute prefix sums

    for i in range(len(arr), 0, -1); of a step from the right of the array, through to 0
        digit = (item // exponent) % 10; recalculate the digit
        index = prefix_arr[digit] - 1; element at digit position in prefix_arr occurs at digit - 1
        prefix_arr[item] -= 1; decrement the prefix sum, s.t. the next run lands in the correct position
        output_array[index] = item

    yield output_array

define radix_sort(array argument) -> list:
    max_value = maximum of array
    exponent = 1; on the first pass, get units place, then tens, then 100's, and so on

    while exponent is no greater than max_value:
        array argument = counting_sort(array argument, exponent)
        exponent *= 10; push to the next place

    yield array
