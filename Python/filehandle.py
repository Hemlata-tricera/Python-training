# File handling

f = open("demofile.txt", "r")
# print(f.read())
print(f.readline())


# Opening different location file

f = open("D:\Hemlata\computer.txt", "r")
# print(f.read())
# By default the read() method returns the whole text, but you can also specify how many characters you want to return
print(f.read(10))


# By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt", "r")
for x in f:
    print(x)

# Close Files
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()

# Write to an Existing File
f = open("demofile.txt", "a")  # "a" - Append - will append to the end of the file

f.write("Now the file has more content")
f.close()
f = open("demofile.txt", "r")
print(f.read())
f.close()

f = open("demofile.txt", "w")
f.write("oops, I have deleted the content")
f.close()

f = open("demofile.txt", "r")
print(f.read())

# Create a New File
# f = open("myfile.txt", "x")
f = open("mytextfile.txt", "w")
f.write("Text added in empty file using w(wite) ")
f.close()

f = open("mytextfile.txt", "r")
print(f.read())
f.close()

# Delete a File
import os
# os.remove("myfile.txt")

#Check if File exist:
# import os
# if os.path.exists("myfile.txt"):
#     os.remove(("myfile.txt"))
# else:
#     print("The file does not exist")

# Python directory
import os
print("Current Working directory is-",os.getcwd())

# Making new directory
# os.mkdir('test')

print(os.listdir())

# rename a directory
# os.rename('test', 'new_test')


