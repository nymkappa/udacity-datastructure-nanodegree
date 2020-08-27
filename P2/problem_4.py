def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    # Ingore all the first 0 as they are already sorted
    if input_list is None:
        return None

    if len(input_list) <= 1:
        return input_list

    low_index = 0
    while low_index < len(input_list) and input_list[low_index] == 0:
        low_index += 1

    # Ingore all the last 2 as they are already sorted
    high_index = len(input_list) - 1
    while high_index >= 0 and input_list[high_index] == 2:
        high_index -= 1

    mid_index = low_index

    while mid_index <= high_index:
        if input_list[mid_index] == 0:
            input_list[mid_index], input_list[low_index] = input_list[low_index], input_list[mid_index] 
            low_index += 1
            mid_index += 1

        elif input_list[mid_index] == 2:
            input_list[mid_index], input_list[high_index] = input_list[high_index], input_list[mid_index] 
            high_index -= 1

        elif input_list[mid_index] == 1:
            mid_index += 1

        else:
            return None

    return input_list


def contains_only_012(test_case):
    for i in test_case:
        if i not in [0, 1, 2]:
            return False
    return True


#########################################
## Tests
#########################################


def test_function(input_vals, expected):
    input_vals_cpy = input_vals.copy()
    sorted_array = sort_012(input_vals)
    print("Input", input_vals_cpy, "Expected", expected)
    assert(sorted_array == expected)


input_vals = []
expected = sorted(input_vals)
test_function(input_vals, expected)

input_vals = [0, 2, 1, 3]
expected = sorted(input_vals)
test_function(input_vals, None)

input_vals = [0, 2, 0, 0, 0, 0]
expected = sorted(input_vals)
test_function(input_vals, expected)

input_vals = [0, 0, 0, 0]
expected = sorted(input_vals)
test_function(input_vals, expected)
input_vals = [2, 2, 2, 2]
expected = sorted(input_vals)
test_function(input_vals, expected)

input_vals = [1, 1, 1, 1]
expected = sorted(input_vals)
test_function(input_vals, expected)

input_vals = [2, 0]
expected = sorted(input_vals)
test_function(input_vals, expected)

input_vals = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
expected = sorted(input_vals)
test_function(input_vals, expected)

input_vals = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
expected = sorted(input_vals)
test_function(input_vals, expected)

input_vals = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
expected = sorted(input_vals)
test_function(input_vals, expected)

print("All test passed")