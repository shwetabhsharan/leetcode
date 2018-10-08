"""
Implement binary search
Complexity : O(log n)
This works only for sorted list. Implements divide and conquer.
Split the array in flat, check if the target is in the first or
the second list, if in first, ignore the second and otherwise.
"""

def binary_search(data, target):
    """
    """
    minimum = 0
    maximum = len(data) - 1
    if minimum > maximum:
        return -1

    while True:
        median = (min+max)/2
        if target < data[median]:
            maximum = median - 1
        elif target > data[median]:
            minimum = median + 1
        else:
            return median

print binary_search([0,1,2,3,4,5,6,7,8,9], 2)