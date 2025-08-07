# Linked List (Doubly)
class Node:
    "Nodes are the data elements which linked lists consist of them"

    def __init__(self, data):
        "creating a node with the given data which currently points to nowhere"
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Linked list is a data structure which consists of nodes where in
    each node there's a data, next and prev; data is the value stored in the
    node, next points to the next node after current node and prev points to
    the previous node before current node"""

    def __init__(self):
        "starting our linked list and considering a head for the starting point"
        self.head = None

    def display(self):
        "Displaying all of the nodes' values in our linked list"
        t = self.head
        while t != None:
            print(t.data, end=" <-> ")
            t = t.next
        print("Null")

    def in_start(self, new_data):
        """Adding a node to the starting point of our linked list and
        adjusting the head position"""
        n = Node(new_data)
        n.next = self.head
        if self.head is not None:
            self.head.prev = n
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
        n.prev = t

    def in_after(self, node, new_data):
        """Adding a node after a specified node in our linked list"""
        n = Node(new_data)
        if node is None:
            print("This node doesn't exist in your linked list")
            return
        n.prev = node
        n.next = node.next
        node.next = n
        if n.next is not None:
            n.next.prev = n

    def in_before(self, node, new_data):
        """Adding a node before a specified node in our linked list"""
        n = Node(new_data)
        if node is None:
            print("This node doesn't exist in your linked list")
            return
        n.next = node
        n.prev = node.prev
        node.prev = n
        if n.prev is None:
            self.head = n
        else:
            n.prev.next = n

    def remove_node(self, d):
        """Removing the desired node from the linked list"""
        t = self.head
        if t is not None:
            if t.data == d:
                t.next.prev = None
                self.head = t.next
                t.next = None
                return
            else:
                while t.next is not None:
                    if t.data == d:
                        break
                    t = t.next
                if t.next:
                    t.prev.next = t.next
                    t.next.prev = t.prev
                    t.next = None
                    t.prev = None
                else:
                    t.prev.next = None
                    t.prev = None
                    return
        if t is None:
            return


x = Node(3)
y = Node(4)
z = Node(5)
l = DoublyLinkedList()
l.head = x
x.next = y
y.next = z
y.prev = x
z.prev = y

l.in_start(2)
l.in_end(7)
l.in_after(z, 6)
l.in_after(l.head.next.next, 4.5)
l.display()
# 2 <-> 3 <-> 4 <-> 4.5 <-> 5 <-> 6 <-> 7 <-> Null
l.remove_node(4.5)
l.display()
# 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> Null
