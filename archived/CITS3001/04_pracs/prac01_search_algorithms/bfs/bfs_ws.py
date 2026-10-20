from collections import deque

def bfs(adj_list, start) -> list:
    """
        Performance: O(V + E) worst case
            - Each reachable vertex visited once
            - Each reachable edge examined once
    """
    bfs_output = []
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        curr = queue.popleft()
        bfs_output.append(curr)

        # Iterate over neighbours; append if not seen before
        for n in adj_list[curr]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

    return bfs_output

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print(bfs(graph, 'A'))