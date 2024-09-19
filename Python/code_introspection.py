# Code Introspection function
# 1.type()- return the type of an object
x = 30
print(type(x))  # o/p- <class 'int'>

y = "Hello"
print(type(y))   # o/p- <class 'str'>

# 2.dir(): Returns a list of the attributes and methods of an object.
class Myclass:
    def method(self):
        pass

obj = Myclass()
print(dir(obj))
# o/p - ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne
# __', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'method']

# 3. id(): Returns the unique identifier of an object.
a = [1, 2, 3]
b = a
print(id(a))  # 2531257692416(ID of the list object)
print(id(b))  # 2531257692416(Same ID as a, since b references the same object)

# 4. getattr(): Retrieves an attribute of an object by name.
class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

s = Student("Suraj", "Desai")
print(getattr(s, 'fname')) # Suraj
print(getattr(s, 'lname')) # Desai
print(getattr(s, 'age', 'age not set')) #  Age not set (default value)

# 5. setattr(): Sets an attribute of an object by name.
setattr(s, 'age', 24)
print(s.age) # 24

# 6. The hasattr() function checks if the object has an attribute.
print("Hasattr()",hasattr(s, 'fname'))
print("Hasattr()",hasattr(s, 'name'))


# 7. callable(): Checks if an object appears to be callable (like functions or classes).
def func():
    return "I am a function"

print(callable(func))  # True
print(callable(s))  # False

# 8. isinstance(): Checks if an object is an instance of a particular class or a tuple of classes.
print(isinstance(s, Student))  # True
print(isinstance(s, str))  # False


# # Inspect Module
# import inspect
#
# def sample_function(a, b):
#     """This is a sample function."""
#     return a + b
#
# print(inspect.getdoc(sample_function))  # This is a sample function.
# print(inspect.signature(sample_function))  # (a, b)
# print(inspect.getmembers(sample_function))  # Lists all members of the function
