# Data structure

For this problem, we use a simple linked list data structure to hold the chain.

The Block class is a node in our linked list. It contains some data about the block itself and a pointer to the next block. It also contains the hash of the previous block (named as "previous_hash"). So if the previous block data is modified, the new hash will not match the value stored in "previous_hash", therefore the chain will not be valid anymore.

# Complexity

There is not much going on in our implementation. The complexity of adding a new block will depends on the implementation of Python list, as we fetch the last block using "self.blocks[-1]", which according to the documentation would be O(1).

Our "print_chain" function just go through all blocks and print their data. So we have an O(n) complexity.

Our space complexity is also O(n) with n being the number of blocks in our chain.