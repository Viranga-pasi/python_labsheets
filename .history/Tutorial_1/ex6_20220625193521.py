marks = []


def sortList(list):
   
    for i in range(len(list)):
        for j in range(i, len(list)):
           print(i)  
                                                                           
    return list


def getMarks(marks):
    i = 1
    file = open('marks_file.txt', 'r')
    while i <= 10:
        marks.append(int(file.readline()[:2]))
        i += 1
    file.close()
    print(marks)
    sorted_list = sortList(marks)
    print(sorted_list)    

getMarks(marks)
