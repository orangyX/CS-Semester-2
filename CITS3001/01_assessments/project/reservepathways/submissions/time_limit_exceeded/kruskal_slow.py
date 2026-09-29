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

def kruskal(edge_list: list[tuple[int, int, int]], v: int) -> int:
    edge_list = sorted(edge_list, key=lambda x: x[2])
    union_find = UnionFind(v)
    mst_sum = 0

    for u, v, w in edge_list:
        if union_find.union(u, v):
            mst_sum += w

    return mst_sum

inputs = sys.stdin.read().split("\n")
edge_list = [tuple(map(int, line.split())) for line in inputs if line.strip()]
v, e = edge_list[0]
edge_list = edge_list[1:]

print(kruskal(edge_list, v))