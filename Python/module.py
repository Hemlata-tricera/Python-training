import mymodule as mx
import platform
import datetime



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


# Python Dates
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

# Creating Date Objects - The datetime() class requires three parameters to create a date: year, month, day.
z = datetime.datetime(2024, 9, 17)

print(z)

# The strftime() Method
print(x.strftime("%B"))  # Month name, full version
print(x.strftime("%b"))  # Month name, short version
print(x.strftime("%Y"))  # Year, full version
print(x.strftime("%y"))  # Year, short version, without century
print(x.strftime("%a"))  # Weekday, short version
print(x.strftime("%A"))  # Weekday, full version
print(x.strftime("%w"))  # Weekday as a number 0-6, 0 is Sunday
print(x.strftime("%d"))  # Day of month 01-31
print(x.strftime("%H"))  # Hour 00-23
print(x.strftime("%I"))  # Hour 00-12
print(x.strftime("%p"))  # AM/PM
print(x.strftime("%M"))  # Minute 00-59
print(x.strftime("%S"))  # Second 00-59
print(x.strftime("%f"))  # Microsecond 000000-999999
print(x.strftime("%x"))  # Local version of date
print(x.strftime("%X"))  # Local version of time
print(x.strftime("%%"))  # Local version of time


# Python Math
# Built-in Math Functions
# 1. min()
x = min(5, 10, 25)
print(x)

#2. max()
y = max(5, 10, 25)
print(y)

# 3. The abs() - function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print(x)

# 4. The pow(x, y)- function returns the value of x to the power of y (xy).
x = pow(4, 3)  # Return the value of 4 to the power of 3 (same as 4 * 4 * 4)
print(x)

# The Math Module
import math

x = math.sqrt(64)
print(x)

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1


x = math.pi
print(x)


import camelcase
c = camelcase.CamelCase()
txt = "Hello world!"
print(c.hump(txt))  # #This method capitalizes the first letter of each word.


