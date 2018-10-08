"""
Implement classes to demonstrate inheritance
"""

class PrintMessage(object):
    def __init__(self, message):
        self.message = message

    def print_message(self):
        print self.message

class Handler(PrintMessage):
    def __init__(self, message):
        PrintMessage.__init__(self, message)

obj = Handler("Message printed from the base class")
obj.print_message()

