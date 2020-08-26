class TrieNode:
    def __init__(self, char, end_of_word):
        """
        Initialize this node in the Trie
        """
        self.char = char
        self.children = []
        self.end_of_word = end_of_word

    def insert(self, char, end_of_word):
        """
        Add a child node in this Trie
        """
        new_child = TrieNode(char, end_of_word)
        self.children.append(new_child)
        return new_child


    def suffixes(self, suffix, words):
        """
        Recursive function that collects the suffix for
        all complete words below this point
        """
        if self.end_of_word is True and len(suffix) > 0:
            words.append(suffix)
        
        if len(self.children) == 0:
            return

        for child in self.children:
            suffix_tmp = suffix + child.char
            child.suffixes(suffix_tmp, words)

        return words


    def find_child(self, char):
        """
        Look for a child with char, and return the node
        """
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
        self.root = TrieNode(None, False)


    def insert(self, word):
        """
        Add a word to the Trie
        """
        current_node = self.root

        idx = 0
        while idx < len(word):
            match_idx = current_node.find_child(word[idx])
            if match_idx is None:
                current_node = current_node.insert(word[idx], idx == len(word) - 1)
            else:
                current_node = current_node.children[match_idx]
            idx += 1


    def find(self, prefix):
        """
        Find the Trie node that represents this prefix
        """
        if prefix is None or len(prefix) == 0:
            return None

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
for word in wordList:
    MyTrie.insert(word)

def test(autocomplete_val, expected):
    output = None
    node = MyTrie.find(autocomplete_val)
    if node is not None:
        output = node.suffixes('', [])
    print("Autocomplete for", autocomplete_val, "Expected", expected, "Got", output)
    assert expected == output

expected = ['nt', 'nthology', 'ntagonist', 'ntonym']
autocomplete_val = "a";
test(autocomplete_val, expected)
test(autocomplete_val, expected)

expected = ['un', 'unction', 'actory']
autocomplete_val = "f";
test(autocomplete_val, expected)

expected = ['ction']
autocomplete_val = "fun";
test(autocomplete_val, expected)

expected = ['e', 'gger', 'gonometry', 'pod']
autocomplete_val = "tri";
test(autocomplete_val, expected)

expected = None
autocomplete_val = "";
test(autocomplete_val, expected)

expected = None
autocomplete_val = None;
test(autocomplete_val, expected)
