import sys

def prims_slow(adj_map: dict[list[tuple[int, int, int]]], edge_list: list[tuple[int, int, int]], num_v: int, t: int) -> tuple[int, int]:
    distances = [float('inf') for _ in range(num_v)]
    visited = set()
    mst_sum = 0
    mst_edge_costs = []

    running_cost = 0
    num_edges = 0

    distances[0] = 0

    while len(visited) < num_v:
        x = None # This shall store the ve

        for u in range(num_v):
            if u not in visited:
                if x is None or distances[u] < distances[x]:
                    x = u

        if x != 0:
            mst_sum += distances[x] # Safe; distances[x] is the cheapest edge crossing a split, hence taking it is optimal
            mst_edge_costs.append(distances[x])
        visited.add(x)

        for v, w in adj_map[x]:
            if v not in visited and w < distances[v]:
                distances[v] = w

    for mst_w in mst_edge_costs:
        for i, (_, _, w) in enumerate(edge_list):
            if mst_w == w:
                edge_list.pop(i)
                break

    edge_list = sorted(edge_list, key=lambda x: x[2])

    for _, _, w in edge_list:
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

mst_sum, num_edges = prims_slow(adj_map, edge_list, num_v, t)
print(mst_sum, num_edges)