import random
import time
import sys

sys.setrecursionlimit(30000)

def counting_sort(arr: list) -> list:
    output_arr = [0] * len(arr)
    # Frequency array, to be transformed into prefix sum array
    prefix_arr = [0] * (max(arr) + 1)

    # Record frequencies
    for item in arr:
        prefix_arr[item] += 1

    # Compute the prefix sums
    for i in range(1, len(prefix_arr)):
        prefix_arr[i] += prefix_arr[i - 1]

    for i in range(len(arr), 0, -1):
        # All arr[i] must be placed before index 
        index = prefix_arr[arr[i - 1]] - 1
        output_arr[index] = arr[i - 1]
        # Decrement the prefix; this means that a duplicate element is placed at the index before
        prefix_arr[arr[i - 1]] -= 1

    return output_arr

def get_arr(arr_size: int) -> list:
    arr = []

    for i in range(arr_size):
        arr.append(random.randint(1, arr_size))

    return arr

def test_random(arr: list) -> None:
    start_time = time.perf_counter()
    end_time = time.perf_counter()

    final_time = end_time - start_time

    print(f"{len(arr)} items sorted in {final_time:.6f} seconds")

def test_adversarial(arr_size: int) -> None:
    arr = [0, arr_size]

if __name__ == "__main__":
    arr_size = random.randint(10000, 20000)
    random_arr = get_arr(arr_size)
    test_random(random_arr)