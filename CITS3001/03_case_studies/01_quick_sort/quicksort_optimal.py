import random
import time
import sys

sys.setrecursionlimit(30000)

def partition(arr: list, li: int, hi: int) -> int:
    # More highly optimised: in the worst case (list sorted in reverse, take the middle value)
    mid = li + (hi - li) // 2
    pivot = arr[mid]
    arr[mid], arr[hi] = arr[hi], arr[mid]

    i = li - 1
    for j in range(li, hi):
        if arr[j] < pivot:
            i += 1
            # Perform the swap
            arr[i], arr[j] = arr[j], arr[i]

    # Swap pivot between the left and right position
    arr[i+1], arr[hi] = arr[hi], arr[i+1]

    # Return the pivot index; this index is sorted and shall never be touched again
    return i + 1

def quicksort(arr, li = 0, hi = None) -> list:
    if hi is None:
        hi = len(arr) - 1

    if li < hi:
        pivot_index = partition(arr, li, hi)
        quicksort(arr, li, pivot_index - 1)
        quicksort(arr, pivot_index + 1, hi)

    return arr

# Test functions

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

    print(f"{len(arr)} adversarial items sorted in {final_time:.6f}")

if __name__ == "__main__":
    arr_size = random.randint(10000, 20000)
    random_arr = get_arr(arr_size)
    adversarial_arr = [1] * arr_size
    test_random(random_arr)
    test_adversarial(adversarial_arr)
