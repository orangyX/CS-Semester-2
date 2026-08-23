def counting_sort_for_radix(arr: list[tuple[int]], exp: int):
    # Counting sort for radix sort; use decimal system (0 - 9)
    prefix_arr = [0] * 10
    output = [0] * len(arr)

    for i in arr:
        # Extract the room position, sort it by the room positions 
        room_position = i[0]
        # Compute the appropriate index, using the places in the room distance
        idx = (room_position // exp) % 10
        prefix_arr[idx] += 1

    for i in range(1, len(prefix_arr)):
        # Compute prefix sum
        prefix_arr[i] += prefix_arr[i - 1]

    # Reversed ensures stability; processing from left-to-right means that the first instance of the identical element is processed; this inverts order and probably makes the sort unstable
    for i in reversed(arr):
        # Extract room position
        room_position = i[0]
        # Compute the index of the room position in the prefix_arr to find the appropriate index in output
        idx = (room_position // exp) % 10
        output[prefix_arr[idx] - 1] = i
        # Decrement; the next room position (if the same) shall sit before the currently processed one
        prefix_arr[idx] -= 1

    return output

def radix_sort(arr: list[tuple[int]]) -> list[tuple[int]]:
    # Exponent; calculate the place
    exp = 1
    max_val = float('-inf')

    for i in arr:
        # Find the max within the array; this shall be used for radix sort and counting sort as a termination condition
        if max_val < i[0]:
            max_val = i[0]

    while max_val // exp > 0:
        arr = counting_sort_for_radix(arr, exp)
        # Move to the next place; units -> tens -> hundreds -> ...
        exp *= 10

    return arr

def get_median_room_position(arr: list[tuple[int]]) -> int:
    student_sum = 0

    # Required for determining student density
    for i in arr:
        student_sum += i[1]

    # Find where most of the students are concentrated; use student_sum / 2; this yields the student density
    tipping_sum = student_sum / 2
    # Track the current sum; terminate when the running sum > tipping_sum
    running_sum = 0
    # Set this immediately when running_sum > tipping_sum
    median_index = 0

    for i in range(len(arr)):
        # Increment the sum
        running_sum += arr[i][1]

        if (running_sum >= tipping_sum):
            median_index = i
            break

    # Extract position information
    ideal_position = arr[median_index][0]
    return ideal_position

def get_minimum_distance(arr: list[tuple[int]], median_room_position: int) -> int:
    minimum_total_distance = 0

    # Compute the minimum total distance; the sum of students in room x_i * distance to room p as provided
    # This sum calculates the distance students have to travel from every room to reach the water station
    for i in arr:
        minimum_total_distance += i[1] * abs(median_room_position - i[0])

    return minimum_total_distance
    
num_rooms = int(input())
rooms = []
# Use this to acquire the correct number of inputs; afterall, each room is considered an independent input
inputs_taken = 0

while inputs_taken < num_rooms:
    io = input().split(" ")
    rooms.append((int(io[0]), int(io[1])))
    inputs_taken += 1

rooms = radix_sort(rooms)
median_room_position = get_median_room_position(rooms)
minimum_total_distance = get_minimum_distance(rooms, median_room_position)
print(str(median_room_position) + " " + str(minimum_total_distance))