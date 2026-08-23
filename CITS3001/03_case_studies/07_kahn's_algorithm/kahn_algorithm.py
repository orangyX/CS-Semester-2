from typing import TypeVar
from collections import deque

# Generic
T = TypeVar('T')

def kahn(adj_list: dict[T, list[T]]) -> list[T] | None:
    n = len(adj_list)
    # Record the degrees of every vertex (done via a map to make possible for varying data types)
    in_deg = {node: 0 for node in adj_list}
    topo = []

    for _, edges in adj_list.items():
        for v in edges:
            if v not in in_deg:
                in_deg[v] = 0
            # For each incident edge, the degree += 1
            in_deg[v] += 1

    # Add all vertices with in-degree of 0
    queue = deque([node for node, deg in in_deg.items() if deg == 0])

    while queue:
        # Fetch the vertex with in-degree 0
        top = queue.popleft()
        topo.append(top)

        # Remove that vertex from the graph; decrement in-degree of all vertices affected by removal
        for v in adj_list.get(top, []):
            in_deg[v] -= 1

            # Next candidate; no dependencies, so it can be processed next
            if in_deg[v] == 0:
                queue.append(v)

    # Cycle detection; was unable to process co-dependent vertices; hence why len(topo) < len(adj_list)
    if len(topo) < len(adj_list):
        return None

    return topo

graph = {
    0: [4, 5, 11],
    1: [2, 4, 8],
    2: [5, 6, 9],
    3: [6, 7, 12],
    4: [8, 13],
    5: [9, 10],
    6: [10, 14],
    7: [12, 15],
    8: [9, 13],
    9: [14],
    10: [14, 15],
    11: [13],
    12: [15],
    13: [14],
    14: [],
    15: []
}

graph_str = {
    'A': ['E', 'F', 'L'],
    'B': ['C', 'E', 'I'],
    'C': ['F', 'G', 'J'],
    'D': ['G', 'H', 'M'],
    'E': ['I', 'N'],
    'F': ['J', 'K'],
    'G': ['K', 'O'],
    'H': ['M', 'P'],
    'I': ['J', 'N'],
    'J': ['O'],
    'K': ['O', 'P'],
    'L': ['N'],
    'M': ['P'],
    'N': ['O'],
    'O': [],
    'P': []
}

adversarial = { 
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

other_adversarial = {
    1: [2],
    3: [4]
}

if __name__ == "__main__":
    print(kahn(graph))
    print(kahn(graph_str))
    print(kahn(adversarial))
    print(kahn(other_adversarial))