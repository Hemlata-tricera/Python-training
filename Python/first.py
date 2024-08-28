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

# Append Items
thislist.append('pear')  # To add an item to the end of the list, use the append() method
print(thislist)
# Extend List
fruitlist = ['watermelon', 'raspberry']
print(fruitlist)
thislist.extend(fruitlist)  # To append elements from another list to the current list, use the extend() method.
print(thislist)
thistuple = ("avacado", "cherry")
thislist.extend(thistuple)  # The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
print(thislist)
thislist.remove("avacado")  # The remove() method removes the specified item.
print(thislist)
thislist.pop(2)  # The pop() method removes the specified index.
print(thislist)
thislist.pop()  # If you do not specify the index, the pop() method removes the last item.
print(thislist)
del thislist[0]  # The del keyword also removes the specified index.
print(thislist)
# del fruitlist # The del keyword can also delete the list completely.
print(fruitlist)
fruitlist.clear()
print(fruitlist)
# Loop Through a List
for x in thislist:
    print(x)
for i in range(len(thislist)):
    print(thislist[i])
# Looping Using List Comprehension
[print(x) for x in thislist]
# List Comprehension


#-------------------------------------------------------------------------------------------------------------------------
# OPERATORS
# Arithmetic Operators
x = 5
y = 3
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y)  # Exponentiation
print(x // y)  # Floor division
# Assignment Operators
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x //= 3
print(x)
x **= 3
print(x)
x = 5
x &= 3
print(x)





# Comparision Operators
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
# Logical Operators
x = 5
print("Logical Operator")
print(x > 3 and x < 10)
print(x < 5 or x < 4)
print(not(x < 5 or x < 4))

# Identity Operators
print("Identity Operators")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)  # returns False because x is not the same object as y, even if they have the same content
print(x == y)

# Membership Operators
print("Membership Operators")
x = ["apple", "banana"]
print("banana" in x)
print("apple" in x)
print("pineapple" not in x)



















