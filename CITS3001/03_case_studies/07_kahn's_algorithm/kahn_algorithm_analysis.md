# 1. Algorithm overview
## 1.1. Purpose
Kahnb's algorithm is used to yield a topologically sorted sequence of visited vertices in a directed, acyclic graph, it does so by:
1. Selecting the vertex with in-degree 0
    * Note: in all DAG's, there must be one vertex with an in-degree of 0
2. Saving the vertex, then removing it from the graph, and updating the in-degree of affected neighbours
3. Selecting other vertices with in-degree's of 0; repeating in-degree updates on affected vertices
4. Continuing 2, 3 until no vertices in the graph are remaining; and all have been processed

## 1.2. Notes
* The graph must be directed
* Kahn's algorithm fails on cycles:
    * In a cycle, if A depends on B and B depends on A, this means that A must finish before accessing B, and B must finish before accessing A
    * A contradiction is yielded

# 2. Complexities
## 2.1. Time complexity
* O(V + E) time required:
    * Visits all vertices once
    * Examines all edges once