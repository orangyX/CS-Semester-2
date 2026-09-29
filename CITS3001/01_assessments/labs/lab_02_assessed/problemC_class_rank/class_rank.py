def pivot(arr: list[int], li: int, hi: int) -> int:
    # Initialise to -1; this value will only ever be accessed from 0 -> hi - 1 (worst case)
    i = li - 1
    for j in range(li, hi):
        if arr[j] <= arr[hi]:
            swap(arr, i + 1, j)
            i += 1

    swap(arr, i + 1, hi)
    # An element at position i + 1 has i elements smaller than it; hence it is the ith smallest
    return i + 1

def swap(arr: list[int], idx_a: int, idx_b: int) -> list[int]:
    arr[idx_a], arr[idx_b] = arr[idx_b], arr[idx_a]
    return arr

def quickselect(arr: list[int], li: int, hi: int, kth: int) -> int:
    if li == hi:
        return arr[li]

    pivot_result = pivot(arr, li, hi)
    
    # An undershoot; hence we cut off the left
    if pivot_result > kth - 1:
        hi = pivot_result - 1
        return quickselect(arr, li, hi, kth)
    # Overshoot; cut off the right
    elif pivot_result < kth - 1:
        li = pivot_result + 1
        return quickselect(arr, li, hi, kth)
    # Just right; we return
    else:
        return arr[pivot_result]

arr_size, kth = map(int, input().split())
marks = list(map(int, input().split()))
li, hi = 0, len(marks) - 1
print(quickselect(marks, li, hi, kth))  
