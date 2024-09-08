# Create a Class - To create a class, use the keyword class
class My_Class:
    x = 5


p1 = My_Class()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p2 = Person("Amish", 45)

print(p2.name)
print(p2.age)
print(p2)
