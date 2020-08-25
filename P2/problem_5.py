class TrieNode:
    def __init__(self, char):
        """
        Initialize this node in the Trie
        """
        self.char = char
        self.children = []
    

    def insert(self, char):
        """
        Add a child node in this Trie
        """
        new_child = TrieNode(char)
        self.children.append(new_child)
        return new_child


    def suffixes(self, suffix = '', suffixes = []):
        """
        Recursive function that collects the suffix for
        all complete words below this point
        """
        suffix += self.char

        if len(self.children) == 0:
            suffixes.append(suffix)
            return

        for child in self.children:
            child.suffixes(suffix, suffixes)

        return suffixes


    def find_child(self, char):
        idx = 0
        while idx < len(self.children):
            if self.children[idx].char == char:
                return idx
            idx += 1

        return None

        
class Trie:
    def __init__(self):
        """
        Initialize this Trie (add a root node)
        """
        self.root = TrieNode(None)


    def insert(self, word):
        """
        Add a word to the Trie
        """
        current_node = self.root

        for char in word:
            match_idx = current_node.find_child(char)
            if match_idx is None:
                current_node = current_node.insert(char)
            else:
                current_node = current_node.children[match_idx]


    def find(self, prefix):
        """
        Find the Trie node that represents this prefix
        """
        current_node = self.root

        for char in prefix:
            match_idx = current_node.find_child(char)
            if match_idx is None:
                return None
            else:
                current_node = current_node.children[match_idx]

        return current_node


#########################################
## Tests
#########################################

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

# # You can test with 25k words
# with open('words') as my_file:
#     wordList = my_file.read().splitlines()

for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

f("a");