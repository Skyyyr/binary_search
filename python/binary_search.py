def binary_search(number_to_search, list_values, iterations_right=0):
    mid_point = len(list_values) // 2
    mid_value = list_values[mid_point]
    if len(list_values) <= 1:
        return -1
    if number_to_search == mid_value:
        print(mid_value, iterations_right)
        return mid_point + iterations_right
    if number_to_search > mid_value:
        iterations_right += mid_point
        list_values = list_values[mid_point:]
    else:
        list_values = list_values[:mid_point]
    return binary_search(number_to_search, list_values, iterations_right)


# test case
print(binary_search(0, [1, 2, 7, 8]))
