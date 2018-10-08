"""
Binary Search Tree Implementation
Non linear data structure where we have a root and then nodes connected
to each other. If new value is less than node, arrange it on the LHS
recursively else arrange it on RHS.

Tree Traversal:
Preorder
Inorder
Postorder
 
      1
   2      3
4    5  6   7

"""

class Node(object):
    def __init__(self, data):
        """
        """
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        """
        compare value with parent node and decide to add it to left
        or right side
        """
        if self.data:

            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, value):
        """
        """

        if value < self.data:
            if self.left is None:
                return "Not found"
            return self.left.search(value)

        elif value > self.data:
            if self.right is None:
                return "Not found"
            return self.right.search(value)

        else:
            return "Found", self.data

    def show_tree(self):
        if self.left:
            self.left.show_tree()
        print self.data
        if self.right:
            self.right.show_tree()

# obj = Node(1)
# obj.insert(2)
# obj.insert(3)
# obj.insert(4)
# obj.insert(5)
# obj.insert(6)
# obj.insert(7)
# 
# print obj.search(11)

# obj.show_tree()

