def buckets(xs: list, arr_size: int, max_size: int, num_buckets: int) -> list:
    # A list of num_buckets buckets
    buckets = [[] for _ in range(num_buckets)]
    output = []

    for i in range(arr_size):
        # Find bucket index, insert xs[i] into the bucket
        bucket = get_bucket(xs[i], max_size, num_buckets)
        buckets[bucket].append(xs[i])

    # Just length calculations
    for bucket in buckets:
        output.append(len(bucket))

    return output

def get_bucket(item, max_size, num_buckets) -> int:
    # Find where item sits between 0, 1 -> scale up to size of buckets by multiplication; truncate decimal component yielding a valid index
    return int(num_buckets * (item / max_size))

input_1 = input()
input_1 = list(map(int, input_1.split()))
xs = input()
xs = list(map(int, xs.split()))

arr_size, max_size, num_buckets = input_1[0], input_1[1], input_1[2]

print(buckets(xs, arr_size, max_size, num_buckets))