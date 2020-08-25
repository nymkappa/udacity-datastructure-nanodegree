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


def test_function(test_case):
    save = test_case.copy()
    sorted_array = sort_012(test_case)

    if save == None and sorted_array == None:
        print("Pass:", "Tested", save)
    elif not contains_only_012(test_case) and sorted_array == None:
        print("Pass:", "Tested", save)
    elif sorted_array == sorted(test_case):
        print("Pass:", "Tested", save)
    else:
        print("Fail:", "Tested", save)


#########################################
## Tests
#########################################

test_function([])
test_function([0, 2, 1, 3])
test_function([0, 2, 0, 0, 0, 0])
test_function([0, 0, 0, 0])
test_function([2, 2, 2, 2])
test_function([1, 1, 1, 1])
test_function([2, 0])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])