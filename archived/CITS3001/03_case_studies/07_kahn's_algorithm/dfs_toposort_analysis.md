# 1. Algorithm overview
DFS w/ toposort is used to yield a topologically sorted sequence of visited vertices (this is basically the same as Kahn's algorithm, only here, we use DFS instead of BFS).
1. Initialize a visited array -> marks whether each vertex has been visited or not
2. Create a stack -> stores vertices (in their finishing orders)
3. For each unvisited vertex, perform DFS from it
    * Within DFS, mark current vertex as visited
    * For each neighbour of the current vertex, if unvisited, invoke DFS on these vertices recursively
4. After visiting all neighbours, push the current vertex onto the stack
5. After DFS finishes, pop all elements from the stack, yielding topological ordering

