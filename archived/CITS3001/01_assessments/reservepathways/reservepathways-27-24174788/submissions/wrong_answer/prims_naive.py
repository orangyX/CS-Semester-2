import sys
import heapq

def prims_naive(adj_map: dict[list[tuple[int, int, int]]], num_v: int, t: int) -> tuple[int, int]:
    pq = []
    visited = set()
    mst = []

    redundant_edges = []
    running_cost = 0
    num_edges = 0

    for v, w in adj_map[0]: # Add all neighbours of vtx 0
        heapq.heappush(pq, (w, 0, v))

    visited.add(0)

    while len(mst) < num_v - 1: # This is the naive assumption; indeed, a tree has V-1 edges, but exiting here leaves edges unpopped from the pq
        w, u, v = heapq.heappop(pq)

        if v in visited:
            redundant_edges.append((u, v, w)) # The edge is not included in the mst; this this makes it eligible for greedy selection

        visited.add(v)
        mst.append((u, v, w)) # If the edge is unvisited 

        for x, w_i in adj_map[v]: # New edges discovered; push onto the priority queue
            if x not in visited:
                heapq.heappush(pq, (w_i, v, x))

    mst_sum = sum(map(lambda x: x[2], mst))

    if redundant_edges: # If no redundant edges, skip this, fall through to the return of 0
        redundant_edges = sorted(redundant_edges, key=lambda x: x[2])

        for _, _, w in redundant_edges: # Greedy edge selection
            running_cost += w

            if running_cost > t:
                break

            num_edges += 1

    return mst_sum, num_edges

# Data processing
inputs = sys.stdin.read().split("\n")
edge_list = [tuple(map(int, line.split())) for line in inputs if line.strip()]
num_v, e, t = edge_list[0] # Although e isn't inherently necessary for this algorithm to work
edge_list = edge_list[1:]
adj_map = {num_v: [] for num_v in range(num_v)} # Primms operates on an adjacency list/map or matrix

for u, v, w in edge_list:
    adj_map[u].append((v, w))
    adj_map[v].append((u, w))

mst_sum, num_edges = prims_naive(adj_map, num_v, t)
print(mst_sum, num_edges)