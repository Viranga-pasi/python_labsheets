import random

def array_2d():
    array = [[0 for x in range(5)] for y in range(5)] 

    for i in range(0,5):
        for j in range(0,5):
            num = int(random.random() * 10)
            array[i][j] = num

    print(array)

def identity_mattrix(r,c):




# array_2d()

