import sys
import heapq

def dijkstra(adj_map: dict[list[tuple[int, int]]], src: int, num_vertices: int) -> list[int]:
    # These values shall record the best known value specific to the vertices
    distances = [float('inf')] * num_vertices
    distances[src] = 0
    heap = []
    heapq.heappush(heap, (0, src)) # Required; each pop shall yield the minimum in O(lgN) time

    while heap:
        # Yield: best current known distance, and a vertex u
        d, u = heapq.heappop(heap)

        # Stale node; we skip
        if d > distances[u]:
            continue

        for v, w in adj_map[u]:
            # Edge relaxation: if found distances[u] + w < distances[v], we then record the new best distance, and push that vertex (w/ distance) to heap
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                heapq.heappush(heap, (distances[v], v))

    return distances

inputs = sys.stdin.read().split("\n")
cleaned = []

num_vertices, src = map(int, inputs[0].split())
adj_map = {u: [] for u in range(num_vertices)}

for line in inputs[1:]:
    parts = line.split()

    if not parts:
        continue

    u, v, w = map(int, parts)

    adj_map[u].append((v, w)) 

print(dijkstra(adj_map, src, num_vertices))