# 1. Algorithm description
## 1.1. Pushing flow
In order to push flow against a certain path in a graph, require:
* Augmenting path; that is a path from source (s) to sink(t)
* Bottleneck of the augmenting path: that is the maximal flow allowed along that path
    * Bottleneck found by taking the edge with the minimum capacity along that path

Residual graph
* Denotes the capacity remaining along each edge
* When flow is pushed along a path, in the augmented path, that amount is represented via a *reversed* edge
    * If there is no capacity left, the edge is completely reversed; it disappears from the graph, with no remaining capacity
* Yields the augmenting path; from that path, compute the bottleneck in order to push the maximal amount of flow

BFS
* BFS will traverse the graph, continually fetching distinct augmenting paths
    * Along each path, push by the bottleneck amount; undoing flow where necessary
    * By means of greed, able to yield the maximal flow
* Better than DFS; tends to avoid edges with a very low flow

## 1.2. Complexity attributes
### 1.2.1. Time complexity
DFS:
* O(|)

# 2. Implementation
pseudocode.
    define ford_fulkerson(args: adjacency_matrix, src, snk) yield int denoting the maximal flow through the network
        let current_flow = 0

        while parent yielded from bfs (augmenting path):
            let bottleneck = infinity
            let curr = snk

            while curr is not src:
                let prev = parent of curr

                if adjacency_matrix[prev][curr] < bottleneck:
                    set bottleneck = adjacency_matrix[prev][curr]

                curr = prev # walk up the chain

            let curr = snk

            while curr is not src:
                let prev = parent of curr

                adjacency_matrix[prev][curr] -= bottleneck; flow push
                adjacency_matrix[curr][prev] += bottleneck; flow in the mirrored direction; this is refundable

                curr = prev 

            current_flow += bottleneck

        yield bottleneck

    def bfs(args: adjacency_matrix, src, snk):
        let queue be a double ended queue
        let visited be a set storing visited vertices
        let parent be the parent to a node

        while queue is non-empty:
            for all nxt in range(len(cap[curr])):
                if cap[curr][nxt] > 0 and nxt is not visited:
                    parent[nxt] = curr
                    mark nxt as visited
                    append nxt to queue

                    if nxt is snk:
                        yield parent