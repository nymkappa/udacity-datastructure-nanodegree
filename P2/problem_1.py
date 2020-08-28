def binary_search_square_root(number, start, end):
    middle = (start + end) // 2
    square = middle * middle
    
    # We found the exact square root or the binary search is over
    if square == number or start >= end:    
        return middle

    if square > number:
        # Search the left side
        res = binary_search_square_root(number, start, middle - 1)
    else:
        # Search the right side
        res = binary_search_square_root(number, middle + 1, end)
        # When we search on the right, the result may be too big, so we fall
        # back to our previous result
        if res * res > number:
            res = middle

    return res


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if not isinstance(number, int) or number < 0:
        return None

    # 0 or 1
    if number <= 1:
        return number

    return binary_search_square_root(number, 0, number)


#########################################
## Tests
#########################################

import math
import random

# Check result against python native function, casted to integer
for i in [random.randint(0, 1000000000) for i in range(100)]:
    expected = int(math.sqrt(i))
    res_fun = sqrt(i)
    print ("Compute sqrt of", i, "expected", expected, "got", res_fun)
    assert expected == res_fun

# Check first square roots as they may be one that have special handling
for i in range(0, 10):
    expected = int(math.sqrt(i))
    res_fun = sqrt(i)
    print ("Compute sqrt of", i, "expected", expected, "got", res_fun)
    assert expected == res_fun

expected = None
res_fun = sqrt(None)
print ("Compute sqrt of", None, "expected", expected, "got", res_fun)
assert expected == res_fun

expected = None
res_fun = sqrt(-10)
print ("Compute sqrt of", -10, "expected", expected, "got", res_fun)
assert expected == res_fun

expected = None
res_fun = sqrt(3.14)
print ("Compute sqrt of", 3.14, "expected", expected, "got", res_fun)
assert expected == res_fun

print("All test passed")