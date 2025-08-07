# Binary Tree
# Traversal Methods ==>
# Preorder: root* / left / right
# Inorder: left / root* / right
# Postorder: left / right / root*


class Node:
    "Nodes are the data elements which trees consist of them"

    def __init__(self, data, left=None, right=None):
        """creating a node with the given data which currently has no connection
        in left or right"""
        self.data = data
        self.left = left
        self.right = right

    def get_left(self):
        "Returns left node"
        return self.left

    def get_right(self):
        "Returns right node"
        return self.right

    def get_data(self):
        "Returns node's data"
        return self.data


class BinaryTree:
    def __init__(self):
        self.x = []

    def inorder(self, root):
        "Traversing binary tree using inorder method knowing the root node"
        if root:
            self.inorder(root.get_left())
            self.x.append(root.get_data())
            self.inorder(root.get_right())
        return self.x

    def inorder_stack(self, root):
        """Traversing binary tree using inorder method knowing the root node +
        stack data structure"""
        c = root
        s = []
        while True:
            if c is not None:
                s.append(c)
                c = c.left
            elif s:
                c = s.pop()
                print(c.data, end=" ")
                c = c.right
            else:
                break

    def peek(stack):
        "Return the top data on the stack"
        if stack:
            return stack[-1]
        return

    def postorder_stack(self, root):
        """Traversing binary tree using postorder method knowing the root node +
        stack data structure"""
        # not tested and evaluated yet
        post = []
        s = []
        while True:
            if root.right is not None:
                s.append(root.right)
            s.append(root)
            root = root.left
            root = s.pop()
            if r.right is not None and self.peek(s) == r.right:
                s.pop()
                s.append(root)
                root = root.right
            else:
                post.append(root.data)
                root = None
            if len(s) <= 0:
                break

    def preorder(self, root):
        "Traversing binary tree using preorder method knowing the root node"
        if root:
            self.x.append(root.get_data())
            self.inorder(root.get_left())
            self.inorder(root.get_right())
        return self.x

    def count_nodes(self, root):
        "Return total number of nodes in the binary tree"
        left_nodes = 0
        right_nodes = 0
        if root.get_left():
            left_nodes = self.count_nodes(root.get_left())
        if root.get_right():
            right_nodes = self.count_nodes(root.get_right())
        return left_nodes + right_nodes + 1

    def count_leaves(self, root):
        """Returns total number of leaves in binary tree (leaf is the final node
        witch has no left or right nodes)"""
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return self.count_leaves(root.left) + self.count_leaves(root.right)


#        1
#    2       3
#  4   5
r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)

bt = BinaryTree()
print(bt.inorder(r))
print(bt.count_nodes(r))
print(bt.count_leaves(r))

#        6
#    7       8
#  9  10  11
root = Node(6, right=Node(8, left=Node(11)), left=Node(7, left=Node(9), right=Node(10)))

bt2 = BinaryTree()
print(bt2.inorder(root))
print(bt2.count_nodes(root))
print(bt2.count_leaves(root))
