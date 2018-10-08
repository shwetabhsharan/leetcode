class Parent(object):
    def __init__(self, message):
        self.message = message
    def show(self):
        print self.message

class Child(Parent):
    def __init__(self, message):
        Parent.__init__(self, message)

obj = Child("This is a test message")
obj.show()