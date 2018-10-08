"""
prototype design pattern helps to hide the complexity of the instances
created by the class. The newly copied object may have some changes
in the properties if required.
"""

import copy

class Prototype(object):
    pass


def main():
    prototype = Prototype()
    new_obj = copy.deepcopy(prototype)
    print prototype
    print new_obj

main()