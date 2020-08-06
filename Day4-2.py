fo = open("google.jpg","rb")
img = fo.read()
fo.close

fo = open("複製.jpg","wb")
fo.write(img)
fo.close()