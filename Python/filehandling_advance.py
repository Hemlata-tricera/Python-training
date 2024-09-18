f = open("myfile.txt")
print(f.read())
f.close()

# f = open("myfile.txt", 'a')
# data = f.write("This is new added line 4")
# print(data)
# f.close()

# f = open("myfile.txt", 'a+')
# data = f.write("This is new added line 5")
# # print(data)
# f.close()



f =open("myfile.txt", 'r+')
f.write("This is r+ mode")
f.close()
