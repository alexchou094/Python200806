import os.path
if os.path.isfile('file.txt'):
    print("file exist")
else :
    print("file does not exist")

fo = open("file.txt",'w')
fo.write("1 + 1")

fo = open("file.txt",'r')
print(fo.read())

fo = open("file.txt",'a')
fo.write("= 2")

fo.close()