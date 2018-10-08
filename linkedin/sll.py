

class Node(object):
    def __init__(self, data):
        self.data = data

class SLL(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def remove(self, value):
        curr = self.head
        while curr is not None:
            prev = None
            if curr.data == value:
                prev.next = curr.next
                curr.next = None
                break
            else:
                prev = curr
                curr = curr.next

    def length(self):
        curr = self.head
        length = 0
        while curr is not None:
            length = length + 1
            curr = curr.next

#     def reverse(self):
#         prev = None
#         current = self.head
#         while(current is not None):
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         self.head = prev

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def sort_list(self):
        pass

    def get_max(self):
        pass

    def get_min(self):
        pass

    def traverse(self):
        curr = self.head
        while curr is not None:
            print curr.data
            curr = curr.next

obj = SLL()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
obj.traverse()
obj.reverse()
obj.traverse()