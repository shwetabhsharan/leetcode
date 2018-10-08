"""
add
show
search
depth first search
breadth first search
preorder traversal
inorder traversal
postorder traversal
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
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

    def search(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.search(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.search(data, self)
        else:
            return self, parent

    def show(self):
        if self.left:
            self.left.show()
        print self.data
        if self.right:
            self.right.show()

    def get_children(self):
        count = 0
        if self.left:
            count = count + 1
        if self.right:
            count = count + 1
        return count

    def delete(self, data):
        node, parent = self.search(data)
        children_count = node.get_children()
        if children_count == 0:
            # case where no children are present
            if parent:
                if parent.left:
                    parent.left = None
                if parent.right:
                    parent.right = None
                del node
            else:
                self.data = None

        elif children_count == 1:
            # when only either left or right child is present
            if self.left:
                node = self.left
            elif self.right:
                node = self.right
            if parent:
                if parent.left:
                    parent.left = node
                if parent.right:
                    parent.right = node
                del node
            else:
                # root case where root has just one child
                self.left = node.left
                self.right = node.right
                self.data = node.data
                
        elif children_count == 2:
            pass
        else:
            print "Not supported"
    
root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

root.show()

node, parent = root.search(3)
root.delete(14)
root.show()


