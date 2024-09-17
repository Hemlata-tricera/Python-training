# function can take another function as an argument

def increment(x):
    return x + 1

def operate(func, x):
    result = func(x)
    return result

print(operate(increment, 3))

# Function inside a function


def print_msg(message):
    greeting = "Hello"

    def printer():
        print(greeting, message)
    return printer


# print_msg("Python is awesome")
fun = print_msg("Python is awesome")  # Function can also return another function as a value
fun()


# A python decorator is a function that takes in a function, adds some functionality to it and return original function.

def display_ifo(func):

    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Finished execution")
    return inner


@display_ifo
def printer():
    print("Hello world!")

printer()


# decorating function with parameters
def smart_divide(func):
    def inner(a, b):
        print("Dividing ", a, "by", b)
        if b == 0:
            print("Cannot divide by zero")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    return a / b

value1 = divide(15, 3)
print(value1)

value2 = divide(5, 0)
print(value2)


# Chaining decorator in python
def star(func):
    def inner(arg):
        print("*" * 30)
        func(arg)
        print("*" * 30)
    return inner


def percent(func):
    def inner(arg):
        print("%" * 30)
        func(arg)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Decorators are wonderful")



def salary(bonus):
    def only_salary():
        print("Before the function")
        print(bonus() + 1000)

        print("After function")
    return only_salary



@salary
def salary_with_bonus():
    print("My salary with bonus")
    return 500


# result = salary(salary_with_bonus)
# print(result)
salary_with_bonus()



# Practice Example
def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

@smart_div
def div(a, b):
    print(a / b)


div(2, 4)

