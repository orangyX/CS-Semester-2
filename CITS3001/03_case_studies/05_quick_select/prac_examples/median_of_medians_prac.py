import random
import time

def median_of_medians(arr: list[int]) -> list[int]:
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]

    sub_medians = []

    i = 0
    while i < len(arr):
        chunk = arr[i: i + 5]
        sub_medians.append(sorted(chunk)[len(chunk) // 2])
        i += 5

    mid_idx = len(sub_medians) // 2
    return quickselect(sub_medians, 0, len(sub_medians) - 1, mid_idx)

# Standard quickselect algorithm
def pivot(arr: list[int], li: int, hi: int, pivot_value: int) -> int:
    for i in range(len(arr)):
        if arr[i] == pivot_value:
            pivot_idx = i
            break

    swap(arr, pivot_idx, hi) # Move to hi; only swaps at the end of the loop

    i = li - 1
    for j in range(li, hi):
        if arr[j] < arr[hi]:
            swap(arr, i + 1, j)
            i += 1

    swap(arr, i + 1, hi)
    return i + 1

def swap(arr: list[int], idx_a: int, idx_b: int) -> list:
    arr[idx_a], arr[idx_b] = arr[idx_b], arr[idx_a]
    return arr

def quickselect(arr: list[int], li: int, hi: int, kth: int) -> int:
    # Eliminated to a single variable; kth is bounded here
    if li == hi:
        return arr[li]

    this_slice = arr[li:hi+1]
    pivot_val = median_of_medians(this_slice)
    pivot_idx = pivot(arr, li, hi, pivot_val)

    # Resides in the left half; discard the upper half
    if pivot_idx > kth:
        hi = pivot_idx - 1
        return quickselect(arr, li, hi, kth)
    # Resides in the right half; discard the left
    elif pivot_idx < kth:
        li = pivot_idx + 1
        return quickselect(arr, li, hi, kth)
    # kth identified
    else:
        return arr[pivot_idx]

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

    print(sorted(arr))
    print(f"Found {kth} smallest = {kth_smallest} in {final_time}")

if __name__ == "__main__":
    arr_size = random.randint(10000, 20000)
    arr = get_arr(arr_size)
    kth = get_kth(arr_size)

    test(arr, kth)
