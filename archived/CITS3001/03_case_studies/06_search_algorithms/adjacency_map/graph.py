from adjacency_map import adjacency_map

import random

def graph_undirected() -> None:
    adj_map = adjacency_map()
    vertices = ["A", "B", "C", "D"]
    edges = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "D"), ("D", "A")]

    for vertex in vertices:
        adj_map.add_vertex(vertex)

    for edge in edges:
        adj_map.add_edge(edge[0], edge[1])

    print(adj_map.is_adjacent("A", "B"))

    adj_map.display()

def graph_directed() -> None:
    adj_map = adjacency_map()
    vertices = ["A", "B", "C", "D"]
    edges = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "D"), ("D", "A")]

    for vertex in vertices:
        adj_map.add_vertex(vertex)

    for edge in edges:
        adj_map.add_edge(edge[0], edge[1], random.randint(1, 20))

    adj_map.remove_vertex("A")
    adj_map.remove_edge("C", "D")

    adj_map.display()

def well_defined_graph() -> None:
    adj_map = adjacency_map()
    searchable = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "F"],
    "E": ["B"],
    "F": ["C", "D"]
    }

    for vertex, neighbours in searchable.items():
        adj_map.add_vertex(vertex)

        for neighbour in neighbours:
            adj_map.add_edge(vertex, neighbour, random.randint(1, 20), False)

    adj_map.display()

if __name__ == "__main__":
    # graph_undirected()
    # print("######")
    # graph_directed()
    well_defined_graph()