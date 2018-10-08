# simple sort O(n^2)
def sort_data(items):
    """
    """
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    print items
    
sort_data([5,4,1,7,9,8])