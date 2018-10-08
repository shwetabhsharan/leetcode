def sum_of_squares(target):
    for i in range(0, target):
        x = i*i
        y = (i+1)*(i+1)
        print x, y
        if x + y == target:
            return True
sum_of_squares(4)