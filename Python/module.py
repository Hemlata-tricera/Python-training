import mymodule as mx
import platform

mx.greeting("Anthony")

a = mx.person1['age']
print(a)

x = platform.system()
print(x)

# Using the dir() Function

y = dir(platform)
print(y)

# Import From Module
from mymodule import person1
print(person1["age"])

