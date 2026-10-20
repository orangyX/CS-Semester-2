"""
DFS with memoization

Runs a depth search for uncalculated tasks. 
Follow the prerequisites first. 
We can calculate the finish time after the wait time of the 
longest prerequisite chain is first calculated. 

This continuously updates the longest chain we are currently looking at
and keeps track of each prerequisite chain. 

This allows us to have a complexity of
O(N + M) Where N is the number of tasks and M is the number of relations.

We maintin the order we finished everything in so we can 
do the backwards path. 

Space complexity is also O(N + M) as the arrays and stack require
up to O(N + M) additional space
"""
from typing import List

def DFS_Solution(n: int, relations: List[List[int]], times: List[int]) -> tuple[int, int]:


    prerequisites = [[] for _ in range(n)]
    successors = [[] for _ in range(n)]
    # For each node, create a list of prerequesistes needed before continuing
    for u, v in relations:
        prerequisites[v-1].append(u-1)
        successors[u-1].append(v-1)

    # List to track finish time and state of each node 
    # 0 = unexplored, 1 = explored, 2 = calculated
    finish_time = [0] * n
    state = [0] * n
    
    order = []
    
    # Skip if a specific node has been calculated
    for task in range(n):
        if state[task] == 2:
            continue
        
        # Add task to the stack
        stack = [(task, False)]
        
        
        while stack:
            current, expanded = stack.pop()
            
            # If explored already skip
            if state[current] == 2:
                continue
            
            # Once a node has had all its prerequisites seen. 
            
            if expanded:
                wait_time = 0
                for index in prerequisites[current]:
                    # Take either the wait time or the largest finish time of a prerequisite.
                    wait_time = max(wait_time, finish_time[index])

                # Finish time of a node is the wait time + the time to complete a node
                finish_time[current] = times[current] + wait_time
                # Finalise in state
                state[current] = 2
                order.append(current)

            # If unexplored, append to stack as explored
            # Find unseen prerquisites and append to end of stack as unexplored to be seen first.
            # This will find all prerequisites needed for a task before calculating time needed.
            elif state[current] == 0:
                state[current] = 1
                stack.append((current, True))

                for value in prerequisites[current]:
                    if state[value] == 0:
                        stack.append((value, False))
                        
    launch_time = max(finish_time)
    # Backward pass. Create list for the latest a task can finish.
    latest = [launch_time] * n

    # Walk backwards. Each task must finish before the tasks after it need to start.
    for current in reversed(order):
        for succ in successors[current]:
            # Keep the earliest start deadline of the tasks after it.
            latest[current] = min(latest[current], latest[succ] - times[succ])

    # A task is critical if it has no spare time.
    # Earliest finish time == latest finish time.
    critical = sum(1 for task in range(n) if finish_time[task] == latest[task])

    return launch_time, critical


# Get the data convert into ints, list and a list of lists.
tasks, relations = map(int, input().split())
times = list(map(int, input().split()))
relation_list = []

for i in range(relations):
    relation = list(map(int, input().split()))
    relation_list.append(relation)

launch_time, critical = DFS_Solution(tasks, relation_list, times)
print(launch_time)
print(critical)