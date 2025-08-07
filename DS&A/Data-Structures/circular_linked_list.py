# Singly Linked List (Circular)
# we also have Doubly Linked List (Circular) where last node(tail)'s next 
# points to the head and head's previous points to the last node (tail)

class Node:
    "Nodes are the data elements which linked lists consist of them"
    def __init__(self, data):
        "creating a node with the given data which currently points to itself"
        self.data = data
        self.next = self

class CircularLinkedList:
    """Linked list is a data structure which consists of nodes where in 
    each node there's a data and next; data is the value stored in the 
    node, next points to the next node after current node and but in circular
    linked list last node also points to the head (starting node)"""
    def __init__(self):
        "starting our linked list and considering a head for the starting point"
        self.head = None
        self.count = 0
        
    def display(self):
        "Displaying all of the nodes' values in our linked list"
        if(self.head == None):
            print("List is Empty!")
            return
        t = self.head
        while True:
            print(t.data, end = ' -> ')
            t = t.next
            if(t == self.head):
                break
    
    def size(self):
        "Returns the size of your list"
        return self.count
    
    def index(self, data):
        "Returns the index of your data node in the list if exists"
        if not self.head:
            print("List is Empty!")
            return
        t = self.head
        for i in range(self.count):
            if t.data == data:
                return i
            t = t.next
        print("This data doesn't exist in your list")
        return None
    
    def insert(self, new_data, i):
        "Inserting a new node at your desired index"
        if(i > self.count) | (i < 0):
            print("Index out of range!")
            return
        if self.head == None:
            self.head = Node(new_data)
            self.count += 1
            return
        t = self.head
        for _ in range(self.count-1 if i-1 == -1 else i-1):
            t = t.next
        a = t.next
        t.next = Node(new_data)
        t.next.next = a
        if(i == 0):
            self.head = t.next
        self.count += 1
        return
    
    def remove(self, i):
        "Removing a node from desired index"
        if(i >= self.count) | (i < 0):
            print("Index out of range!")
            return
        if self.count == 1:
            self.head = None
            self.count = 0
            return
        t = self.head
        for _ in range(self.count-1 if i-1 == -1 else i-1):
            t = t.next
        a = t.next.next
        t.next = a
        if(i == 0):
            self.head = a
        self.count -= 1
        return
        
l = CircularLinkedList()
l.insert(11, 0)
l.insert(12, 1)
l.insert(13, 2)
l.display() # 11 -> 12 -> 13 -> 
print('\n')
l.insert(10, 0)
l.insert(14, 4)
l.insert(20, 2)
l.display() # 10 -> 11 -> 20 -> 12 -> 13 -> 14 -> 
print('\n')
l.remove(2)
l.display() # 10 -> 11 -> 12 -> 13 -> 14 -> 

