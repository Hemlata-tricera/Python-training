# f = open("myfile.txt")
# print(f.read())
# f.close()

# f = open("myfile.txt", 'a')
# data = f.write("This is new added line 4")
# print(data)
# f.close()

# It will append string, It can be perform on existing or non existing file(It will create new file).
f = open("myfile123.txt", 'a+')
data = f.write("This is a+ mode2")
# print(data)
f.close()


# # Perform on existing file only
# f =open("myfile.txt", 'r+')
# f.write("This is r+ mode 2")
# f.close()

# It will overide content, It can be perform on existing or non existing file(It will create new file).
# f =open("myfile.txt", 'w+')
# f.write("This is w+ mode")
# f.close()