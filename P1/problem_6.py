class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    union = set()

    if llist_1 != None:
        head = llist_1.head
        while head != None:
            union.add(head.value)
            head = head.next

    if llist_2 != None:
        head = llist_2.head
        while head != None:
            union.add(head.value)
            head = head.next

    return union


def intersection(llist_1, llist_2):
    if llist_1 == None or llist_2 == None:
        return set()

    dummy_list = None
    set_compare = None
    iterate_list = None

    # Generate a set for the longest list
    if llist_1.size() > llist_2.size():
        set_compare = union(llist_1, None)
        iterate_list = llist_2
    else:
        set_compare = union(llist_2, None)
        iterate_list = llist_1

    intersection = set();

    head = iterate_list.head
    while head != None:
        if head.value in set_compare:
            intersection.add(head.value)
        head = head.next

    return intersection


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("\nTest 1")
print ("Expected:", {3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11, 21})
print ("  Result:", union(linked_list_1,linked_list_2))
print ("Expected:", {4, 6, 21})
print ("  Result:", intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("\nTest 2")
print ("Expected:", {3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21})
print ("  Result:", union(linked_list_3,linked_list_4))
print ("Expected:", {})
print ("  Result:", intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1,1]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("\nTest 3")
print ("Expected:", {1})
print ("  Result:", union(linked_list_3,linked_list_4))
print ("Expected:", {})
print ("  Result:", intersection(linked_list_3,linked_list_4))

# Test case 4

linked_list_5 = LinkedList()

element_1 = [1,1]

for i in element_1:
    linked_list_5.append(i)

print ("\nTest 4")
print ("Expected:", {1})
print ("  Result:", union(None,linked_list_5))
print ("Expected:", {})
print ("  Result:", intersection(linked_list_5,None))