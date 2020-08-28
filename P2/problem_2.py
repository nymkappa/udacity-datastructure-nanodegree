def binary_search(input_list, number, start, end):
    # We only have two elements left, directly check them, end of recursion
    if start >= end:
        if number == input_list[start]:
            return start;
        else:
            return -1

    middle = (start + end) // 2
    if number == input_list[middle]:
        return middle

    middle_value = input_list[middle]
    # print(middle, middle_value)
    end_value = input_list[end]
    start_value = input_list[start]

    if middle_value < end_value:
        if number > middle_value and number <= end_value:
            return binary_search(input_list, number, middle + 1, end)
        else:
            return binary_search(input_list, number, start, middle - 1)
    else:
        if number >= start_value and number <= middle_value:
            return binary_search(input_list, number, start, middle - 1)
        else:
            return binary_search(input_list, number, middle + 1, end)

    return -1
        

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0 or input_list is None or number is None:
        return -1

    return binary_search(input_list, number, 0, len(input_list) - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


#########################################
## Tests
#########################################

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]

    expected = linear_search(input_list, number)
    output = rotated_array_search(input_list, number)

    # print("Input", test_case, "Expected", expected, "Got", output)
    assert(output == expected)


import random

for i in range(0, 10):
    arr = sorted(list(set([random.randint(0, 20) for i in range(20)])))
    search = random.randint(0, 20)
    test_function([arr, search])    

test_function([[3, 4, 5, 6, 1, 2], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])
test_function([[1, 2, 3], None])

test_list=[i for i in range (1011,10000)]+[i for i in range (0,1011)]
test_function([test_list, 6])
test_list=[i for i in range (1011,10000)]+[i for i in range (-1000,1011)]
test_function([test_list, 6])

print("All tests passed")
