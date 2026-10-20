import random
import time

def counting_sort_radix(arr: list[int], exp: int) -> list[int]:
    # Base 10
    digits = [0] * 10
    output = [0] * len(arr)

    for item in arr:
        # Procure place portion; 1 -> ones place; 10 -> ten's place, ...
        index = item // exp
        # 10 removes to the right, if required
        digits[index % 10] += 1

    for i in range(1, len(digits)):
        # Compute prefix sums
        digits[i] += digits[i-1]

    for i in range(len(arr), 0, -1):
        index = arr[i - 1] // exp
        # %10 removes to the left, whereas // (integer division) removes from the right (according to the value of the exponent)
        output[digits[index % 10] - 1] = arr[i - 1]
        # Decrement the prefix sum; shift the index of the next entry in that slot by 1
        digits[index % 10] -= 1

    return output

def radix_sort(arr: list[int]) -> list:
    # Fetch each component of the number
    exp = 1
    # Condition value; this value contains the max number of digits d
    max_val = max(arr)

    while exp < max_val:
        arr = counting_sort_radix(arr, exp)
        # Move the place up
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
    print(radix_sort(arr))
    end_time = time.perf_counter()
    final_time = end_time - start_time

    print(f"{len(arr)} items sorted in {final_time:.6f} seconds")

if __name__ == "__main__":
    arr = get_arr(random.randint(10000, 25000))
    test_random(arr)
    pass