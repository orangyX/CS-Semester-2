def toposort_recursive(adj_list):
    topo = []
    visited = set()
    state = {vertex: 0 for vertex in adj_list}

    def dfs(u) -> bool:
        visited.add(u)
        state[u] = 1

        for v in adj_list[u]:
            if state.get(v, 0) == 1:
                # Cycle detected
                return True
            if v not in visited:
                if dfs(v):
                    # Push true up the call stack
                    return True

        state[u] = 2
        topo.append(u)
        return False

    for vertex in adj_list:
        if vertex not in visited:
            # Return nothing if there is a cycle
            if dfs(vertex):
                return None

    return topo[::-1]

graph = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0, 1],
    5: [0, 2]
}

adversarial_graph = {
    1: [2],
    2: [1]
}


if __name__ == "__main__":
     print(toposort_recursive(graph))
     print(toposort_recursive(adversarial_graph))