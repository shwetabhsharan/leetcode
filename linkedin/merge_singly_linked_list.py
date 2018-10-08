"""
Merge two singly linked
1->2->4, 1->3->4
1->1->2->3->4->4
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        return self.head

    def traverse(self):
        curr = self.head
        while curr is not None:
            print curr.value
            curr = curr.next

    def merge(self, l1, l2):
        """
        """
        l1_head = l1
        l2_head = l2
        l1_curr = l1_head
        prev = None
        while l1_curr is not None:
            prev = l1_curr
            l1_curr = l1_curr.next
        else:
            prev.next = l2_head
            self.head = l1
        self.sort()

    def sort(self):
        sorted_list = []
        curr = self.head
        while curr is not None:
            sorted_list.append(curr.value)
            curr = curr.next
        self.head = None
        print sorted_list
        sorted_list.sort()
        print sorted_list
        for i in sorted_list:
            self.add(i)
        return self.head

obj = SLL()
obj.add(1)
obj.add(2)
L1 = obj.add(4)
# obj.traverse()


obj = SLL()
obj.add(1)
obj.add(3)
L2 = obj.add(4)
# obj.traverse()


obj.merge(L1, L2)

obj.traverse()
obj.sort()
print "*"*100
obj.traverse()

# print L1, L2