import sys

sys.setrecursionlimit(10000)

def kosaraju(adj_map: dict, origin: int, destination: int) -> list:
    """
        Algorithm for finding all SCC's
    """
    visited = set()
    finish_times = []
    sccs = []

    # Procure a list comprised of finishing times of all nodes
    dfs(adj_map, origin, visited, finish_times)

    visited.clear()
    transposed = transpose(adj_map)

    while len(finish_times) > 0:
        curr = finish_times.pop()

        if curr not in visited:
            instance_scc = []
            dfs(transposed, curr, visited, instance_scc)
            sccs.append(instance_scc)

    return sccs

# Used twice, in the initial pass to find the finish times, and the second pass, to find all SCC's
# Lines 11, 22
def dfs(adj_map: dict, src: int, visited: set, data_struct: list):
    visited.add(src)

    for v in adj_map[src]:
        if v not in visited:
            visited.add(v)
            dfs(adj_map, v, visited, data_struct)

    data_struct.append(src)

# Standard graph transposition; in an SCC, any subset of vertices should be able to reach one another, irrespective of a transposed graph
# Line 14
def transpose(adj_map: dict) -> dict:
    transposed = {}

    # Create keys : list
    for v in adj_map:
        transposed[v] = []

    # Fill; for every every neighbour of v, we reverse the edge
    for v in adj_map:
        for n in adj_map[v]:
            transposed[n].append(v)

    return transposed

def get_demerits(adj_map: dict, sccs: list) -> int:
    v_scc_mapping = [None] * len(adj_map)

    for i in range(len(sccs)):
        for v in sccs[i]:
            v_scc_mapping[v] = i

    print(v_scc_mapping)
    print(sccs)


inputs = sys.stdin.read().splitlines()
# Splitting each list, since each list is current in the form ['a' 'b' 'c']
inputs = [ln.split() for ln in inputs]

# Also convert each element to an int
for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        inputs[i][j] = int(inputs[i][j])

num_places, origin, destination = inputs[0][0], inputs[0][1], inputs[0][2]

# Skip the first line
inputs = [ln for ln in inputs[1:]]

adj_map = {}

for i in range(len(inputs)):
    adj_map[i] = []

    for j in range(len(inputs[i])):
        if j == 0:
            continue

        adj_map[i].append(inputs[i][j])

sccs = kosaraju(adj_map, origin, destination)
get_demerits(adj_map, sccs)