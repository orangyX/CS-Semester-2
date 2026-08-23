from typing import TypeVar
from collections import deque

T = TypeVar('T')

def kahn(adj_list: dict[T, list[tuple[T, int]]]) -> list[T]:
    in_deg = {node: 0 for node in adj_list}
    topo = []

    for _, edges in adj_list.items():
        for v in edges:
            v = v[0]
            in_deg[v] += 1

    queue = deque([node for node, deg in in_deg.items() if deg == 0])

    while queue:
        top = queue.popleft()
        topo.append(top)

        for v in adj_list.get(top, []):
            v = v[0]
            in_deg[v] -= 1

            if in_deg[v] == 0:
                queue.append(v)

    if len(topo) < len(adj_list):
        return None

    return topo

def minimum_path(adj_list: dict[T, list[T]], source: T) -> list[T]:
    top_order = kahn(adj_list)

    dist = [None] * len(adj_list)

graph = {
    0: [(4, 2), (5, 1), (11, 5)],
    1: [(2, 4), (4, 4), (8, 3)],
    2: [(5, 2), (6, 9), (9, 2)],
    3: [(6, 10), (7, 7), (12, 1)],
    4: [(8, 1), (13, 2)],
    5: [(9, 4), (10, 4)],
    6: [(10, 9), (14, 10)],
    7: [(12, 1), (15, 9)],
    8: [(9, 4), (13, 9)],
    9: [(14, 7)],
    10: [(14, 4), (15, 8)],
    11: [(13, 10)],
    12: [(15, 5)],
    13: [(14, 1)],
    14: [],
    15: []
}


if __name__ == "__main__":
    print(kahn(graph))
