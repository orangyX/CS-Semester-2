import sys
from collections import deque

def bfs01(fwd: list, rev: list, src: int) -> list:
    queue = deque()
    # Measure distances from src to all other vertices
    distances = [float('inf') for _ in range(len(fwd))]

    distances[src] = 0
    queue.appendleft(src)

    while queue:
        curr = queue.popleft()

        # This incurs no cost (legal), so if a road exists, we take it if its cheaper
        for n in fwd[curr]:
            if distances[curr] < distances[n]:
                distances[n] = distances[curr]
                queue.appendleft(n)

        # This incurs a cost + 1 (illegal); if a road does not exist, we take +1 cost to traverse
        for n in rev[curr]:
            if distances[curr] + 1 < distances[n]:
                distances[n] = distances[curr] + 1
                queue.append(n)

    return distances

"""
    Inputs processing + setting up appropriate data structures
"""
inputs = sys.stdin.read().splitlines()
# Splitting each list, since each list is current in the form ['a' 'b' 'c']
inputs = [ln.split() for ln in inputs]

# Also convert each element to an int
for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        inputs[i][j] = int(inputs[i][j])

num_places, src, dst = inputs[0][0], inputs[0][1], inputs[0][2]

# Skip the first line
inputs = inputs[1:]

# And also remove the num. roads from the place; it is useless here
for i in range(num_places):
    inputs[i] = inputs[i][1:]

# fwd: legal roads, rev: illegal roads
fwd = [[] for _ in range(num_places)]
rev = [[] for _ in range(num_places)]

# Build up the fwd, and rev (transposed); this shall have the legal and illegal directions
for i in range(num_places):
    for j in inputs[i]:
        fwd[i].append(j)
        rev[j].append(i)

# Travel from src -> dst, then dst -> src
first_leg = bfs01(fwd, rev, src)
second_leg = bfs01(fwd, rev, dst)

# The minimum demerits is the sum of the dst index of the first leg, and src index of the second leg
print(first_leg[dst] + second_leg[src])