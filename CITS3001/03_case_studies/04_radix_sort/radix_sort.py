import random
import time
import sys

sys.setrecursionlimit(25000)

def counting_sort(arr: list, exp) -> list:
    output = [0] * len(arr)
    prefix_arr = [0] * 10

    for item in arr:
        # Store the occurrences of the digit in the specified place, in the prefix_arr
        index = (item // exp) % 10
        prefix_arr[index] += 1

    for i in range(1, len(prefix_arr)):
        # Compute the prefix sum; for an element x at position n, all occurrences of x are to sit at n - 1
        prefix_arr[i] += prefix_arr[i - 1]

    for i in range(len(arr), 0, -1):
        digit = ((arr[i - 1] // exp) % 10)
        index = prefix_arr[digit] - 1
        prefix_arr[digit] -= 1
        output[index] = arr[i - 1]

    return output


def radix_sort(arr: list) -> list:
    arr_max = max(arr)
    exp = 1

    while exp <= arr_max:
        arr = counting_sort(arr, exp)
        exp *= 10

    return arr

# Testing functions
def get_arr(arr_size: int) -> list:
    arr = []

    for i in range(arr_size):
        arr.append(random.randint(1, arr_size))

    return arr

def test_random(arr: list) -> None:
    start_time = time.perf_counter()
    radix_sort(arr)
    end_time = time.perf_counter()
    final_time = end_time - start_time

    print(f"{len(arr)} items sorted in {final_time:.6f} seconds")

if __name__ == "__main__":
    arr = get_arr(random.randint(10000, 25000))
    test_random(arr)
    pass