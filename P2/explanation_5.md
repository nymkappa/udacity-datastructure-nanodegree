# Data structure

For this problem we used a Trie datastructure. Each node can possiblity contains an unlimited number of child nodes. In this exercice, the maximum number of child nodes would depend on our how many possible characters can be contains in words.

# Complexity

## Trie creation

We will call our number of words "n" and the maximum length of a word "m". For each letter of each word, we have to create a node (considering each words have a complete different sequence of letter). Therefore our space and time complexity is O(nm).

## Searching

Finding the starting node which matches the prefix has a time complexity of O(p) with "p" being the length of the prefix, by using a map to store child nodes.

Looking for all the prefix of the starting node is similar to generating the Trie. We have to go through all sub Trie to generate the prefix list. Therefore the time complexity would be O(nm). Additionaly, the space compexity required to store all prefixes would also be in the worst case O(nm) if all prefixes have a different sequence of character.