# 1. Task description
## 1.1. Task overview
* Dates have three components: day, month, year

## 1.2. Task goal
* Sort dates in chronological order
* Use radix sort to do so; decide on the MSD, LSD

## 1.3. Inputs
* Line 1: contains an integer n, denotes no. dates
* Line 2, ..., n contains dates, one per line

# 2. Implementation
## 2.1. General approach to handling dated components
* Convert to a tuple; indexed from 0, 1, 2:
    * 0 denotes the day component
    * 1 denotes the month component
    * 2 denotes the year component
* Use tuple indices; denote as date_component:
    * Termination condition for radix sort: while date_component <= 2 (i.e., the last index)
-------

## 2.2. Radix sort algorithm
### 2.2.1. Complexities
Time complexity:
* O(n) time required for finding max value, and min value
* Counting sort earns O(d*n + sum(date_component)); here, d = 3
    * = O(3n + sum(k_i)) = O(3n) = O(n)

Space complexity:
* O(n+k) addtl. space required:
    * k denotes difference between the max, and min elements + 1

## 2.3. Design considerations
### 2.3.1. Data processing
Date-component reasoning:
* I tried ot work with datetime import, but it was incredibly messy; I found it much easier to use a tuple:
    * Tuple allows indexing
    * Gives away an easy looping condition for free; continue while not all components have been processed

### 2.3.2. Radix sort
"What is offset constant? why are you using it?"
* Offset constant denotes the minimum value within the dateset

"Why compute the min/max every time, per run, rather than just hardcode it?"
* Allows us to dynamically handle inputs
* For some date component, the data range varies (day: 0-28, month: 0-12, year: 1900-2100)
* By this, if we wished to add a minutes/seconds component; it would certainly be possible, with reduced code modifications

"What is data_range? why are you using it? why + 1 on the end?"
* We only care about the absolute range of the data, consider:
    * A year component, varying from 1900 to 2100
    * We wish to create 200 positions, not 2100, then only using the last 200 positions; that is wasted memory in the worst case
* +1 is important; ensures inclusivity of certain values; in year, min = 1900, max = 2100; so inclusive of <= 201 values

"Why use day component as the LSD, rather than year?"
* The last pass must be the MSD
    * Go by LSD first (i.e., day)
    * Counting sort is stable, the final pass fixes the primary order, all earlier passes survive within ties, thus MSD must go last

### 2.3.3. Counting sort
prefix_arr:
* Instantiated to data_range; this ensures that there are positions available for every number to count the occurences

Filling prefix_arr:
* index item by date_compoennt to access the required date_component:
    * If date_component = 0, access day component, if 2, year, etc.
    * Subtract the offset_constant; this is the minimum value within the data range, given to the function:
        * For year, lowest is 1900, highest is 2100, so the real mapping is from 0 - 200
    * Bump up the count of that number

Computing the prefix sums:
* Loop through the prefix_arr, sum prefix_arr[i] and prefix_arr[i-1]:
    * It holds the count of elements whose key is <= i + offset
    * The cumulative sum maps each value to the ending index within the sort array

Inserting into the output_arr:
* Fetch the item, we need to grab the date from the date array:
    * Traverse from right-to-left to ensure stability; a higher value is placed at the right of the array first, built to the left
    * Index via i-1; indexed using the date component (subtract the offset constant to map down to the valid range, so we get the date component in the range)
    * Compute the index; accessed by using item as index on prefix_arr - 1 (since prefix sum yields count; the -1 converts to a 0-indexed based scheme)
    * Insert into the output_arr using that index; we just insert the raw date itself into the array
    * Decrement in the prefix_arr for that item; ensures relative stability; items in the output_arr are filled from right to left
