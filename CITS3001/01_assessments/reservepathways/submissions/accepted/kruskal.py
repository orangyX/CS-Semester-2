import sys

sys.setrecursionlimit(10000) # This might be needed if the inputs grow very large in a recursive implementation

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)] # An index i has a parent stored in the ith cell of the array
        self.rank = [0] * n # Tree height upper-bound

    def find(self, u: int) -> int:
        # Case: the node is the parent node itself
        if self.parent[u] == u:
            return u

        self.parent[u] = self.find(self.parent[u]) # Compression; point each node to the root as we search for the root
        return self.parent[u]

    def union(self, u, v) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v: # Merged to the same set; do nothing; this also indicates cycle detection
            return False

        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u # Merge v under u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v # Merge u under v
        else: # Tree sizes equal; choice of merge does not matter
            self.parent[root_u] = root_v # Merge v under u
            self.rank[root_v] += 1 # Since we have merged another tree under; the rank of u increases

        return True # Merge successful

def kruskals(edge_list: tuple[int, int, int], v: int, t: int) -> tuple[int, int]:
    edge_list = sorted(edge_list, key=lambda x: x[2]) # Sort in ascending order of edge weights, costs O(nlogn) time

    union_find = UnionFind(v) 
    network_sum = 0 # The sum of the edge weights in the minimum spanning tree; this shall be the output
    running_cost = 0
    redundant_edges = [] # This will store the edges introducing cycles; these are usually discarded by Kruskal's, but the problem calls for a greedy approach to use these
    num_edges = 0 # Num. edges which can be introduced into the network

    for u, v, w in edge_list:
        if union_find.union(u, v): # If not forming a cycle, we shall take the edge
            network_sum += w
        else:
            redundant_edges.append((u, v, w))

    for u, v, w in redundant_edges:
        running_cost += w

        if running_cost > t:
            break

        num_edges += 1

    return network_sum, num_edges
        
# Standard data processing
inputs = sys.stdin.read().split("\n")
edge_list = [tuple(map(int, line.split())) for line in inputs if line.strip()]
v, e, t = edge_list[0] # Although e isn't inherently necessary for this algorithm to work
edge_list = edge_list[1:]

network_sum, num_edges = kruskals(edge_list, v, t)
print(network_sum, num_edges)