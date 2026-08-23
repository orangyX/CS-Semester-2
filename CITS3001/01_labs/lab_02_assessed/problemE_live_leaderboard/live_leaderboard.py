
import heapq

def get_kth(finish_times: list[int], kth: int) -> list[int]:
    # The heap, always at size k, no more, no less
    kth_elements = []
    output = []

    # Fill the heap with the first k values (not kth) in the given array; for i < j, the output is -1 (since there aren't enough finishes to count the kth smallest)
    for i in range(kth):
        if i < kth - 1:
            # -1 if i < j
            output.append(-1)
        kth_elements.append(finish_times[i])

    heapq.heapify_max(kth_elements)
    finish_times = finish_times[kth - 1:]

    # Replace strictly if i < the top element in kth_elements
    for i in finish_times:
        if i < kth_elements[0]:
            # Heap replacement procedure; replace the top-most element with the faster run-time
            heapq.heapreplace_max(kth_elements, i)

        output.append(kth_elements[0])

    return output

# Standard input processing
input_1 = list(map(int, input().split()))
finish_times = list(map(int, input().split()))

num_finish_times, kth = input_1[0], input_1[1]

kth_runners = get_kth(finish_times, kth)

for k in kth_runners:
    print(k)