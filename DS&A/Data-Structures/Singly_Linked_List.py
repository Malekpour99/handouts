# Linked List (Singly)
class Node:
    "Nodes are the data elements which linked lists consist of them"

    def __init__(self, data):
        "creating a node with the given data which currently points to nowhere"
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Singly linked list is a data structure which consists of nodes where in
    each node there's a data and next; data is the value stored in the node and
    next points to the next node after current node"""

    def __init__(self):
        "starting our linked list and considering a head for the starting point"
        self.head = None

    def display(self):
        "Displaying all of the nodes' values in our linked list"
        t = self.head
        while t != None:
            print(t.data, end=" -> ")
            t = t.next
        print("Null")

    def in_start(self, new_data):
        """Adding a node to the starting point of our linked list and
        adjusting the head position"""
        n = Node(new_data)
        n.next = self.head
        self.head = n

    def in_end(self, new_data):
        """Adding a node to the end of our linked list and telling the
        previous last node where its next node is"""
        n = Node(new_data)
        if self.head is None:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n

    def in_after(self, node, new_data):
        """Adding a node after a specified node in our linked list"""
        # example: l.in_after(l.head.next.next, 10)
        n = Node(new_data)
        if node is None:
            print("This node doesn't exist in your linked list")
            return
        n.next = node.next
        node.next = n

    def remove_node(self, d):
        """Removing the desired node from the linked list"""
        t = self.head
        if t is not None:
            if t.data == d:
                self.head = t.next
                t = None
                return
        while t is not None:
            if t.data == d:
                break
            p = t
            t = t.next
        if t == None:
            return
        p.next = t.next
        t = None


# x = Node(3)
# y = Node(4)
# z = Node(5)
# l = SinglyLinkedList()
# l.head = x
# x.next = y
# y.next = z

# l.in_start(2)
# l.in_end(7)
# l.in_after(z, 6)
# l.in_after(l.head.next.next, 4.5)
# l.display()
# 2 -> 3 -> 4 -> 4.5 -> 5 -> 6 -> 7 -> Null
# l.remove_node(4.5)
# l.display()
