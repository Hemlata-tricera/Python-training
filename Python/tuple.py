# Python Tuples
mytuple = ("apple", "banana", "cherry")
print(mytuple)

my_tuple = ("apple", "mango", "banana", "guava", "papaya")
print(my_tuple)

# Tuple Length
print(len(my_tuple))

# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple Items - Data Types - Tuple items can be of any data type
tuple1 = ("Almonds", "Cashew", "raisins")
tuple2 = ( 1, 3, 4, 6)
tuple3 = (True, False, True)

print(tuple1)
print(tuple2)
print(tuple3)

# A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male", 4.6)
print(tuple1)

# type()
print(type(my_tuple))
# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Python - Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing
print(thistuple[-1])

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # The search will start at index 2 (included) and end at index 5 (not included).
print(thistuple[:4])  # This example returns the items from the beginning to, but NOT included, "kiwi"
print(thistuple[2:])  # This example returns the items from "cherry" and to the end

print(thistuple[-4:-1])  # This example returns the items from index -4 (included) to index -1 (excluded)

# Check if Item Exists
tuple_1 = ("Hi", "Hello")

if "Hi" in tuple_1:
    print("Yes, 'Hi' is in the tuple_1 tuple")

# Python - Update Tuples
t = ("Hindi", "English", "Marathi")
l = list(t)
print(l)
l[1] = "Sanskrit"
print(l)
t = tuple(l)
print(t)

# Add Items
# 1. Convert into a list
thistuple = ("apple", "banana", "cherry")
x = list(thistuple)
x.append("Orange")
thistuple = tuple(x)
print(thistuple)

# 2. Add tuple to a tuple.
# Create a new tuple with the value "orange", and add that tuple
t = ("Hey", "Hi")
x = ("Hello",)
t += x
print(t)


# Remove Items
y = list(t)
y.remove("Hi")
t = tuple(y)
print(t)

tuple_2 = ("Jaya", "Sushma", "Rekha")
print(tuple_2)
# del(tuple_2)
print(tuple_2)

# Python - Unpack Tuples - When we create a tuple, we normally assign values to it. This is called "packing" a tuple
fruits = ("apple", "banana", "cherry")

(x, y, z) = fruits

print(x)   # o/p - apple
print(y)  # o/p - banana
print(z)  # o/p - cherry

# Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)  # o/p - apple
print(yellow)  # o/p - banana
print(red)  # o/p - ['cherry', 'strawberry', 'raspberry']

# Loop Through a Tuple
tuple_3 = ("a", "b", "c")
for x in tuple_3:
    print(x)

# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


# Using a While Loop
thistuple = ("a", "b", "c")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join Two Tuples
tup1 = ("a", "b", "c")
tup2 = (1, 2, 3)
tup3 = tup1 + tup2
print(tup3)

# Multiply Tuples
mytup = tup2 * 3
print(mytup)

# tuple methods
# 1. Count() - Return the number of times the value 5 appears in the tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 8)
x = thistuple.count(8)
print(x)

# 2. index() - Search for the first occurrence of the value 8, and return its position
thistuple = (1, 8, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

