import sys

def ford_fulkerson(adj_map: dict[int, dict[int, int]], src: int, snk: int) -> int:
    flow = 0 # Store the maximal flow
    residual = {u: {v: 0 for v in adj_map[u]} for u in adj_map} # The residual graph

    # Instantiation of back-edges; if a back-edge does not exist, we initialize it to 0
    for u in adj_map:
        for v in adj_map[u]:
            if u not in adj_map[v]: # Error here
                adj_map[v][u] = 0

    while True:
        path = find_augmenting_path(adj_map, residual, src, snk)

        if not path:
            break

        flow += push_flow(adj_map, residual, path)

    print(residual)

    return flow

def find_augmenting_path(adj_map: dict[int, dict[int, int]], residual: dict[int, dict[int, int]], src: int, snk: int) -> dict[int]:
    # DFS implementation
    parents = {} # Keep track of vertices + their parents
    stack = [(src, src)]

    while len(stack) > 0:
        p, u = stack.pop()

        parents[u] = p

        for v in adj_map[u]:
            if v not in parents and residual[u][v] < adj_map[u][v]:
                stack.append((u, v))

    if not parents:
        return None

    path = [src]

    while path[-1] != src:
        path.append(parents[path[-1]])
        path.reverse()

    return path


def push_flow(adj_map: dict[int, dict[int, int]], residual: dict[int, dict[int, int]], path):
    for u, v in zip(path, path[1:]):
        bottleneck = min(bottleneck, adj_map[u][v] - residual[u][v])

    # Updating the capacities
    for u, v in zip(path, path[1:]):
        residual[u][v] += bottleneck
        residual[v][u] += bottleneck

    return bottleneck

inputs = sys.stdin.read().split("\n")
inputs = [tuple(map(int, ln.split())) for ln in inputs if ln.strip()]
src, snk, v = inputs[0]
inputs = inputs[1:]

adj_map = {v: {} for v in range(v - 1)}

for u, v, w in inputs:
    adj_map[u][v] = w

print(ford_fulkerson(adj_map, src, snk))