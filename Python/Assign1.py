# Assignment 1
# Define variables
myvar = "Hello"
my_var = "Hello"
_my_var = "Hello"
myVar = "Hello"
MYVAR = "Hello"
myvar2 = "Hello"

'''Illegal variable names:
2myvar = "Hello"
my-var = "Hello"
my var = "Hello"
'''

# LIST MANIPULATION
# 1. List append() Method -  The append() method adds a single element to the end of the list.
L1 = ['cashew', 'almond', 'raisins']
L2 = ['black raisins', 'dates']
L1.append(L2)
print(L1)

# 2. List clear() Method
L3 = [1, 'Two', 3, 4.0]
print(L3)
L3.clear()
print(L3)

# 3. List copy() Method
L4 = ['Yellow', 'Red', 'Pink']
x = L4.copy()
print(x)

# 4. List count() Method
L5 = [1, 2, 5, 6, 7, 2, 0, 2, ["mango", "cherry", "mango"], ("hi", "bye"), "Hello", (2, 8)]
y = L5.count(2)  # Use count function to find the number of times 2
print(y)
y = L5.count(("hi", "bye"))  # Count tuple element ("hi", "bye") inside a list
print(y)
y = L5.count(["mango", "cherry", "mango"])  # Count list element ["mango", "cherry", "mango"] inside a list
print(y)
my_str = 'Maharashtra'
y = my_str.count('a')  # count the number of times a appear in maharashtra
print(y)

# 5. List extend() Method- method adds all the elements of an iterable to the end of the list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
# Add List to the fruits list
fruits.extend(cars)
print(fruits)
# Add a tuple to the fruits list
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
# Add set to the fruits list:
myset = {"mango", "litchi", "papaya"}
fruits.extend(myset)
print(fruits)

# 6.List index() Method
L6 = [3.0, 'Dates', 'almonds', 'raisins', 100, 3.0, ['hello', 'hi']]
x = L6.index(3.0)  # It will find the position of given number parameter
print(x)
x= L6.index('Dates')   # It will find the position of given string parameter
print(x)
x= L6.index(['hello', 'hi'])  # It will find the position of given list parameter
print(x)

# 7.List insert() Method
L7 = ['Jay', 'suresh', 100]
L7.insert(0, 'Ajay')
print(L7)
L7.insert(2, 200)
print(L7)

# 8. List pop() Method
L8 = ['question', 'answer', 'solution']
L8.pop(1)  # The pop() method removes the element at the specified position here the position is 1.
print(L8)
L8.pop()  # default value is -1, which returns the last item(It will delete last position item)
print(L8)


# 9.List remove() Method
L9 = [100, 'apple', 'banana', 'cherry',['hello', 'hi'], 100]
L9.remove(100)  # Remove the number element of the L9 list
print(L9)
L9.remove(['hello', 'hi']) # Remove the list element of the L9 list
print(L9)
L9.remove('cherry') # Remove the string element of the L9 list
print(L9)

# 10.List reverse() Method
# The reverse() method reverses the sorting order of the elements.
L10 = ['apple', 'banana', 'cherry', 'banana']
L10.reverse()
print(L10)

# 11. List sort() Method
# The sort() method sorts the list ascending by default.
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()  # default ascending sorting
print(cars)
cars.sort(reverse=True)  # reverse=True will sort the list descending.
print(cars)

# A function that returns the length of the value


def myfunc(e):
    return len(e)


L11 = ['Ford', 'Mitsubishi', 'BMW', 'VW', "hello"]
L11.sort(key=myfunc) #Pass function as a key parameter
print(L11)
L12 = ['a', 'abc', 'abcd', 'ab']
L12.sort(key=myfunc)
print(L12)








