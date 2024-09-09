# OOPs Concept
# Inheritance
class Person:
    def __init__(self, name, lname):
        self.firstname = name
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# x = Person("Hemlata", "Raghuvanshi")
# x.printname()


class Student(Person):
    def __init__(self, name, lname, year):
        super().__init__(name, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


y = Student("Hema", "Raghuvanshi", 2024)
y.welcome()


# Why Method Overloading Not support in Python-
# We may define many methods of the same name and different arguments,
# but we can only use the latest defined method. Calling the other method will produce an error.

# First product method - Takes two argument and print their product
def product(a, b):
    p = a * b
    print(p)

# Second product method
# Takes three argument and print their product


def product(a, b, c):
    p = a * b*c
    print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4, 5, 5)

