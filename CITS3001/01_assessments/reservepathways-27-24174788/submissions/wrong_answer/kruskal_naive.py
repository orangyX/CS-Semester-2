import sys

def kruskal_naive(edge_list: list[tuple[int, int, int]], v: int, t: int) -> tuple[int, int]:
    edge_list = sorted(edge_list, key=lambda x: x[2])
    network_sum = 0
    running_sum = 0
    num_edges = 0
    edge_lst_used = set() # This will store the used edges; also use a set to circumvent TLE; we want to test for wrong answer, not a time out

    for i in range(v-1): # Naive assumption; a connected network is at least V - 1, so loop V - 1 times
        u, v, w = edge_list[i]
        edge_lst_used.add((u, v, w))
        network_sum += w

    for u, v, w in edge_list: # Naive assumption 2: any edge in used cannot be used; any edge not in used can be used provided that it is within cost limits
        if (u, v, w) in edge_lst_used:
            continue
        
        running_sum += w

        if running_sum > t:
            break

        num_edges += 1

    return network_sum, num_edges

inputs = sys.stdin.read().split("\n")
edge_list = [tuple(map(int, line.split())) for line in inputs if line.strip()]
v, e, t = edge_list[0]
edge_list = edge_list[1:]

network_sum, num_edges = kruskal_naive(edge_list, v, t)
print(network_sum, num_edges)