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
