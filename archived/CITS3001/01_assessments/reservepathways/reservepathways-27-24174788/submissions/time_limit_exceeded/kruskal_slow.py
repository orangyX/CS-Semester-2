import sys
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, u) -> int:
        if self.parent[u] == u:
            return u

        # Iterative; a large chain of nodes will force a RecursionError
        while self.parent[u] != u:
            u = self.parent[u] # No path compression; simply walk up the chain to find the representative of u

        return u

    def union(self, u, v) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        self.parent[root_u] = root_v # Just hang it; we do not use the rank at all
        return True

def kruskal_slow(edge_list: list[tuple[int, int, int]], v: int, t: int) -> int:
    edge_list = sorted(edge_list, key=lambda x: x[2])
    union_find = UnionFind(v)
    network_sum = 0
    running_cost = 0
    redundant_edges = []
    num_edges = 0

    for u, v, w in edge_list:
        if union_find.union(u, v):
            network_sum += w
        else:
            redundant_edges.append((u, v, w))

    for u, v, w in redundant_edges:
        running_cost += w

        if running_cost > t:
            break

        num_edges += 1

    return network_sum, num_edges

inputs = sys.stdin.read().split("\n")
edge_list = [tuple(map(int, line.split())) for line in inputs if line.strip()]
v, e, t = edge_list[0]
edge_list = edge_list[1:]

network_sum, num_edges = kruskal_slow(edge_list, v, t)
print(network_sum, num_edges)