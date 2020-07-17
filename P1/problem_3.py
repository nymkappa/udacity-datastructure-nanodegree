import sys

debug = False


###########################################################
# Debug utils
###########################################################

def print_nodes(tree):
    print ("Tree nodes:")
    for node in tree:
        print(
            node.letter + str(node.occurrences),
            node.left_child.letter if node.left_child else "",
            node.right_child.letter if node.right_child else ""
        )
    print()


def print_tree(root):
    print(root.letter + str(root.occurrences))
    if root.left_child is not None:
        print_tree(root.left_child)
    if root.right_child is not None:
        print_tree(root.right_child)


###########################################################
# Huffman binary tree Node
###########################################################

class Node:
    left_child = None
    right_child = None
    occurrences = 0
    letter = ""


###########################################################
# Count occurrences of each letter and order from the least
# present to the most present and return a list of nodes
###########################################################

def build_priority_queue(data):
    occurrences_map = {}

    for val in data:
        if val not in occurrences_map:
            occurrences_map[val] = 0
        occurrences_map[val] += 1

    occurrences = sorted(occurrences_map.items(), key=lambda x: x[1])

    nodes = []
    for occurrence in occurrences:
        n = Node()
        n.occurrences = occurrence[1]
        n.letter = occurrence[0]
        nodes.append(n)

    return nodes


###########################################################
# Generate the binary tree from the priority queue
###########################################################

def generate_tree(nodes):
    while len(nodes) > 1:
        # Create parent node
        parent = Node()
        parent.occurrences = nodes[0].occurrences + nodes[1].occurrences
        parent.left_child = nodes[0]
        parent.right_child = nodes[1]

        # Remove the two childs from the priority queue
        nodes.pop(0)
        nodes.pop(0)

        # Insert the new node at the correct spot
        insert_index = 0
        for node in nodes:
            if node.occurrences > parent.occurrences:
                break
            insert_index += 1
        nodes.insert(insert_index, parent)
        if debug is True:
            print_nodes(nodes)

    return nodes[0]


###########################################################
# Generate the encoding code table from the binary tree
###########################################################

def generate_code_table(root, code_table, current_code):
    if root.left_child is None and root.right_child is None:
        code_table[root.letter] = current_code
        return

    if root.left_child is not None:
        current_code += "0"
        generate_code_table(root.left_child, code_table, current_code)
        current_code = current_code[:-1]

    if root.right_child is not None:
        current_code += "1"
        generate_code_table(root.right_child, code_table, current_code)
        current_code = current_code[:-1]


###########################################################
# Encode/compress data
###########################################################

def huffman_encoding(data):
    if (len(data) < 1):
        raise Exception("data cannot be empty")

    # Count occurences of each character and create initial nodes
    nodes = build_priority_queue(data)
    if debug is True:
        print_nodes(nodes)

    if (len(nodes) < 2):
        raise Exception("there must be at least two different character "
                        "in the string")

    # Create Huffman tree for initial nodes
    tree_root = generate_tree(nodes)
    if debug is True:
        print("Tree:")
        print_tree(tree_root)

    # Generate encoding table
    code_table = {}
    generate_code_table(tree_root, code_table, "")
    if debug is True:
        print(code_table)

    # Encode the string
    encoded = ""
    for char in data:
        encoded += code_table[char]
    if debug is True:
        print(encoded)

    return encoded, tree_root


###########################################################
# Generate the encoding code table from the binary tree
###########################################################

def decode_char(root, encoded_data):
    if root.left_child is None and root.right_child is None:
        return root.letter, encoded_data

    if encoded_data[0] == "0":
        return decode_char(root.left_child, encoded_data[1:])
    elif encoded_data[0] == "1":
        return decode_char(root.right_child, encoded_data[1:])


###########################################################
# Decode/decompress data
###########################################################

def huffman_decoding(data, tree):
    decoded_data = ""

    while len(data) > 0:
        character, data = decode_char(tree, data)
        decoded_data += character

    if debug is True:
        print(decoded_data)

    return decoded_data


###########################################################
# Tests
###########################################################

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    huffman_encoding(a_great_sentence)

    print ("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
