def merge_sorted_arrays(array_one, array_two):
    merged_array = [None] * (len(array_one) + len(array_two))
    array_one_index = 0
    array_two_index = 0
    current_index = 0

    while array_one_index < len(array_one) and array_two_index < len(array_two):
        if array_one[array_one_index] <= array_two[array_two_index]:
            merged_array[current_index] = array_one[array_one_index]
            array_one_index += 1
        else:
            merged_array[current_index] = array_two[array_two_index]
            array_two_index += 1
        current_index += 1
    
    array_one_completed = array_one_index == len(array_one)
    remaining_array = array_two if array_one_completed else array_one
    last_index = array_two_index if array_one_completed else array_one_index

    for i in range(last_index, len(remaining_array)):
        merged_array[current_index] = remaining_array[i]
        current_index += 1

    return merged_array

array1 = [int(x) for x in input('Enter comma separated values for array one: ').split(',')]
array2 = [int(x) for x in input('Enter comma separated values for array two: ').split(',')]

print(merge_sorted_arrays(array1, array2))