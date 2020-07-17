# Datastructure

For this problem, I choose to use two arrays. One is the cache data itself, which stored the key/value pair information. The other array is a FIFO queue that holds the access history.

# Complexity

By using two arrays for this problem, we are able to keep a complexity of O(1).
* `get()` function simply access the cache index directly.
* `set()` function also set the value at index directly
* The history handling is also O(1) because it's a FIFO queue, therefore we only use `push` and `pop` operation to keep the cache access history up to date, which both are also O(1)