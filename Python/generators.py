# A generator is a function that returns an iterator that produces a sequence of values when iterated over.

def even_generator():
    n = 0

    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n

numbers = even_generator()

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))



# Example 2- Odd numbers

def odd_generators():
    n = 1
    print(n)

    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n

num = odd_generators()
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))