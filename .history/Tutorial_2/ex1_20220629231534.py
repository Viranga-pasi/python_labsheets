import random

# create 2D array
def array_2d():
    array = [[0 for x in range(5)] for y in range(5)] 

    for i in range(0,5):
        for j in range(0,5):
            num = int(random.random() * 10)
            array[i][j] = num

    print(array)


# create indentuty mattrix
def identity_mattrix():
    c = int(input("Enter number of column : "))
    r = int(input("Enter number of rows : "))
    array = [[0 for x in range(c)]  for y in range(r)]
    for i in range(0,r):
        for j in range(0,c):
            if i == j:
                array[i][j] = 1
            else:
                array[i][j] = 0

    
    print(array)

# multiply arrays
def array_multiply():
    c = int(input("Enter number of columns : "))
    r = int(input('Enter number of rows : '))




# array_2d()
# identity_mattrix()
array_multiply()