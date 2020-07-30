# Data structure

For this problem, we used a tree to hold the active directory structure, where each node can be either a group or a user. A group can be the root of a new sub-tree, a user cant.

Each root node can contain multiple groups or users, which which store in a python list.

# Complexity of is_user_in_group

* len is O(1) based on the documentation
* Here the bottleneck could be the "in" operator, to check if a user is part of the node users. As we used python list, it can become slower if we have a node with a lot of users. We could reduce this to O(1) by using a set or hashmap to store users.
* We recursively call is_user_in_group for each sub group of a node

It's a bit difficult to see the time complexity here, as the sub group numbers and user number is always different for each node. As we've mentioned, the bottleneck would most likely be on the "user seeking" part. Therefore in the worst case scenario, we would have to go through all users one by one to find the matching one. So this would give us a worst complexity time of O(n).

Regarding the space complexity, the bottleneck would be the recursive call. If we pass "user" and "sub_group" by reference/pointer, then our space complexity bottleneck would be the storage of groups and users in the list O(userNbr + groupNbr).