"""
In this case we use a topological BFS approach.

Instead of proacitvely tracking the in edges we simply loop
through and check for nodes that dont have any more prerequisites.

This means a node can be visited many times, this pushes the 
time complexity from O(N + M) -> O(N(N + M))
Though it still maintains a O(N + M) space complexity

This will fail when large reversed chains are input
"""

from typing import List

def time_limit(n: int, relations: List[List[int]], times: List[int]) -> tuple[int, int]:
        
    prerequisites = [[] for _ in range(n)]          
    successors = [[] for _ in range(n)]

    # Process the relations and also fix indexing here.
    # prerequisite: courses
    for prerequisite, task in relations:
        prerequisites[task - 1].append(prerequisite - 1)
        successors[prerequisite - 1].append(task - 1)
    # Lists for storing DP finish times
    # Done for tracking completed nodes
    # Completed for taking node progress
    finish = [0] * n
    state = [False] * n
    completed = 0
    order = []
    
    # Loop until ALL nodes are seen
    while completed < n:
        
        # If a node completed, skip
        for task in range(n):
            if state[task]:
                continue

            # Check all prerequisites of a node if they've been processed
            # before continuing to complete calculation
            ready = True
            for value in prerequisites[task]:
                if not state[value]:
                    ready = False
                    break
            
            # Calculate node finishing time.
            if ready:
                latest = 0
                for previous in prerequisites[task]:
                    latest = max(latest, finish[previous])

                finish[task] = latest + times[task]
                state[task] = True
                completed += 1
                order.append(task)

    launch_time = max(finish)

    # Backward pass. Create list for the latest a node can finish.
    latest = [launch_time] * n

    # Walk backwards. Each node must finish before the nodes after it need to start.
    for task in reversed(order):
        for succ in successors[task]:
            # Keep the earliest start deadline of the nodes after it.
            latest[task] = min(latest[task], latest[succ] - times[succ])

    # A node is critical if it has no spare time.
    # Earliest finish time == latest finish time.
    critical = sum(1 for task in range(n) if finish[task] == latest[task])

    return launch_time, critical

# Get the data convert into ints, list and a list of lists.
tasks, relations = map(int, input().split())
times = list(map(int, input().split()))
relation_list = []

for i in range(relations):
    relation = list(map(int, input().split()))
    relation_list.append(relation)

launch_time, critical = time_limit(tasks, relation_list, times)
print(launch_time)
print(critical)