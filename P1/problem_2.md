# Datastructure

For this problem, the only datastructure we use in an array, which holds the file list.

# Complexity

We traverse the directory tree by doing a DFS from the original path send as parameter, which gives a complexity of O(n) with n being the total number of sub directories in the tree.
We loop through all files for each directory we traverse, which also gives us a complexity of O(n), with n being the number of files in the sub directory.

Overall, this algorythm is similiar to having one single folder, with all files at the same level, which we loop through only onces trying to match the requested pattern.
Therefore overall, this algorythm has a complexity of O(n), with n being the number of paths (file + directories) in the tree.