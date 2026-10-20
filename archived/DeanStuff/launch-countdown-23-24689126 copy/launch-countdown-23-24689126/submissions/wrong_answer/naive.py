"""
This solution uses the task ordering to process the tasks
This avoids the topological component.

This structure is not guaranteed in the project description
and can cause a prerequisite to make an assumption on
its wait time and incorrectly return the time.

This will fail when chains are out of loop

This is sitll O(N + M) for time and space 
"""


from typing import List

def naive(n: int, relations: List[List[int]], times: List[int]) -> tuple[int,int]:
        
        
    prerequisites = [[] for _ in range(n)]   
    successors = [[] for _ in range(n)]       
    
    # Process the relations and also fix indexing here.
    # prerequisite: courses
    for prerequisite, task in relations:
        prerequisites[task - 1].append(prerequisite - 1)
        successors[prerequisite - 1].append(task - 1)
    
    # Track the finish times using DP
    finish = [0] * n

    # Loop through and take the longest chain
    for task in range(n):
        wait_time = 0
        for previous in prerequisites[task]:
            wait_time = max(wait_time, finish[previous])


        finish[task] = wait_time + times[task]

    launch_time = max(finish)

    # Backward pass. Create list for the latest a task can finish.
    latest = [launch_time] * n

    # Walk backwards in number order (N down to 1) instead of a proper order.
    # Wrong if a task comes after one with a higher number.
    for task in reversed(range(n)):
        for succ in successors[task]:
            # Keep the earliest start deadline of the tasks after it.
            latest[task] = min(latest[task], latest[succ] - times[succ])

    # A task is critical if it has no spare time.
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

launch_time, critical = naive(tasks, relation_list, times)
print(launch_time)
print(critical)