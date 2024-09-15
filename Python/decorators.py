# function can take another function as an argument

def increment(x):
    return x + 1

def operate(func, x):
    result = func(x)
    return result

print(operate(increment, 3))
