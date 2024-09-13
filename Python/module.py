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







