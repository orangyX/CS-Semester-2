import random

def pivot(arr: list[int], li: int, hi: int) -> int:
    i = li - 1 # Init at -1
    pivot_index = (li + hi) // 2
    swap(arr, pivot_index, hi) # Move to hi; only swaps at the end of the loop

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
        print(arr)
        return arr[li]

    pivot_idx = pivot(arr, li, hi)

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
        print(arr)
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

    print(f"{kth} smallest element: {quickselect(arr, li, hi, kth)}")

if __name__ == "__main__":
    arr_size = 10
    arr = get_arr(arr_size)
    kth = get_kth(arr_size)

    test(arr, kth)