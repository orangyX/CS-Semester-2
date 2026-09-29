import sys

def bellman_ford(edge_list: tuple[int, int, int], src: int, num_vertices: int) -> list[int]:
    """
        Standard bellman-ford algorithm; for each vertex, computes the minimum path weight from the src
            Complexity: O(V*E); for each iteration, since for each vertex, loop over all edges
    """
    distances = [float('inf')] * num_vertices
    distances[src] = 0
    prev = [None ] * num_vertices # This can be used to find the exact path for a given distance; access each index; acts like a linked-list

    for _ in range(num_vertices - 1):
        for u, v, w in edge_list:
            # Standard edge relaxation logic
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                prev[v] = u

    # Negative cycle check; ∃negative cycle -> path weight never settles; it infinitely reduces
    for u, v, w in edge_list:
        if distances[u] + w < distances[v]:
            return None

    return distances, prev
    
inputs = sys.stdin.readlines()
edge_list = []

for i in inputs:
    i = i.split()
    if not i:
        continue

    edge_list.append(tuple(int(j) for j in i))

v, src = edge_list[0][0], edge_list[0][1]
edge_list = edge_list[1:]

print(bellman_ford(edge_list, src, v)[0])