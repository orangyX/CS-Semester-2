import sys

def kruskal_naive(edge_list: list[tuple[int, int, int]], v: int) -> int:
    """
        Naive implementation:
            - Consider MST of N-1 edges
            - Take the cheapest N-1 edges:
                - Cycles are not checked
                - Taking v-1 edges means that other edges might be left out
    """

    edge_list = sorted(edge_list, key=lambda x: x[2])
    mst_sum = 0

    for i in range(v-1):
        _, _, w = edge_list[i]

        mst_sum += w

    return mst_sum

inputs = sys.stdin.read().split("\n")
edge_list = [tuple(map(int, line.split())) for line in inputs if line.strip()]
v, e = edge_list[0]
edge_list = edge_list[1:]

print(kruskal_naive(edge_list, v))