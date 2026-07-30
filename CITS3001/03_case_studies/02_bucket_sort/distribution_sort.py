import random
import time

def key_function(x: int) -> int:
    return x

def distribution_sort(xs: list, key = key_function) -> None:
    if not xs:
        return xs
    
    # Create keys
    keys = []

    for x in xs:
        keys.append(key_function(x))

    key = max(keys) + 1

    # Create blocks
    blocks = []
    for _ in range(key):
        blocks.append([])

    # Fill the blocks
    for x in xs:
        blocks[key_function(x)].append(x)

    # Join all blocks
    result = []
    for block in blocks:
            result.extend(block)

    # Return the sorted
    return result

def get_arr(arr_size: int) -> list:
    arr = []

    for i in range(arr_size):
        arr.append(random.randint(1, arr_size))

def test_random():
    arr_size = random.randint(10000, 1000000)
    arr = get_arr(arr_size)
    
    start_time = time.perf_counter()
    arr = distribution_sort(arr)
    end_time = time.perf_counter()

    final_time = end_time - start_time

    print(f"{arr_size} items sorted in {final_time:.6f} seconds")

def test_none() -> None:
    arr = distribution_sort(None)

def test_negative():
    arr_size = random.randint(-10, 10)

if __name__ == "__main__":
    test_random()

     

    