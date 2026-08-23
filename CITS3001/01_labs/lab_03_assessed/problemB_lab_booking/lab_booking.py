import sys

def pivot(request_lst: list) -> list:
    pivot_index = len(request_lst) - 1
    pivot_val = request_lst[pivot][1]
    i = -1

    for j in range(request_lst):
        if request_lst[j][1] <= pivot_val:
            i += 1
            swap(request_lst, j, i)

    swap(request_lst, j, i + 1)

def swap(request_lst: list, j_idx: int, i_idx: int) -> None:
    request_lst[j_idx][1], request_lst[i_idx][1] = request_lst[i_idx][1], request_lst[j_idx][1]

inputs = sys.stdin.read().split()
print(inputs)
num_req = int(inputs[0])
request_lst = []

for i in range(1, num_req):
    request_lst.append((int(inputs[i]), int(inputs[i+1])))