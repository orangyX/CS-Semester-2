import sys
from collections import deque

mod_path = r"C:\Users\justi\Uni\2026\sem_02\CITS3001\03_case_studies\06_search_algorithms\adjacency_map"

if mod_path not in sys.path:
    sys.path.append(mod_path)

from adjacency_map import adjacency_map
from stack import stack

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

def dfs(adj_map: adjacency_map, starting_vertex) -> list:
    stack_ds = stack()

    stack_ds.push(starting_vertex)
    visited = set()
    visited.add(starting_vertex)
    dfs_result = []

    while len(stack_ds) > 0:
        curr = stack_ds.pop()
        dfs_result.append(curr)

        for n in adj_map[curr]:
            if n not in visited:
                visited.add(n)
                stack_ds.push(n)

    return dfs_result

if __name__ == "__main__":
    adj_map = get_graph()
    print(dfs(adj_map, 1))