def dfs_bookkeeping(adj_list: dict[int, list[int]]) -> tuple[dict[int, int], dict[int, int]]:
    visited = set()
    discovery_times = {}
    finishing_times = {}
    timer = 0

    def dfs(u: int):
        nonlocal timer
        visited.add(u)
        timer += 1
        discovery_times[u] = timer

        for v in adj_list[u]:
            if v not in visited:
                dfs(v)

        timer += 1
        finishing_times[u] = timer

    for v in adj_list:
        if v not in visited:
            dfs(v)

    return discovery_times, finishing_times

adj_list = {
    0: [1, 2, 3],
    1: [2, 3],
    2: [3],
    3: [4, 5],
    4: [],
    5: [4]
}

if __name__ == "__main__":
    discover, finishing = dfs_bookkeeping(adj_list)

    print(discover)
    print(finishing)