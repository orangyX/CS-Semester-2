from typing import TypeVar

T = TypeVar('T')

def dfs_toposort(adj_list: dict[T, list[T]]) -> list[T] | None:
    visited = set()
    stack = []
    state = {node: 0 for node in adj_list}

    def dfs(u: T) -> bool:
        visited.add(u)
        # Visited state (but not fully processed)
        state[u] = 1

        for v in adj_list.get(u, []):
            # 1 denotes cycle detected
            if state.get(v, 0) == 1:
                return True
            # Not valid; exit upon a detected cycle
            if v not in visited:
                # Need to also check if a cycle occurs here (where the recursion implicitly returns true from the above branch)
                if dfs(v):
                    return True

        # Process only after its neighbours have been processed
        stack.append(u)
        # 2 denotes completely processed
        state[u] = 2
        return False

    # Invoke DFS on every node in adj_list
    for node in adj_list:
        if node not in visited:
            # Check for cycle; if true, topological ordering not possible
            if dfs(node):
                return None

    # Since we exited on the detected cycle, then len(stack) < len(adj_list) is true
    if len(stack) < len(adj_list):
        return None

    return stack[::-1]
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
    'B': ['A']
}

if __name__ == "__main__":
    print(dfs_toposort(graph))
    print(dfs_toposort(graph_str))
    print(dfs_toposort(adversarial))
    