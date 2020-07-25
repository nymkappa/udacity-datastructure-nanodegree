# Data structure

For this problem, I used three main data structures:

* A temporary array which holds the priority queue
* A binary tree (Huffman Tree)
* A dictionary which is used as encoding table. I choose to generate this dictionary because it makes the final encoding part faster that going through the Huffman Tree for each character

Note: The priority queue and the binary tree both shares a common structure, which is defined by the "Node" class.

# Complexity

## Encoding

1. We first generate our priority queue with a worst complexity of O(nlogn):

 * O(n) for iterating through the data once (generating a count map of character occurrences)
 * O(nlogn) for sorting the map (we need it because we will run a binary search later)
 * O(n) to generate convert map to our priority 
(using the Node class)

2. We then generate the Huffman tree with a complexity of O(n) as we iterate through the priority queue only once (we pop 2 nodes, and insert 1, so same time as going through all nodes once). For inserting the internal nodes at the correct position, we run a binary search in the priority queue, which has a complexity of O(logn). Therefore our complexity to generate the Huffman tree is O(nlogn).

3. Then we generate the encoding table with O(n), as we simply traverse our binary tree to generate it.

4. We encode our string with O(n), thanks to the encoding table generated in step 3. Otherwise we would have to traverse the tree for each character (to find the code), which would takes much more time.

We can see that we have a worst case complexity of O(nlogn) for the encoding part.

## Decoding

For the decoding part, we run a binary search in the tree for each character (the algorithm does the opposite way, but the idea is the same). This operation is O(logn). So to decode the complete data we have a complexity of O(nlogn).

# Notes

The exercise mentioned using a min-heap to keep the priority queue ordered when inserting internal nodes. I believe it's easier to follow the algorithm by using a binary search on the priority queue instead (and requires less code, as we insert directly at the good position, so no need to re-order). Also, the complexity is the same for both solutions.