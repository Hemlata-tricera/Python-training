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



# -----------------------------------------------------------------------------------------------------------------------------------------
# DATA TYPES
x = 5
print(type(x)) # Getting the Data Type of x

x = "Hello World"  # str
x = 20  # int
x = 20.5  # float
x = 1j  # complex
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)  # range
x = {"name" : "John", "age" : 36}  # dict
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True  # bool
x = b"Hello"  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview
x = None  # NoneType
print(x)

# -------------------------------------------------------------------------------------------------------------
# Python Numbers
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion
# convert from int to float:
x = float(1)

# convert from float to int:
y = int(2.8)

# convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

# -----------------------------------------------------------------------------------------------------------------------------------
# LIST
list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(list1))

thislist = list(("apple", "banana", "cherry", "papaya", "grapes")) # Creating a new list using list() constructor
print(thislist)

print(thislist[1]) # Access list item
print(thislist[-1])
# Range of Indexes
print(thislist[:2])
print(thislist[2:])
print(thislist[:4])
print(thislist[1:4])
# Range of Negative Indexes
print(thislist[-4:-1])
# Check if Item Exists
if "apple" in thislist:
    print("Yes! apple is in thislist")
# Change Item Value
thislist[0] = "mango"
print(thislist)
# Change a Range of Item Values
thislist[1:3] = ["apple", "strawberry"]
print(thislist)

# Insert Items
thislist.insert(2, "guava")
print(thislist)