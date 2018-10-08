"""
Binary tree is non linear data structure
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, item):
        if self.value:
            if item < self.value:
                if self.left is None:
                    self.left = Node(item)
                else:
                    self.left.insert(item)
            elif item > self.value:
                if self.right is None:
                    self.right = Node(item)
                else:
                    self.right.insert(item)
        else:
            self.value = item

    def search(self, item):
        if item < self.value:
            if self.left is None:
                return "Not found"
            return self.left.search(item)

        elif item > self.value:
            if self.right is None:
                return "Not found"
            return self.right.search(item)

        else:
            return "Found", self.value

obj = Node(0)
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.insert(6)
obj.insert(7)
print obj.search(4)
