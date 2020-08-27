# Data structure

For this problem we used a Trie datastructure. Each node can possiblity contains an unlimited number of child nodes, as each routes can contains as many sub-routes as the user wish.

# Complexity

## Trie creation

We can consider a full route path to be a word, and a route part to be a character. With "n" being the number of routes, and "m" the number of part for a route, this gives us a time and space complexity of O(nm).

## Searching

Finding the node which matches the route parts has a time complexity of O(p) with "p" being the number of parts in the route, by using a map to store child nodes.

## Note

Performances could be improved by using a map to store children like in problem 5. However in a web application context, there is usually not thousands of different routes paths, and if there is, they usually share the same structure, making the number of "re-used" nodes very high, so performances should be fine.