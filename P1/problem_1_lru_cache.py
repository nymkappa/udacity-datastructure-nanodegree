#########################################################################################
#
# For our first problem, the goal will be to design a data structure known
# as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in
# which we remove the least recently used entry when the cache memory reaches
# its limit. For the current problem, consider both get and set operations
# as an use operation.
#
# Your job is to use an appropriate data structure(s) to implement the cache.
#
#    * In case of a cache hit, your get() operation should return the appropriate value.
#    * In case of a cache miss, your get() should return -1.
#    * While putting an element in the cache, your put() / set() operation must
#      insert the element. If the cache is full, you must write code that removes
#      the least recently used entry first and then insert the element.
#
# All operations must take O(1) time.
#
#########################################################################################

import sys

class LRU_Cache(object):
    max_capacity = None
    cache = []  # Cache data
    cache_history = []  # Keep insertion order

    def __init__(self, capacity):
        # Initialize class variables
        self.max_capacity = capacity
        # Initialize the cache with -1 so we can avoid doing index check in get
        for i in range(0, capacity):
            self.cache.append(-1)

    def get(self, key):
        key = key - 1

        # Trying to read outside the cache area
        if key >= len(self.cache) or key < 0:
            return -1

        # If the item is already the most recently accessed/updated cache item
        # then we don't have anything to do
        if self.cache_history[len(self.cache_history) - 1] != key:
            self.__add_cache_entry(key, self.cache[key])

        return self.cache[key]

    def set(self, key, value):
        key = key - 1

        # Trying to write outside the cache area
        if key >= len(self.cache) or key < 0:
            return -1

        self.__add_cache_entry(key, value)

    def __add_cache_entry(self, key, value):
        # Cache is full, remove the oldest element
        if len(self.cache_history) >= 5:
            self.cache[self.cache_history[0]] = -1
            self.cache_history.pop(0)

        self.cache[key] = value
        self.cache_history.append(key)


###############################################################################
# Tests
###############################################################################

enable_output = True
cache_size = 5
our_cache = LRU_Cache(cache_size)
cache = our_cache.cache
cache_history = our_cache.cache_history
if enable_output: print cache, cache_history

# Check if cache is properly initialized
assert len(cache) == cache_size
assert cache[0] == -1
assert cache[cache_size - 1] == -1
if enable_output: print cache, cache_history

# Check if cache set works properly
our_cache.set(1, 1)
assert cache[0] == 1
assert len(cache_history) == 1
assert cache_history[len(cache_history) - 1] == 0
if enable_output: print cache, cache_history

our_cache.set(2, 2)
assert cache[1] == 2
assert len(cache_history) == 2
assert cache_history[len(cache_history) - 1] == 1
if enable_output: print cache, cache_history

our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
assert cache[4] == 5
assert len(cache_history) == 5
assert cache_history[len(cache_history) - 1] == 4
if enable_output: print cache, cache_history

# Check that we can't write outside the cache
our_cache.set(-1, -1)
our_cache.set(6, 6)
assert cache[4] == 5
assert len(cache_history) == 5
assert cache_history[len(cache_history) - 1] == 4
if enable_output: print cache, cache_history

# Check that cache history is properly updated
our_cache.set(4, 6)
assert len(cache_history) == 5
assert cache_history[len(cache_history) - 1] == 3
if enable_output: print cache, cache_history

our_cache.set(5, 10)
assert len(cache_history) == 5
assert cache_history[len(cache_history) - 1] == 4
if enable_output: print cache, cache_history

our_cache.set(3, 7)
assert len(cache_history) == 5
assert cache_history[len(cache_history) - 1] == 2
if enable_output: print cache, cache_history

our_cache.set(1, 9)
assert len(cache_history) == 5
assert cache_history[len(cache_history) - 1] == 0
if enable_output: print cache, cache_history

our_cache.set(2, 8)
assert len(cache_history) == 5
assert cache_history[len(cache_history) - 1] == 1
if enable_output: print cache, cache_history

# Check if get works properly
assert our_cache.get(1) == 9
assert our_cache.get(2) == 8
assert our_cache.get(5) == -1 # Was too old
assert our_cache.get(9) == -1
assert our_cache.get(-2) == -1
if enable_output: print cache, cache_history

for i in range(0, cache_size):
    our_cache.get(1)
assert cache_history[0] == 1
if enable_output: print cache, cache_history

print("All tests passed")
