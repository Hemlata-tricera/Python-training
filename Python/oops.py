# OOPs Concept
# Inheritance
class Person:
    def __init__(self, name, lname):
        self.firstname = name
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Hemlata", "Raghuvanshi")
x.printname()


class Student(Person):
    pass

y = Student("Hema", "Raghuvanshi")
y.printname()
