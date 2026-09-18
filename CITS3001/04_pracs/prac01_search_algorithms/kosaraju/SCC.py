import random

def scc(g: list[list[bool]]) -> list[list[int]]:

    dfs_order = [] # List of int vertices
    visited = [False for _ in g]

    def dfs(u: int):
        visited[u] = True
        for v in range(len(g)):
            if g[u][v] and not visited[v]:
                dfs(v)

        dfs_order.append(u)

    for u in range(len(g)):
        if not visited[u]:
            dfs(u)

    # Now transposition is required; second dfs is required
    visited = [False for _ in g]
    def dfs_2(u: int, sc: list[int]):
        visited[u] = True
        sc.append(u)
        for v in range(len(g)):
            if g[v][u] and not visited[v]:
                dfs_2(v, sc)
    sccs = []

    for i in range(len(g) - 1, -1, -1):
        if not visited[dfs_order[i]]:
            sc = []
            dfs_2(dfs_order[i], sc)
            sccs.append(sc)

    return sccs

def random_graph(n: int, density: float) -> list[list[bool]]:
    g = []

    for i in range(n):
        adj = []
        for j in range(n):
            adj.append(random.random() < density and not i == j)
        g.append(adj)

    return g
            

if __name__ == "__main__":
    g = random_graph(random.randint(10, 50), 0.05)
    for i in range(len(g)):
        for j in range(len(g)):
            print('1' if g[i][j] else '0', end = ' ')
        print('\n')

    print(scc(g))