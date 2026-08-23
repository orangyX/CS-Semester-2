from typing import TypeVar

# Generic type, which makes any data type compatible with this implementation
T = TypeVar('T')

def kosaraju(adj_list: dict[T, list]) -> list[list[T]]:
    """
        Finds all strongly connected compoennts in a graph.
            Time: O(V + E)
    """
    # First pass + instantiation
    visited: set[T] = set()
    stack: list[T] = []

    for vertex in adj_list:
        if vertex not in visited:
            stack.extend(dfs_postorder(adj_list, visited, vertex))

    # After the first pass
    transposed = transpose(adj_list)
    visited.clear()
    sccs: list[list[T]] = []

    # Pop from the stack; dfs exits when it cannot reach a component; this signals the presence of an scc
    while len(stack) > 0:
        current = stack.pop()

        # Check if visited; if visited, simply ignore the vertex
        if current not in visited:
            sccs.append(dfs_postorder(transposed, visited, current))

    return sccs


def transpose(adj_list: dict[T, list]) -> dict[T, list]:
    """
        Basic function; transposes an adjacency map G -> G^T
            Time: O(V + E)
    """
    transposed: dict[T, list] = dict()

    for vertex, edge in adj_list.items():
        for e in edge:
                # setdefault(e, []).append(v) -> circumvents key error; if e not in transposed, add key, along with [], then append the vertex
            transposed.setdefault(e, []).append(vertex)

    return transposed

def dfs_postorder(adj_list: dict[T, list], visited: set, root: T) -> list[T]:
    """
        Basic depth-first search post-order algorithm
            Time: O(V + E)
    """

    dfs_output = []

    def dfs(current: T):
        # We only wish to consider vertices that are unvisited
        if current not in visited:
            visited.add(current)

            for n in adj_list[current]:
                dfs(n)

            # Mark as complete when all neighbours have been visited
            dfs_output.append(current)

    # Invoke dfs
    dfs(root)

    return dfs_output


adj_list = {
    0: [1],
    1: [2],
    2: [3, 4],
    3: [0],
    4: [5],
    5: [6],
    6: [4, 7],
    7: []
}

if __name__ == "__main__":
    print(kosaraju(adj_list))