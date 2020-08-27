def binary_search(input_list, number, start, end):
    # We only have two elements left, directly check them, end of recursion
    if end - start == 1:
        if input_list[start] == number:
            return start
        if input_list[end] == number:
            return end;
        return -1

    middle = (start + end) // 2
    if number == input_list[middle]:
        return middle

    # If left half is sorted, and number is between extremums, search there
    elif (input_list[start] <= input_list[middle - 1] and
        number >= input_list[start] and
        number <= input_list[middle - 1]):
        return binary_search(input_list, number, start, middle - 1)

    # If right half is sorted, and number is between extremums, search there
    elif (input_list[middle + 1] <= input_list[end] and
        number >= input_list[middle + 1] and
        number <= input_list[end]):
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

    print("Input", test_case, "Expected", expected)
    assert(output == expected)


import random

for i in range(0, 10):
    arr = sorted(list(set([random.randint(0, 20) for i in range(20)])))
    search = random.randint(0, 20)
    test_function([arr, search])    

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])
test_function([[1, 2, 3], None])

print("All tests passed")
