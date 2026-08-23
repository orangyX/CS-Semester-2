from collections import deque

def maze_hop(matrix: list[list[str]], starting_pos: tuple[int], ending_pos: tuple[int]) -> list[tuple[int]] | int:
    solution = []
    queue = deque()
    visited = set()
    visited.add((starting_pos[0], starting_pos[1]))
    queue.append(starting_pos)

    # First issue of note: storing characters in the queue is pointless; when we dequeue, "." is of no help at all; store the coordinates instead
    # Why is it looping forever?
    # Because we were checking if something like (2, 3, 4) was in visited; no, cool, but then (2, 3, 5) would not be in visited either; infinite loop
    while queue:
        row_coord, col_coord, distance = queue.popleft()

        # Only save the final ending coordinate, along with the popped distance
        if (row_coord, col_coord) == (ending_pos[0], ending_pos[1]):
            solution.append((row_coord, col_coord, distance))

        # Compute neighbours, up, down, left, and right
        # Out of bounds cells are not treated as neighbours
        # "#" is never treated as a neighbour
        down_neighbour = (row_coord + 1, col_coord, distance + 1)
        up_neighbour = (row_coord - 1, col_coord, distance + 1)
        right_neighbour = (row_coord, col_coord + 1, distance + 1)
        left_neighbour = (row_coord, col_coord - 1, distance + 1)

        # Is the neighbour:
            # In invalid bounds?
            # In "#" state?
            # Visited?
        process_neighbour(down_neighbour, matrix, queue, visited)
        process_neighbour(up_neighbour, matrix, queue, visited)
        process_neighbour(right_neighbour, matrix, queue, visited)
        process_neighbour(left_neighbour, matrix, queue, visited)

    return solution

def process_neighbour(coord: tuple[int], matrix: list[list[str]], queue: deque[tuple[int]], visited: set[tuple[int]]) -> None:
    # Bounds checking was a big issue; in this implementation, the computations in the while queue sometimes forces an invalid bound
    # Checked for strictly g.t. relationship, must be >=
    if (coord[0] >= rows or coord[1] >= cols) or (coord[0] < 0 or coord[1] < 0):
        return
    # If #, we don't consider this
    elif matrix[coord[0]][coord[1]] == "#":
        return
    # All cases pass, all good
    else:
        if (coord[0], coord[1]) not in visited: # We need to test coordinate components only; having distance in this means that (2, 3, 4) and (2, 3, 5) are distinct
            visited.add((coord[0], coord[1]))
            queue.append(coord)

input_1 = list(map(int, input().split()))
rows = input_1[0]
cols = input_1[1]
current_row = 0

# Matrix instantiation
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

while current_row != rows:
    input_row = input()
    for i in range(len(input_row)):
        matrix[current_row][i] = input_row[i]

        if matrix[current_row][i] == "S":
            starting_pos = (current_row, i, 0)
        elif matrix[current_row][i] == "E":
            ending_pos = (current_row, i, None)
    current_row += 1

solution = maze_hop(matrix, starting_pos, ending_pos)

min_distance = float('inf')
for _, _, distance in solution:
    if distance < min_distance:
        min_distance = distance

min_distance = -1 if min_distance == float('inf') else min_distance

print(min_distance)