import sys

mod_path = r"C:\Users\justi\Uni\2026\sem_02\CITS3001\03_case_studies\06_search_algorithms\dfs"

if mod_path not in sys.path:
    sys.path.append(mod_path)

from dfs import stack

def dfs(adj_list, start) -> list:
    """
        Performance: O(V+E):
            - All reachable vertices are visited exactly once
            - All reachable edges are examined exactly once
    """
    if start not in adj_list:
        raise ValueError(f"Specified start does not exist ({start})")
    
    stack_ds = stack()
    visited = set()
    dfs_output = []

    visited.add(start)
    stack_ds.push(start)

    while len(stack_ds) > 0:    
        curr = stack_ds.pop()
        dfs_output.append(curr)

        for n in adj_list[curr]:
            if n not in visited:
                stack_ds.push(n)
                visited.add(n)

    return dfs_output

if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }

    print(dfs(graph, 'A'))
    # print(dfs(graph, "Z")) # Test error case

        