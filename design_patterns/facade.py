"""
Facade provides interface to set of different interfaces
"""

class A(object):
    def __init__(self):
        print "A"

class B(object):
    def __init__(self):
        print "B"

class Operation(object):
    def __init__(self):
        pass

    def operation(self):
        A()
        B()

class Facade(object):
    def __init__(self):
        obj = Operation()
        obj.operation()

obj = Facade()