# Data structure and Complexity

### union

This function has no choice but to go through all nodes one by one for both linked list.
In order to make sure we don't insert duplicated value in the union, we used a set which gives us an insertion time of O(1).

As we have to go through all nodes for both list, the time complexity is O(nListA + nListB).
The worst space complexity would be O(n) is all elements from both list are differents.


### intersection

We first generate a set for the longest list, which allows us to search it in O(1) time. We will iterate the shortest list and seek for the value in our set.

So the overall time complexity will be O(min(nListA, nListB));
The space complexity would be O(max(nListA, nListB) + unionSize(nListA + nListB));
