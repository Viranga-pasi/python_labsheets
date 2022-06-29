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
    if r == 0 or c == 0:
        print("Array size is empty")
    else:
        array = [[0 for x in range(c)]  for y in range(r)]
        for i in range(0,r):
            for j in range(0,c):
                if i == j:
                    array[i][j] = 1
                else:
                    array[i][j] = 0
        print(array)

    
    

# multiply arrays

def mattrix_multiply():
    print("------------Create mattrix 1------------")
    array_1 = generate_mattrix()
    print("------------Create mattrix 2------------")
    array_2 = generate_mattrix()

    if len(array_1) == len(array_2[0]) and len(array_2) == len(array_1[0]):
        ans = [[0 for x in range(0,len(array_1))] for y in range(0,len(array_2[0]))]
        for i in range(len(array_1)):
            for j in range(len(array_2[0])):
                for k in range(len(array_2)):
                    ans[i][j] +=  array_1[i][k] * array_2[j][k]    
        print(ans)
    else:
        print('Mattixies cannot multiply')

# generate mattrix using user inputs
def generate_mattrix():
    r = int(input("Enter number of rows : "))
    c = int(input('Enter number of columns : '))
    
    if r == 0 or c == 0:
        print("Aray size is empty")
    else: 
        array = [[0 for x in range(c)] for y in range(r)]
        for i in range(0,r):
            for j in range(0,c):
                num = int(input("Enter value for {} {} index : ".format(i,j)))
                array[i][j] = num
        return array
        




# array_2d()
# identity_mattrix()
mattrix_multiply()