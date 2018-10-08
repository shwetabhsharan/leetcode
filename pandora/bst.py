"""
Implement binary search tree
"""

class BST(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BST(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BST(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def search(self, value):
        if value < self.value:
            if self.left is None:
                print "Not found"
            else:
                self.left.search(value)
        elif value > self.value:
            if self.right is None:
                print "Not found"
            else:
                self.right.search(value)
        else:
            print "found"

    def show(self):
        if self.left:
            self.left.show()
        print self.value
        if self.right:
            self.right.show()

obj = BST(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.insert(6)
obj.insert(7)
obj.search(6)
obj.show()