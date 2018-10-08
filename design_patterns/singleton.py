"""
Singleton allows only one object to be created for a class, it is a creational pattern
"""

class Singleton(object):

    instance = None # this is class object so shared across objects

    def __init__(self):
        if Singleton.instance != None:
            raise Exception("Singleton class, object already exists")
        else:
            Singleton.instance = self

obj1 = Singleton()
print obj1
obj2 = Singleton()
print obj2


    