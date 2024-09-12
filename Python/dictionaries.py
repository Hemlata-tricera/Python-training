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

