"""
This solution uses Kahn's algorithm with dynamic programming. 
It's slightly altered to use a queue for convenience. 

We have to do a pass forward then a similar backward pass.

Handle every prerequisite first. 
Uses a count to keep track of prerequisites.
Tasks with no prerequisites can begin immediately.
Update finish times of dependants. 
Once all prerequisites of a task is handled can be added to queue

Once the earliest launch time is found, walk backwards to find 
the latest a node can finish. If they are the same they're on the critical path.

*Both passes have the same complexity

Time complexity: O(N + M) where N is the number of tasks and M is the number of relations
BFS visits each node once and each edge only once.
Space: O(N + M) for the graph, counts queue and finish time values.
"""
from collections import defaultdict, deque
from typing import List


def launch_countdown(n: int, relations: List[List[int]], hours: List[int]) -> tuple[int, int]:

    # Build adjacency list and count prerequisites, fixing indexing here.
    adjacency_list = defaultdict(list)
    in_degree = [0] * n
    
    for prerequisite, check in relations:
        adjacency_list[prerequisite - 1].append(check - 1)
        in_degree[check - 1] += 1

    # Checks with no prerequisites start immediately.
    # Every duration is positive, so the 0 for other checks is always
    # overwritten by the max below.
    queue = deque()
    earliest = [0] * n
    for check in range(n):
        if in_degree[check] == 0: # Base case for DP
            queue.append(check)
            earliest[check] = hours[check]

    # Create topological order and recored earliest finish time.
    order = []
    while queue:
        curr = queue.popleft()
        order.append(curr)
        
        for succ in adjacency_list[curr]:
            # A check can only start once its slowest prerequisite is done.
            earliest[succ] = max(earliest[succ], earliest[curr] + hours[succ])
            
            # Once all prerequisites are handled, add it to the queue.
            in_degree[succ] -= 1
            if in_degree[succ] == 0:
                queue.append(succ)

    launch_time = max(earliest)

    # Backward pass. Create list for the latest a task can finish.
    latest = [launch_time] * n
    
    # Walk backwards through order and find previous node latest finish time.
    for curr in reversed(order):
        for succ in adjacency_list[curr]:
            # curr must finish before succ needs to start.
            latest[curr] = min(latest[curr], latest[succ] - hours[succ])

    # A check is critical if must be done at the latest finish time.
    # Earliest finish time == latest finish time.
    critical = sum(1 for check in range(n) if earliest[check] == latest[check])

    return launch_time, critical


# Get the data convert into ints, list and a list of lists.
tasks, relations = map(int, input().split())
times = list(map(int, input().split()))
relation_list = []

for i in range(relations):
    relation = list(map(int, input().split()))
    relation_list.append(relation)

launch_time, critical = launch_countdown(tasks, relation_list, times)
print(launch_time)
print(critical)