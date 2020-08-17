def partition(input_list, start, end):
    pivot = input_list[end]
    i = start - 1

    for j in range(start, end):
        if input_list[j] > pivot:
            i += 1
            input_list[i], input_list[j] = input_list[j], input_list[i]

    input_list[i + 1], input_list[end] = input_list[end], input_list[i + 1]

    return i + 1


def quick_sort(input_list, start, end):
    if start < end:
        pivot_index = partition(input_list, start, end)
        quick_sort(input_list, start, pivot_index - 1)
        quick_sort(input_list, pivot_index + 1, end) 


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:
        return None

    quick_sort(input_list, 0, len(input_list) - 1)

    len_input = len(input_list)
    sample_size = len_input // 2
    if len_input % 2 == 1:
        sample_size += 1

    first = ""
    second = ""
    i = 0
    while i < len(input_list):
        first += str(input_list[i])
        if i + 1 < len(input_list):
            second += str(input_list[i + 1])
        i += 2

    return [int(first), int(second)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]

    if output is None and solution is None:
        print("Pass")
    elif sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


#########################################
## Tests
#########################################

test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case)

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case = [[0], None]
test_function(test_case)

test_case = [[0, 0], [0, 0]]
test_function(test_case)

test_case = [[1000, 0], [0, 1000]]
test_function(test_case)

test_case = [[5, 8, 7, 6, 9, 4], [975, 864]]
test_function(test_case)
