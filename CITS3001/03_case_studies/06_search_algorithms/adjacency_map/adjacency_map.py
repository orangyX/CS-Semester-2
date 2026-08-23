from VertexNotFoundError import VertexNotFoundError
from EdgeNotFoundError import EdgeNotFoundError

class adjacency_map:
    def __init__(self):
        self.adj_list = {}

    def __getitem__(self, vertex) -> list:
        if vertex not in self.adj_list:
            raise VertexNotFoundError(f"Vertex does not exist ({vertex})")

        return self.adj_list[vertex]

    def add_vertex(self, vertex) -> None:
        if vertex not in self.adj_list:
            self.adj_list[vertex] = {}

    def add_edge(self, vertex_a, vertex_b, weight=None, bidirectional=True) -> None:
        # O(1); constant time operation
        self.add_vertex(vertex_a)
        self.add_vertex(vertex_b)

        # O(1) amortized
        self.adj_list[vertex_a][vertex_b] = weight

        if bidirectional:
            self.adj_list[vertex_b][vertex_a] = weight  

    def is_adjacent(self, vertex_a, vertex_b) -> bool:
        # O(V + E) operation; scan through vertices; then scan through the related vertice's list
        associated_list = self.adj_list[vertex_a]
        if vertex_a not in self.adj_list:
            raise VertexNotFoundError(f"Vertex not found ({vertex_a})")

        return vertex_b in self.adj_list[vertex_a]

    def remove_vertex(self, vertex):
        if vertex not in self.adj_list:
            raise VertexNotFoundError(f"Cannot remove a vertex that was never in the adjacency list ({vertex})")     

        # O(E) operation
        for neighbour in self.adj_list.keys():
            if vertex in self.adj_list[neighbour]:
                del self.adj_list[neighbour][vertex]

        # Total tc: O(V + E)
        return(self.adj_list.pop(vertex))

    def remove_edge(self, vertex_a, vertex_b, bidirectional=True):
        if vertex_a not in self.adj_list or vertex_b not in self.adj_list:
            raise EdgeNotFoundError(f"Cannot remove an edge that was never in the adjacency list ({vertex_a}: {vertex_b})")

        # O(V + E) operation
        del self.adj_list[vertex_a][vertex_b]

        if bidirectional:
            del self.adj_list[vertex_b][vertex_a]
        
    def display(self):
        for vertex, neighbours in self.adj_list.items():
            print(f"{vertex}: {neighbours}")

    def __iter__(self):
        return iter(self.adj_list)