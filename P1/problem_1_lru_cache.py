class LRU_Cache(object):
    max_capacity = None
    cache = [] # Cache data
    cache_history = [] # Keep insertion order

    def __init__(self, capacity):
        # Initialize class variables
        self.max_capacity = capacity
        # Initialize the cache with -1 so we can avoid doing index check in get
        for i in range(0, capacity):
            self.cache.append(-1)

    def get(self, key):
        # todo - update as most recently used

        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            return self.cache[key]
        except:
            return -1

    def set(self, key, value):
        key = key - 1

        # Trying to write outside the cache area
        if (key >= len(self.cache) or key < 0):
            return -1

        # Cache is full, remove the oldest element
        if (len(self.cache_history) >= 5):
            self.__remove_oldest_cache_element()

        self.__update_cache_entry(key, value)

    def __update_cache_entry(self, key, value):
        self.cache[key] = value
        self.cache_history.append(key)

    def __remove_oldest_cache_element(self):
        try:
            self.cache[self.cache_history[0]] = -1
            self.cache_history.pop(0)
        except:
            # No history so far, so there is nothing to remove
            return

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
print(our_cache.cache, our_cache.cache_history)
our_cache.set(2, 2)
print(our_cache.cache, our_cache.cache_history)
our_cache.set(3, 3)
print(our_cache.cache, our_cache.cache_history)
our_cache.set(4, 4)
print(our_cache.cache, our_cache.cache_history)
our_cache.set(5, 5)
print(our_cache.cache, our_cache.cache_history)

our_cache.set(1, 6)
print(our_cache.cache, our_cache.cache_history)
our_cache.set(2, 7)
print(our_cache.cache, our_cache.cache_history)
our_cache.set(3, 8)
print(our_cache.cache, our_cache.cache_history)
our_cache.set(4, 9)
print(our_cache.cache, our_cache.cache_history)
our_cache.set(5, 10)
print(our_cache.cache, our_cache.cache_history)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.cache)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
