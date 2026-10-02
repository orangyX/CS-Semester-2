import sys
import heapq

def prims(adj_map: dict[list[int]], t: int) -> tuple[int, int]:
    """
        Grow a tree of vertices from an initial vertex
    """

    pq = [] # Since Prim's algorithm uses a priority queue
    visited = set()
    mst = []

    redundant_edges = []
    running_cost = 0
    num_edges = 0

    for v, w in adj_map[0]:
        heapq.heappush(pq, (w, 0, v))

    visited.add(0)

    while pq:
        w, u, v = heapq.heappop(pq)

        if v in visited: # Adding this edge will introduce a cycle, so it is skipped
            redundant_edges.append((u, v, w))
            continue

        visited.add(v)
        mst.append((u, v, w))

        for x, w_i in adj_map[v]: # Process all neighbours of v
            if x not in visited:
                heapq.heappush(pq, (w_i, v, x)) 

    mst_sum = sum(map(lambda x: x[2], mst)) # The sum of the weights is a part of the solution

    if redundant_edges:
        redundant_edges = sorted(redundant_edges, key=lambda x: x[2]) # Non-sorted order, requires sorting by weight

        for _, _, w in redundant_edges:
            running_cost += w

            if running_cost > t:
                break

            num_edges += 1

    return mst_sum, num_edges

inputs = sys.stdin.read().split("\n")

edge_list = [tuple(map(int, line.split())) for line in inputs if line.strip()]
num_v, e, t = edge_list[0] # Although e isn't inherently necessary for this algorithm to work
edge_list = edge_list[1:]
adj_map = {num_v: [] for num_v in range(num_v)} # Primms operates on an adjacency list/map or matrix

for u, v, w in edge_list:
    adj_map[u].append((v, w))
    adj_map[v].append((u, w))

mst_sum, num_edges = prims(adj_map, t)
print(mst_sum, num_edges)