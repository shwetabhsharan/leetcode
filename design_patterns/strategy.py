"""
Strategy pattern is behavioral pattern in which client decides based on
the requirement which algorithm/procedure needs to be executed. Differnt
algorithms can be swapped in and swapped out based on the requirements.
"""

class StrategyPattern(object):
    def __init__(self, func=None):
        if func:
            self.execute = func

    def execute(self):
        print "Original execution"

def execute_replacement1():
    print "Strategy 1"

def execute_replacement2():
    print "Strategy 2"

if __name__ == "__main__":
    obj0 = StrategyPattern()
    obj1 = StrategyPattern(execute_replacement1)
    obj2 = StrategyPattern(execute_replacement2)

    obj0.execute()
    obj1.execute()
    obj2.execute()
