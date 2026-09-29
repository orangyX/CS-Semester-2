import sys
from collections import deque

def ford_fulkerson(cap: list[list[int]], src: int, snk: int) -> int:
    """
        Edmond-Karps implementation: DFS is flawed, worst-case run time is O(|V|*|f|):
            * Time complexity: O(V*E^2); stictly polynomial unlike standard Ford-Fulkerson algorithm
            * O(V+E) space required to store an edge-list/adj-list; O(V^2) for matrix
    """

    flow = 0

    while (parent := bfs(cap, src, snk)):
        bottleneck = float('inf') # Here, we wish to find the bottle-neck of the augmenting path as the edge w/ the minimum flow 
        curr = snk # Set curr to sink to allow for iterability

        while curr != src:
            prev = parent[curr] # Find the parent of the current node

            if cap[prev][curr] < bottleneck: # Finds the minimum flow of the augmenting path
                bottleneck = cap[prev][curr]

            curr = prev # Walk up the chain, from the snk

        curr = snk # Second iteration; reset

        while curr != src:
            prev = parent[curr] # Where did we come from? get the parent

            cap[prev][curr] -= bottleneck # Push flow along the path of the original graph; less capacoty
            cap[curr][prev] += bottleneck # Add along the reverse path (mirror edge) of the residual path; we can "refund" flow if there is a better solution

            curr = prev 

        flow += bottleneck # The processed flow is added to the running total

    return flow
            
def bfs(cap: list[list[int]], src: int, snk: int) -> dict[int, int] | None:
    queue = deque([src])
    visited = {src}
    parent = {}

    while queue:
        curr = queue.popleft()

        # Also fetch the nxt coordinate
        for nxt in range(len(cap[curr])):
            # Shall ignore 0 entries or visited entries
            if cap[curr][nxt] > 0 and nxt not in visited:
                visited.add(nxt)
                parent[nxt] = curr
                queue.append(nxt)

                # Indentation here is important: if nxt == snk, immediately return
                if nxt == snk:
                    # The path, and it terminates the moment we find snk
                    return parent

    return None

inputs = sys.stdin.read().split("\n")
edges = [tuple(map(int, item.split())) for item in inputs if item.strip()]

n, src, snk = edges[0]
edges = edges[1:]

cap = [[0] * n for _ in range(n)]

for u, v, w in edges:
    cap[u][v] += w

print(ford_fulkerson(cap, src, snk))