# **********************DAY-14(Python)*******************************************
# ********Variables***********
# Variable declaration, print function and indentation in python
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

# Multi Words Variable Names
# 1. Camel Case
myVariableName = "John"
# 2. Pascal Case
MyVariableName = "John"
# 3. Snake Case
my_variable_name = "John"

# Python Variables - Assign Multiple Values
# 1. Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# 2. One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# 3. Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global Variables
# Variables that are created outside of a function are known as global variables.
# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



