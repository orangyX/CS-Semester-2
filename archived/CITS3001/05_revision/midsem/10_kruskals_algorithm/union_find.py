class DisjointSet:
    """
        Standard union-find data structure; all operations are O(1) amortized; 
            - Union; hanging a smaller tree from a larger one is O(1)
            - Finding the root of a tree 
    """
    def __init__(self, size):
        # Initialised as [0, 1, 2, 3, ..., size - 1]
        self.parent = list(range(size))

        # The rank, which measures the depth of each tree
        self.rank = [0] * size

    def find(self, x):
        # Get the root of x by traversing to the root
        while self.parent[x] != x:
            x = self.parent[x]

        return x

    def union(self, x, y):
        # Get the roots of x, y
        root_x = self.find(x)
        root_y = self.find(y)

        # Reside within the same set, so there is nothing more to do
        if root_x == root_y:
            return

        # Naive version
        # self.parent[root_x] = root_y

        # Non-naive version
        if root_x != root_y:
            # Hang y beneath x
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_x] = root_y
            # Hang x beneath y
            elif self.rank[root_y] > self.rank[root_x]:
                self.parent[root_y] = root_x
            # Same size, either selection is fine; bump the rank up
            else:
                self.parent[root_x] = root_y
                self.rank[root_x] += 1
            # True since x and y do not reside within the same set
            return True
        # False if x, y reside within the same set (required strictly for Kruskal's to discern the presence of cycles)
        return False