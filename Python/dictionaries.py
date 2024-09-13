# Python Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Dictionary Items
print(thisdict["brand"])

# Dictionary Length
print(len(thisdict))

# Dictionary Items - Data Types
print(type(thisdict))

# The dict() Constructor
thisdic = dict(name = "John", age = 36, country = "Norway")
print(thisdic)

# Accessing Items
x = thisdict["model"]
print(x)

# OR

x = thisdict.get("model")
print(x)

#Get Keys

x = thisdict.keys()
print(x)

# Get Values
x = thisdict.values()
print(x)

# Update Dictionary
thisdict.update({"year": 2020})
print(thisdict)

# Adding Items
thisdict["color"] = "red"
print(thisdict)

# Removing Items
thisdict.pop("model")  # The pop() method removes the item with the specified key name
print(thisdict)

thisdict.popitem()  # The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
print(thisdict)

# The del keyword removes the item with the specified key name
del thisdict["year"]
print(thisdict)

# The clear() method empties the dictionary
thisdict.clear()
print(thisdict)


# Loop Through a Dictionary
dict1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in dict1:
    print(x)

# Print all values in the dictionary, one by one
for x in dict1:
    print(dict1[x])

# You can also use the values() method to return values of a dictionary
for x in dict1.values():
    print(x)

# You can use the keys() method to return the keys of a dictionary
for x in dict1.keys():
    print(x)

# Loop through both keys and values, by using the items() method
for x, y in dict1.items():
    print(x, y)

# Copy a Dictionary

dictA = {"name": "Asma", "age": 34}

dictB = dictA.copy()
print(dictB)

# Another way to make a copy is to use the built-in function dict().
dictC = dict(dictB)
print(dictC)

# Python - Nested Dictionaries
myfamily = {
    "Child1": {
        "name": "Amar",
        "age": 18
    },
    "Child2": {
        "name": "Akbar",
        "age": 20
    },
    "Child3": {
        "name": "Anthony",
        "age": 22
    }
}

print(myfamily)

dictD= {
    "Dict1": dictA,
    "Dict2": dictB,
    "Dict3": dictC
}
print(dictD)

# Access Items in Nested Dictionaries
print(myfamily["Child2"]["name"])

# Loop Through Nested Dictionaries
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])


# Dictionary Method
# 1. clear()- Removes all items from the dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()
print(car)

# 2. dict.copy()-Returns a shallow copy of the dictionary.

my_dict = {'a': 1, 'b': 2}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'a': 1, 'b': 2}

# 3. dict.fromkeys(iterable, value=None)- Creates a new dictionary with keys from iterable and values set to value.
keys = [ 'a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)

# 4. dict.get(key, default=None) - Returns the value for key if key is in the dictionary; otherwise, returns default.

x = new_dict.get("b")

print(x)
y = new_dict.get("d")  # default value is none
print(y)

# 5. items()- Returns a view object that displays a list of a dictionary's key-value tuple pairs.
my_dict = { "a": "apple", "b":"ball"}
print(my_dict.items())  # o/p- dict_items([('a', 'apple'), ('b', 'ball')])

# 6. keys()-Returns a view object that displays a list of all the keys in the dictionary.
my_dict = { "a": "apple", "b":"ball", "c": "camel"}
print(my_dict.keys())


# 7. pop(key, default) - Removes the specified key and returns its value. If the key is not found, returns the default value if provided.
my_dict = { "a": "apple", "b":"ball", "c": "camel"}
print(my_dict.pop('a'))       # Output: 1
print(my_dict.pop('d', 'not found'))  # Output: not found
print(my_dict)

# 8. popitem() -Removes and returns a (key, value) pair from the dictionary. Pairs are returned in LIFO (last-in, first-out) order
my_dict = {'a': 1, 'b': 2}
item = my_dict.popitem()
print(item)  # Output: ('b', 2)
print(my_dict)  # Output: {'a': 1}

# 9. setdefault(key, default)-Returns the value of a key if it is in the dictionary. If not, inserts the key with a default value and returns that value.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)  # o/p- white
print(car) # o/p- {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'white'}

# 10. update(other) - Updates the dictionary with the key/value pairs from another dictionary or iterable of key/value pairs.
my_dict = {'a': 1}
my_dict.update({'b': 2, 'c': 3})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 11. values()- Returns a view object that displays a list of all the values in the dictionary.
my_dict = {'a': 1, 'b': 2}
print(my_dict.values())  # Output: dict_values([1, 2])
