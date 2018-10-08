"""
implement binary serach for sorted list, search data in the list
"""

def binary_search(data, value):
    min = 0
    max = len(data)
    while True:
        med = (min + max)/2
        if value < data[med]:
            max = med - 1
        elif value > data[med]:
            min = med + 1
        else:
            return med

data = [8, 10, 15, 19, 25, 30, 31, 38, 52, 53, 55, 57, 60, 61, 64, 68, 69, 75, 78, 79, 84, 87, 89, 91, 98]
print binary_search(data, 99)