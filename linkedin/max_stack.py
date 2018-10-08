class MinStack(object):
    def __init__(self, data):
        self.head = None
        self.value = data

    def push(self, value):
        node = MinStack(value)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head:
            current = self.head
            self.head = current.next
            return current.value

    def top(self):
        return self.head.value

    def get_min(self):
        curr = self.head
        l1 = []
        while curr is not None:
            l1.append(curr.value)
            curr = curr.next
        return min(l1)

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)

print obj.pop()

print obj.top()
print obj.get_min()