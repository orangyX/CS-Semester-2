import random
import time

def pivot(arr: list[int], li, hi) -> int:
    i = li - 1
    # Select the middle value forom the pivot
    pivot_idx = (li + hi) // 2
    swap(arr, pivot_idx, hi)

    for j in range(li, hi):
        if arr[j] <= arr[hi]:
            swap(arr, i + 1, j)
            i += 1

    swap(arr, i + 1, hi)
    return i + 1

def swap(arr: list[int], idx_a: int, idx_b: int) -> list:
    arr[idx_a], arr[idx_b] = arr[idx_b], arr[idx_a]
    return arr

def quickselect(arr: list[int], li: int, hi: int, kth: int) -> int:
    if li == hi:
        # print(arr)
        return arr[li]

    pivot_index = pivot(arr, li, hi)

    # Discard the right
    if pivot_index > kth:
        return quickselect(arr, li, pivot_index - 1, kth)
    # Discard the left
    elif pivot_index < kth:
        return quickselect(arr, pivot_index + 1, hi, kth)
    # Found kth; return
    else:
        # print(arr)
        return arr[pivot_index]

# Test functions
def get_arr(arr_size: int) -> list[int]:
    arr = []

    for _ in range(arr_size):
        arr.append(random.randint(1, arr_size))

    return arr

def get_kth(arr_size: int):
    return random.randint(1, arr_size) - 1

def test(arr : list[int], kth: int) -> int:
    li, hi = 0, len(arr) - 1
    print(sorted(arr))
    print(f"{kth} smallest element: {quickselect(arr, li, hi, kth)} for len = {len(arr)}")

if __name__ == "__main__":
    arr_size = 10
    arr = get_arr(arr_size)
    kth = get_kth(arr_size)

    test(arr, kth)