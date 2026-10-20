# Kosaraju's algorithm; case study
## 1. Algorithm overview
Kosaraju's algorithm is an algorithm designed to find all strongly connected components within a graph.

It makes use of DFS to identify all strongly connected components within the graph; it utilizes the principle that for any graph, a strongly connected component infers that a vertex can be reached by any other vertex within the subset. 

Transposing the graph should not change a strongly connected component; since if every vertex is reachable from every other vertex, a directional change has no effect on reachability

Hence, this feature is used to identify strongly connected components themselves; when DFS is invoked on a transposed graph, it returns the moment that it is unable to recur into another set of vertices.

Here, the stack is used to guide DFS, ensuring that it traverses the graph entirely, by feeding it starting points; DFS returns each time it identifies a strongly connected component, but while the stack is non-empty, DFS is essentially told to continue from the points which are fed by the stack.

The stack stores the finishing times of the vertices within the first invocation, since DFS can reach every component in the first call.    

## 2. Strongly connected components
A strongly connected component is a subset of vertices and edges of a graph G s.t. any vertex is reachable from any other vertex within the same strongly connected component.

Consider the following adjacency map:
    adj_map = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: [4]
        4: [5]
        5: [3, 6]
        6: []
    }

Within the above, observe that 0 -> 1 -> 2 -> 0; irrespective of the vertex selected within this subset of vertices, all other vertices in this subset are reachable:
* Select 0: from 2, we have that 2 -> 0
* Select 1: from 2, we have that 2 -> 0 -> 1
* etc.

However, 2 -> 3 (the other edge), is not a strongly connected component; it does not comprise this strongly connected component subset:
    - Select 1: 1 -> 2 -> 3, fine
    - Select 3: cannot travel into the set of vertices, hence it is not included within the set

For any vertex, a vertex itself is trivially considered to be a strongly connected component.

## 3. DFS algorithm (postoder)
In this case, we use DFS (postorder implementation) to identify all strongly connected components within the graph.

DFS works by pushing into a graph as deeply as possible, processing children before parents; in the event that a leaf is reached, we push this to the stack; due to a recursive implementation, the DFS algorithm unwinds on the call-stack, and yields the stack.

On the secondc all, while the stack is non-empty, vertices are popped and fed into DFS once more:
* DFS traverses all strongly connected components; returning when a vertex becomes unreachable
* DFS continues; it is fed vertices from the stack; it traverses every single strongly connected component; DFS assumes varying starting positions for each invocation
* When the stack empties, all vertices have been processed

## 4. Algorithm
We use depth-first search twice in order to find all strongly connected components of a particular graph; these is broken into three istinct phases:
* Phase 1: standard DFS algorithm; pushing to the stack when reaching the inner-most child; store a visitation set to mark vertices that are visited
* Phase 2: transpose the graph; within this algorithm, a component is considered strongly connected iff every vertex can reach every other vertex in the strong component, in both the regular graph, and transposed graph
* Phase 3: DFS upon the transposed graph; each time DFS reaches an unreachable component in the graph, it exits, returning the strongly connected component; while the length of the stack > 0, pop from the stack and call DFS
* Phase 4: return the strongly connected components

### 4.1. Pseudocode for Kosaraju's algorithm
```
define kosaraju(adjacency_list) -> scc:
    set visited = set()
    set stack = []

    for every vertex in the adjacency_list:
        if vertex not in visited:
            invoke dfs(adjacency_list, visited, vertex)

    transposed_graph = transpose(adjacency_list)
    visited.clear() -> this is particularly important
    sccs = []; a list to store sccs

    while stack is non-empty:
        current = stack.pop()

        if current not in visited:
            sccs.append(dfs_postoder(transposed, visited, current))

    yield sccs
```

```
define transpose(adjacency_list) -> transposed adjacency_list:
    transposed = []

    for all vertices, edges in adj_list.items():
        for edge in edges:
            transposed.setdefault(e, []).append(vertex); here, we are essentially just swapping everything

    yield transposed    
```

```
define dfs_postorder(adjacency_list, visited, root) -> list (stack in phase 1, scc in phase 2):
    dfs_output = []

    define dfs(current_vertex):
        if current_vertex is not visited:
            visited.add(current_vertex)
            
            for neighbours in adj_list[current_vertex]:
                dfs(neighbour)

            dfs_output.append(current_vertex) if all of its parents have been visited

    dfs(root) -> invoke dfs; then it will recursively invoke itself

    yield dfs_output
```

### 4.2. Algorithm attributes
#### 4.2.1. Time complexity
Standard time complexity for this algorihm is O(V + E):
* First DFS: DFS runs in O(V + E); it visits all vertices once, and examines all edges once
* Transposition: demains O(V + E); we must visit all vertices, and all edges in order to transpose the graph
* Second DFS: also runs in O(V + E) in order to process components in order of the finishing stack
* Total time: O(V + E) + O(V + E) + O(V + E) = O(V + E)

O(V + E) is yielded as the algorithm visits all vertices once, and examines each edge once.
#### 4.2.2. Space complexity
Kosaraju's algorithm requires O(V + E) space:
* Original graph is of size O(V + E) (adjacency list), or O(V^2) as an adjacency matrix
* Transposed graph: since Kosaraju's requires a transposition of the input graph, this is O(V + E) in space
* Visited set: O(V) space required to tabulate visited vertices
* Order stack: O(V) space required to store the finishing order of the vertices after DFS
* Total space complexity: 3*O(V + E) + 2*O(V) = O(V + E)