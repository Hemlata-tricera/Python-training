# Exception handling

try:
    print(x)
except:
    print("An exception occurred")

# Many Exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Else- You can use the else keyword to define a block of code to be executed if no errors were raised
try:
    print("Hello")
except:
    print("Somthing went wrong")
else:
    print("Nothing went wrong")

# Finally - The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("Somthing went wrong")
finally:
    print("The 'try except' is finished")


# Practice example-
try:
    num = int(input("Enter an Integer"))
except ValueError:
    print("Number entered is not integer")
else:
    print("Integer accepted")
finally:
    print("This block is always executed")

