import random
import time

def median_of_medians(arr: list[int]) -> list:
    # Base case
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]

    # Stores the median of the chunks of len 5
    sub_medians = []

    # For each chunck of 5, sort it, then select the median
    for i in range(0, len(arr), 5):
        chunk = arr[i:i+5]
        sub_medians.append(sorted(chunk)[len(chunk) // 2])

    # Select the median of sub_meadians
    mid_idx = len(sub_medians) // 2

    # Recur; delegate to quickselect to find the mid_idxth value of sub_medians; this yields the best possible pivot
    return quickselect(sub_medians, 0, len(sub_medians) - 1, mid_idx)

# median_of_medians requires quickselect (and pivot) to achieve O(n)
def pivot(arr: list[int], li: int, hi: int, pivot_value: int) -> int:
    # Find the first occurrence of the pivot_value in the array (from the slice li -> hi)
    for i in range(li, hi + 1):
        if arr[i] == pivot_value:
            pivot_idx = i
            break

    # Move pivot out of the way
    swap(arr, pivot_idx, hi)

    # Standard Lomuto scheme
    i = li - 1
    for j in range(li, hi):
        if arr[j] < arr[hi]:
            swap(arr, i + 1, j)
            i += 1

    swap(arr, i + 1, hi)
    return i + 1

def quickselect(arr: list[int], li: int, hi: int, kth: int) -> int:
    # kth is bounded between li and hi; if li == hi, then kth is found
    if (li == hi):
        return arr[li]

    current_slice = arr[li:hi+1]
    # Find the median of medians; quickselect -> median_of_medians -> quickselect -> best pivot
    best_pivot_value = median_of_medians(current_slice)

    # Find the pivot index via one call
    pivot_idx = pivot(arr, li, hi, best_pivot_value)

    # kth lies to the left; discard right
    if pivot_idx > kth:
        # Recur; supply a portion of the array; the search range reduces
        return quickselect(arr, li, pivot_idx - 1, kth)
    # kth lies to the right; discard left
    elif pivot_idx < kth:
        return quickselect(arr, pivot_idx + 1, hi, kth)
    # kth found
    else:
        return arr[pivot_idx]

def swap(arr, idx_a, idx_b):
    arr[idx_a], arr[idx_b] = arr[idx_b], arr[idx_a]
    
    return arr

# Test functions
def get_arr(arr_size: int) -> list[int]:
    arr = []

    for i in range(arr_size):
        arr.append(random.randint(1, arr_size))

    return arr

def get_kth(arr_size: int):
    return random.randint(1, arr_size) - 1

def test(arr : list[int], kth: int) -> int:
    li, hi = 0, len(arr) - 1

    start_time = time.perf_counter()
    kth_smallest = quickselect(arr, li, hi, kth)
    end_time = time.perf_counter()

    final_time = end_time - start_time

    print(f"Found {kth} smallest = {kth_smallest} in {final_time}")

if __name__ == "__main__":
    arr_size = random.randint(1000000, 9999999)
    arr = get_arr(arr_size)
    kth = get_kth(arr_size)

    test(arr, kth)