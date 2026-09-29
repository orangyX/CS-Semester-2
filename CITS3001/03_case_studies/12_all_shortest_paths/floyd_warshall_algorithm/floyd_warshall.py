import sys

def floyd_warshall(matrix: list[list[float]], edge_list: list[list[int]], num_vertices: int) -> list[list[int]]:
    """
        Standard floyd-warshall algorithm; for each pair of vertices, find the cheapest costing path between
        Attributes:
            Time complexity: O(V^3); triple-nested loop
            Space complexity: O(V^2) required to construct the matrix
    """
    # A vertex to itself has a distance of 0
    for i in range(num_vertices):
        matrix[i][i] = 0

    # Put the edge weights down for already-established relations
    for u, v, w in edge_list:
        matrix[u][v] = min(matrix[u][v], w)

    # Use the standard formula; take A^k[i, j] = min(A^(k-1)[i, j], A^(k-1)[i, k] + A^(k-1)[k, j])
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    return matrix

inputs = sys.stdin.read().split("\n")
edge_list = []
num_vertices = 0

for line in inputs:
    part = list(map(int, line.split()))
    if not part:
        continue

    edge_list.append(part)

num_vertices = edge_list[0][0]
edge_list = edge_list[1:]
matrix = [[float('inf') for _ in range(num_vertices)] for _ in range(num_vertices)]

new_matrix = floyd_warshall(matrix, edge_list, num_vertices)

for row in new_matrix:
    print(row)