import sys
from union_find import DisjointSet

def kruskal(edge_list: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    unique_vertices = set()

    # Form a set of all vertices
    for u, v, _ in edge_list:
        if u not in unique_vertices:
            unique_vertices.add(u)
        if v not in unique_vertices:
            unique_vertices.add(v)

    disjoint_set = DisjointSet(len(unique_vertices))
    mst = []

    for u, v, w in edge_list:
        # True if non-cycle; false if cycle
        if disjoint_set.union(u, v):
            mst.append((u, v, w))

    return mst

def get_sum_edges(mst: list[tuple[int, int, int]]) -> int:
    sum_w = 0

    for edge in mst:
        sum_w += edge[2]

    return sum_w

# Raw line extraction
inputs = sys.stdin.read().splitlines()
splitted_inputs = []

# Split each list of strings
for ln in inputs:
    splitted_inputs.append(ln.split())

# Convert each char to an int
for i in range(len(splitted_inputs)):
    splitted_inputs[i] = [int(x) for x in splitted_inputs[i]]

num_vertices, num_edges = splitted_inputs[0][0], splitted_inputs[0][1]

edge_list = []

# Create the edge list
for i in range(1, len(splitted_inputs)):
    u, v, w = splitted_inputs[i]
    edge_list.append((u, v, w))

# Sort by weight, in ascending order
edge_list = sorted(edge_list, key=lambda x: x[2])

mst = kruskal(edge_list)
print(get_sum_edges(mst))