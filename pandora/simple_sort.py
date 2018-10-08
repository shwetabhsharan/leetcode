def simple_sort(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] > data[j+1]:
                data[i], data[j+1] = data[j+1], data[i]
    print data
data = [2,4,3,1]
simple_sort(data)