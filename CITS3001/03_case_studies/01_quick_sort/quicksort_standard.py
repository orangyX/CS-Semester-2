import random
import time
import sys

sys.setrecursionlimit(30000)

def partition(arr, li: int, hi: int) -> int:
    # Consider the last index to be the pivot index
    pivot = arr[hi]
    # The wall
    i = li - 1

    for j in range(li, hi):
        if arr[j] < pivot:
            i += 1
            # Shift element if element < pivot, else element stays in its position
            arr[i], arr[j] = arr[j], arr[i]
    # The pivot value gets placed at the end of this list
    arr[i+1], arr[hi] = arr[hi], arr[i+1]

    return i + 1 # The pivot index, handed back to quicksort

def quicksort(arr, li = 0, hi = None) -> list:
    """
    Take pivot value as the last index (prone to adversarial inputs)
    """
    if hi is None:
        hi = len(arr) - 1

    if li < hi:
        # Acquire the pivot index
        pivot_index = partition(arr, li, hi)
        # LHS: consider arr[li:pivot_index - 1]
        quicksort(arr, li, pivot_index - 1)
        # RHS: consider arr[pivot_index + 1:hi]
        quicksort(arr, pivot_index + 1, hi)

    return arr    

def get_arr(arr_size: int) -> list:
    arr = []

    for i in range(arr_size):
        arr.append(random.randint(1, arr_size))

    return arr

def test_random(arr: list) -> None:
    start_time = time.perf_counter()
    quicksort(arr)
    end_time = time.perf_counter()

    final_time = end_time - start_time

    print(f"{len(arr)} random items sorted in {final_time:.6f}")

def test_adversarial(arr: list) -> None:
    start_time = time.perf_counter()
    quicksort(arr)
    end_time = time.perf_counter()

    final_time = end_time - start_time

    print(f"{len(arr)} reversed items sorted in {final_time:.6f}")

if __name__ == "__main__":
    arr_size = random.randint(10000, 20000)
    random_arr = get_arr(arr_size)
    reversed_arr = list(reversed(sorted(random_arr)))
    test_random(random_arr)
    test_adversarial(reversed_arr)
