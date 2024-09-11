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

# Types of inheritance
# Multiple Inheritance

class Mother:
    mothername = " "

    def mother(self):
        print(self.mothername)


class Father:
    fathername = " "

    def father(self):
        print(self.fathername)


class Son(Mother, Father):
    def parents(self):
        print("Father", self.fathername)
        print("Mother", self.mothername)

s1 = Son()
s1.fathername = "Ajay"
s1.mothername = "Anjali"
s1.parents()


# Multilevel inheritance

class Grandfather:
    def __init__(self, gfathername):
        self.gfathername = gfathername


class Father(Grandfather):
    def __init__(self, fathername, gfathername):
        self.fathername = fathername

        # invoking constructor of Grandfather class
        Grandfather.__init__(self, gfathername)


class Son(Father):
    def __init__(self, sonname, fathername, gfatthername):
        self.sonname = sonname

        # invoking constructor of Father class
        Father.__init__(self, fathername, gfatthername)

    def print_name(self):
        print("Grandfather name:", self.gfathername)
        print("Father Name:", self.fathername)
        print("Son Name:", self.sonname)



s1 = Son("Ajay", "Avinash", "Anil")
print(s1.gfathername)
s1.print_name()


# ENCAPSULATION-

class student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def test(self):
        return "hello"


class student1(student):
    def __init__(self, rn, name, age):
        self.rn = rn
        super().__init__(name, age)

    def test(self):
        return "Hello World"


std2 = student("Hema", 31)
print(std2.name)
print(std2.test())



# Abstraction

from abc import ABC, abstractmethod


class democlass(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return

    def method2(self):
        print("concrete method")


class concreteclass(democlass):
    def method1(self):
        super().method1()
        return


obj = concreteclass()
obj.method1()
obj.method2()
