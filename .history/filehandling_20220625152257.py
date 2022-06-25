# with open(filenme, mode) as file: -> another way to open a file
# • modes:
#   • “r” - Read mode which is used when the file is only being read
#   • “w” - Write mode which is used to edit and write new information to
#           the file(any existing files with the same name will be erased
#           when this mode is activated)
#   • “a” - Appending mode, which is used to add new data to the end of
#           the file that is new information is automatically amended to the end
#   • “r +” - Special read and write mode, which is used to handle both
#           actions when working with a file
#   • “b” - Open in binary mode

file = open('sample_file.txt', 'r')  # only open the file

# read the contetn and store it, can have a parameter to limit characters
content = file.read()
lllo = file.readline()

# print(content)
print(lllo)
file.close()
