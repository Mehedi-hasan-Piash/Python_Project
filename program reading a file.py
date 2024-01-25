file = open("student.txt", "r+")
# print(file.readable())
for lines in file :
    print(lines)
# text = file.readlines()[2]
# print(text)
# text = file.read()
# print(text)
# size = len(text)
# print(size)
file.close()