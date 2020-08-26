import sys

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints) == 0:
        return None

    min_value = sys.maxsize
    max_value = -sys.maxsize - 1

    for val in ints:
    	if val < min_value:
    		min_value = val
    	if val > max_value:
    		max_value = val

    return min_value, max_value


#########################################
## Tests
#########################################

import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("get_min_max(0 => 10), Expected", (0, 9))
assert (0, 9) == get_min_max(l)

l = [i for i in range(-10, 10)]  # a list containing -10 - 9
random.shuffle(l)
print("get_min_max(-10 => 10), Expected", (-10, 9))
assert (-10, 9) == get_min_max(l)

l = [i for i in range(-123456789, -123456788)]  # a list containing -123456789
random.shuffle(l)
print("get_min_max(-123456789 => -123456788), Expected", (-123456789,-123456789))
assert (-123456789,-123456789) == get_min_max(l)

l = [i for i in range(0, 1)]  # a list containing 0
random.shuffle(l)
print("get_min_max(0 => 1), Expected", (0, 0))
assert (0, 0) == get_min_max(l)

print("get_min_max([]), Expected", "None")
assert None == get_min_max([])

print("get_min_max(None), Expected", "None")
assert None == get_min_max(None)

print("All tests passed")