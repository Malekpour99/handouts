# Binary Search Tree
# inorder traversing of the BST will returns an ordered list of its nodes!


class Node:
    "Nodes are the data elements which trees consist of them"

    def __init__(self, key, left=None, right=None):
        """creating a node with the given data which currently has no connection
        in left or right"""
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.x = []

    def inorder(self, root):
        "Traversing binary tree using inorder method knowing the root node"
        if root:
            self.inorder(root.left)
            # self.x.append(root.key)
            print(root.key, end=" ")
            self.inorder(root.right)
        return

    def search(self, root, key):
        "Searching BST for desired key starting from its root"
        if root is None or root.key == key:
            return root
        if key > root.key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def insert(self, root, key):
        "Inserting a new key in BST"
        if root is None:
            return Node(key)
        if key > root.key:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)
        return root

    def delete(self, root, key):
        "Deleting desired key from BST"
        if root.key == key:
            if root.left and root.right:
                rl = root.left
                while rl.right:
                    rl = rl.right
                temp_val = rl.key
                root = self.delete(root, rl.key)
                root.key = temp_val
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            root.left = self.delete(root.left, key)
        return root

    def min_value_node(self, root):
        "Returns the minimum node value in BST"
        c = root
        while c.left is not None:
            c = c.left
        return c

    def max_value_node(self, root):
        "Returns the maximum node value in BST"
        c = root
        while c.right is not None:
            c = c.right
        return c


#        4
#    2       6
#  1   3   5   7
# r = Node(4)
r = None
bst = BinarySearchTree()
r = bst.insert(r, 4)
r = bst.insert(r, 2)
r = bst.insert(r, 3)
r = bst.insert(r, 6)
r = bst.insert(r, 5)
r = bst.insert(r, 7)
r = bst.insert(r, 1)

# r = Node(4)
# r.left = Node(2)
# r.right = Node(6)
# r.left.left = Node(1)
# r.left.right = Node (3)
# r.right.left = Node(5)
# r.right.right = Node(7)


print(bst.inorder(r))
r = bst.insert(r, 8)
print(bst.inorder(r))
print(bst.min_value_node(r).key)
print(bst.max_value_node(r).key)
try:
    print(bst.search(r, 9).key)
except AttributeError:
    print("This key doesn't exist in BST")

r = bst.delete(r, 4)
print(bst.inorder(r))
