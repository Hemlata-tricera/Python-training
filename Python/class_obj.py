# Create a Class - To create a class, use the keyword class
class My_Class:
    x = 5


p1 = My_Class()
print(p1.x)


class Person:
    def __init__(self, name, age):      # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
        self.name = name
        self.age = age

    def __str__(self):                                    # Str function
        return f"{self.name}({self.age})"


p2 = Person("Amish", 45)

print(p2.name)
print(p2.age)
print(p2)

# The self Parameter
class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def myfun(abc):
        print("Hello my name is " + abc.name)


p1 = Person("avinash", 35)
p1.myfun()


# Modify Object Properties
p1.age = 40
print(p1.age)

# Delete Object Properties - You can delete properties on objects by using the del keyword
del p1.age
print(p1.age)

