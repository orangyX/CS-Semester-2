def counting_sort(date_array: list, data_range: int, offset_constant: int, date_component: int) -> list:
    # Store the outputs
    output_arr = [0] * len(date_array)
    # Array to calculate the indices of each value
    prefix_arr = [0] * data_range

    # Count the occurrences of the index in the array; subtract by the offset constant to adjust the domain
    # Example case: year is bounded in [1900, 2100]; the offset is the lowest value; thus 2100 - 1900 = 200; the prefix array shall be 200 items in size
    for item in date_array:
        prefix_arr[item[date_component] - offset_constant] += 1

    # Compute the prefix sums
    for i in range(1, len(prefix_arr)):
        prefix_arr[i] += prefix_arr[i - 1]  

    # For each entry in the prefix sum array; an entry at index n must occur at index n - 1
    # Method for insertion into the output_arr:
        # Find the item; this requires accessing the date array, using the date component, and subtracting the offset_constant
        # Look up the index using the computed item; the item shall be used to access the counts of that specific item in the prefix_arr
        # Use the index, insert into the output_arr
        # Decrement the no. instances in the prefix arr; this ensures that an item already inserted forces the same value to sit at position n-2: [a_1, a_2, ..., a_n-1, a_n-1] 
    for i in range(len(date_array), 0, -1):
        item = date_array[i - 1][date_component] - offset_constant
        index = prefix_arr[item] - 1
        output_arr[index] = date_array[i - 1]
        prefix_arr[item] -= 1

    return output_arr
    
def radix_sort(date_array: list) -> list:
    # Index of the date
    data_component = 0

    # Condition; loop upon the date component
    while data_component <= 2:
        # Find the min data; for any value <, set
        min_data = float('inf')
        # Find the max data; for any value >, set
        max_data = float('-inf')

        for item in date_array:
            # Find min (the offset constant)
            min_data = item[data_component] if min_data > item[data_component] else min_data
            # Find max; required to compute the number of indices required
            max_data = item[data_component] if max_data < item[data_component] else max_data
    
        offset_constant = min_data
        # Shrink to a valid data range; for year component; have 200 values, rather than 2100; where only the last 200 are used
        data_range = max_data - min_data + 1

        # Fetch the date array using the data
        date_array = counting_sort(date_array, data_range, offset_constant, data_component)
        # Bump this value; it progresses toward loop termination
        data_component += 1

    return date_array

def display(date_array: list) -> None:
    for i in date_array:
        # Convert each component to the appropriate output; for day, and/or date < 10; then something like 9 -> 09
        print(f"{i[0]:02d}/{i[1]:02d}/{i[2]}")

# Standard input collection
deadlines = int(input())
deadlines_list = []
# Use this to correctly acquire the correct no. dates, since each date is its own input
current_processed = 0

while (current_processed < deadlines):
    this_input = input().strip().split("/")
    this_input = (int(this_input[0]), int(this_input[1]), int(this_input[2]))
    deadlines_list.append(this_input)
    current_processed += 1

deadlines_list = radix_sort(deadlines_list)

# Print
display(deadlines_list)