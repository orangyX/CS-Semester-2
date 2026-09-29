import sys

def lab_booking(bookings):
    # Sort by the ending times; important for our greedy algorithm
    bookings = sorted(bookings, key=lambda x: x[1])
    # First ending value needs to be stored, so that comparison is possible between the first state and next state
    prev_end = 0
    valid_requests = []

    for time in bookings:
        start, end = time

        # Consider if the booking end time starts after the most recent end time; if occurring in the booking, it becomes invalid
        if start >= prev_end:
            valid_requests.append((start, end))
            prev_end = end

    return len(valid_requests)

# Given something like [(1, 3), (2, 4), (3, 5), (6, 7)]
# Count:
    # 1, 3 (prev_end iter 1)
    # 2, 4 -> invalidated, since the start time occurs during the running time of 1, 3
    # 3, 5 -> valid, since 3 >= 3, this runs to 5
    # 6, 7 -> also valid, since 6 >= 5, it occurs after the finishing time of 3, 5

inputs = sys.stdin.read().split()
num_req = int(inputs[0])
bookings = []

for i in range(1, len(inputs), 2):
    bookings.append((int(inputs[i]), int(inputs[i+1])))

print(lab_booking(bookings))