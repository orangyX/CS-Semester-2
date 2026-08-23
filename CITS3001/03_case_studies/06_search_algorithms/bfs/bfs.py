import sys
from collections import deque

mod_path = r"C:\Users\justi\Uni\2026\sem_02\CITS3001\03_case_studies\06_search_algorithms\adjacency_map"

if mod_path not in sys.path:
    sys.path.append(mod_path)

from adjacency_map import adjacency_map

def get_graph() -> dict:
    adj_map = adjacency_map()
    graph = {
        1: [6, 8, 15, 16],
        2: [7, 11, 15, 19],
        3: [5, 11, 20],
        4: [6],
        5: [3, 11, 19],
        6: [1, 4, 10, 11, 20],
        7: [2, 10, 11, 12, 17],
        8: [1],
        9: [15, 18],
        10: [6, 7],
        11: [2, 3, 5, 6, 7, 17],
        12: [7, 13],
        13: [12, 15, 20],
        14: [15, 19],
        15: [1, 2, 9, 13, 14, 16, 17, 18],
        16: [1, 15],
        17: [7, 11, 15, 18, 19],
        18: [9, 15, 17],
        19: [2, 5, 14, 17], 
        20: [3, 6, 13]
    }

    for vertex, neighbours in graph.items():
        adj_map.add_vertex(vertex)
        for neighbour in neighbours:
            adj_map.add_edge(vertex, neighbour)

    return adj_map

def bfs(adj_map: adjacency_map, starting_vertex) -> list:
    # Assume starting position is at 1

    if starting_vertex not in adj_map:
        raise ValueError(f"{starting_vertex} does not exist")

    # Instantiate the queue as the starting vertex [n]
    queue = deque([starting_vertex])
    # Set; recording all visited values
    visited = set()
    # Trivial; the first vertex is visited
    visited.add(starting_vertex)
    bfs_result = []

    while queue:
        # Dequeue; then append to the result
        curr = queue.popleft()
        bfs_result.append(curr)

        for n in adj_map[curr]:
            # Loop through the vertex list; add all neighbours that are not visited
            if n not in visited:
                # Now visited
                visited.add(n)
                # Enqueue; sits at the back of the queue, follows fifo ordering, prioritising level-to-level processing
                queue.append(n)

    # Final tc: O(V + E); iterates through all vertices, and all edges
    return bfs_result

if __name__ == "__main__":
    adj_map = get_graph()
    print(bfs(adj_map, 1))