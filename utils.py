import math as m 


def distance(x, y):
    return m.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def count(L, value):
    count = 0
    for i in L:
        if i == value:
            count += 1
    return count