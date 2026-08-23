import sys

sys.path.append(r"C:\Users\justi\Uni\2026\sem_02\CITS3001\04_pracs\02_toposort")

from toposort import toposort_recursive

def longest_path(adj_list: dict[int, list[int]]) -> list[int]:
    longest = [0] * len(adj_list)

    # Loop through all vertices
    for v in toposort_recursive(adj_list):
        if adj_list[v] == []:
            longest[v] = 0

        else:
            max_path = 0
            for u in adj_list[v]:
                if longest[u] >= max_path:
                    max_path = longest[u]

                longest[v] = max_path + 1

    return longest

graph = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0, 1],
    5: [0, 2]
}

if __name__ == "__main__":
    print(longest_path(graph))