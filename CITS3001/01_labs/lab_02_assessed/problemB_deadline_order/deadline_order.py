def counting_sort(date_array: list, data_range: int, offset_constant: int, date_component: int) -> list:
    output_arr = [0] * len(date_array)
    prefix_arr = [0] * data_range

    for item in date_array:
        prefix_arr[item[date_component] - offset_constant] += 1

    for i in range(1, len(prefix_arr)):
        # Compute the prefix sums
        prefix_arr[i] += prefix_arr[i - 1]

    for i in range(len(date_array), 0, -1):
        item = date_array[i - 1][date_component] - offset_constant
        index = prefix_arr[item] - 1
        output_arr[index] = date_array[i - 1]
        prefix_arr[item] -= 1

    return output_arr
    
def radix_sort(date_array: list) -> list:
    data_component = 0

    while data_component <= 2:
        min_data = float('inf')
        max_data = float('-inf')

        for item in date_array:
            min_data = item[data_component] if min_data > item[data_component] else min_data
            max_data = item[data_component] if max_data < item[data_component] else max_data
    
        offset_constant = min_data
        data_range = max_data - min_data + 1

        date_array = counting_sort(date_array, data_range, offset_constant, data_component)
        data_component += 1

    return date_array

# deadlines = int(input())
current_processed = 0

# while (current_processed < deadlines):
#     date_array.append(datetime.strptime(input(), "%d/%m/%Y"))
#     current_processed += 1

num_dates = 3


if __name__ == "__main__":
    date_array1 = []
    date_array2 = []

    str1 = "05/09/2026"
    str2 = "17/08/2026"
    str3 = "01/09/2026"

    str4 = "29/01/2026"
    str5 = "01/01/2027"
    str6 = "29/01/2026"

    str1 = str1.split("/")
    str2 = str2.split("/")
    str3 = str3.split("/")

    str4 = str4.split("/")
    str5 = str5.split("/")
    str6 = str6.split("/")

    tup1 = (int(str1[0]), int(str1[1]), int(str1[2]))
    tup2 = (int(str2[0]), int(str2[1]), int(str2[2]))
    tup3 = (int(str3[0]), int(str3[1]), int(str3[2]))

    tup4 = (int(str4[0]), int(str4[1]), int(str4[2]))
    tup5 = (int(str5[0]), int(str5[1]), int(str5[2]))
    tup6 = (int(str6[0]), int(str6[1]), int(str6[2]))

    date_array1.append(tup1)
    date_array1.append(tup2)
    date_array1.append(tup3)

    date_array2.append(tup4)
    date_array2.append(tup5)
    date_array2.append(tup6)

    print(radix_sort(date_array1))
    print(radix_sort(date_array2))