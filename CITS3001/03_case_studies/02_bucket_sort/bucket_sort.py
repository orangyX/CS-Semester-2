import random
import time

def bucket_sort(xs: list) -> list:
    arr_size = len(xs)

    if arr_size == 0:
        return xs

    # Create a list of buckets; buckets cardinality = list size
    buckets_list = [[] for _ in range(arr_size)]
    output_arr = []

    for i in xs:
        # Retrieve bucket index, then put the value into the acquired bucket index
        bucket = get_bucket(i, max(xs), arr_size)
        buckets_list[bucket].append(i)

    # Via insertion sort, sort each bucket in the buckets_list
    for i in range(len(buckets_list)):
        buckets_list[i] = sort_bucket(buckets_list[i])

    # Each bucket is sorted; append every value in each bucket, starting from first bucket to last bucket
    for bucket in buckets_list:
        output_arr.extend(bucket)

    return output_arr

def get_bucket(value: int, max_size: int, buckets) -> int:
    # Normalization: maps some value to [0, 1]; division by max_size + 1 ensures that the value is strictly less than 1
    # Scaling: the normalized factor is scaled to n bucketes; then truncated to ensure appropriate index mapping
    return int(buckets * (value / (max_size + 1)))

# Standard insertion sort algorithm; assumes that values are uniformly distributed across the table, and that each bucket is sufficiently small
def sort_bucket(block: list) -> list:
    for i in range(len(block)):
        j = i
        while j > 0 and block[j-1] > block[i]:
            block[j-1], block[i] = block[i], block[j-1]
            j -= 1

    return block

def get_arr(arr_size: int) -> list:
    xs = []

    for i in range(arr_size):
        xs.append(random.randint(0, arr_size))

    return xs


def test(xs: list) -> None:
    start_time = time.perf_counter()
    (bucket_sort(xs))
    end_time = time.perf_counter()

    final_time = end_time - start_time

    print(f"{len(xs)} items sorted in {final_time:.6f} seconds")

def test_adversarial(arr_size: int) -> None:
    xs = []

    for i in range(arr_size):
        xs.append(random.randint(1, 1000))

    start_time = time.perf_counter()
    (bucket_sort(xs))
    end_time = time.perf_counter()

    final_time = end_time - start_time

    print(f"{len(xs)} condensed items sorted in {final_time:.6f} seconds")

if __name__ == "__main__":
    arr_size = random.randint(10000, 25000)
    xs = get_arr(arr_size)

    test(xs)
    test_adversarial(arr_size)