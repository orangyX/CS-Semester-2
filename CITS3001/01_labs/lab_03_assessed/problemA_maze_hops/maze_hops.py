from collections import deque

def maze_hop(matrix: list[list[str]], starting_pos: tuple[int], ending_pos: tuple[int]) -> list[tuple[int]] | int:
    solution = []
    queue = deque()
    visited = set()
    visited.add(starting_pos)
    queue.append(starting_pos)

    # First issue of note: storing characters in the queue is pointless; when we dequeue, "." is of no help at all; store the coordinates instead
    # Why is it looping forever?
    while queue:
        row_coord, col_coord = queue.popleft()
        solution.append((row_coord, col_coord))

        # Compute neighbours, up, down, left, and right
        # Out of bounds cells are not treated as neighbours
        # "#" is never treated as a neighbour
        down_neighbour = (row_coord + 1, col_coord)
        up_neighbour = (row_coord - 1, col_coord)
        right_neighbour = (row_coord, col_coord + 1)
        left_neighbour = (row_coord, col_coord - 1)

        process_neighbour(down_neighbour, matrix, que
                          ue, visited)
        process_neighbour(up_neighbour, matrix, queue, visited)
        process_neighbour(right_neighbour, matrix, queue, visited)
        process_neighbour(left_neighbour, matrix, queue, visited)

    if len(solution) == 0:
        return -1

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
        if coord not in visited:
            visited.add(coord)
            queue.append(coord)
        

input_1 = list(map(int, input().split(" ")))
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
            starting_pos = (current_row, i)
        elif matrix[current_row][i] == "E":
            ending_pos = (current_row, i)
    current_row += 1

for i in matrix:
    print(i)

fucking_bullshit = maze_hop(matrix, starting_pos, ending_pos)
print(fucking_bullshit)
    