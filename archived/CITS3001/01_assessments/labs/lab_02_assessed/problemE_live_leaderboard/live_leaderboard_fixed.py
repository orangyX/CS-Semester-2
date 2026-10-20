import heapq

def get_kth(finish_times: list[int], kth: int) -> list[int]:
    # Since heapq_max is unavailable; inversion inputs and operations mimics a maxheap
    for i in range(len(finish_times)):
        finish_times[i] = -finish_times[i]

    # The heap, always at size k, no more, no less
    kth_elements = []
    output = []

    # Fill the heap with the first k values (not kth) in the given array; for i < j, the output is -1 (since there aren't enough finishes to count the kth smallest)
    # As long as i < kth; we need to append -1; hence kth - 1; we terminate as soon as i = kth, then append and heapify
    for i in range(kth - 1):
        if i < kth - 1:
            # -1 if i < j
            output.append(-1)
        kth_elements.append(finish_times[i])

    kth_elements.append(finish_times[kth - 1])
    heapq.heapify(kth_elements)
    # Append the kth runner, for now
    output.append(-kth_elements[0])

    # Replace strictly if i < the top element in kth_elements
    # We do not care about finish times at < kth
    for i in finish_times[kth:]:
        if i > kth_elements[0]:
            # Heap replacement procedure; replace the top-most element with the faster run-time
            heapq.heapreplace(kth_elements, i)

        # Transform back ot positives
        output.append(-kth_elements[0])

    return output

# Standard input processing
input_1 = list(map(int, input().split()))
finish_times = list(map(int, input().split()))

num_finish_times, kth = input_1[0], input_1[1]

kth_runners = get_kth(finish_times, kth)

for k in kth_runners:
    print(k)