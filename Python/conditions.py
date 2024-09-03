# If statement:
a = 10
b = 20

if b > a:
    print("b is greater than a")

# Elif-The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 10
b = 10

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b  are equal")

# Else - The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 30

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b  are equal")
else:
    print("a is greater than b")

# Short Hand If - If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b")  # One line if statement:

# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 2
b = 100
print("A") if a > b else print("B")

# You can also have multiple else statements on the same line:
a = 100
b = 100
print("A") if a > b else print("=") if a == b else print("B")

# And
# The and keyword is a logical operator, and is used to combine conditional statements
a = 100
b = 50
c = 200
if a > b and c > b:  # Test if a is greater than b, AND if c is greater than a
    print("Both conditions are True")

# Or
# The or keyword is a logical operator, and is used to combine conditional statements
if a > b or a > c:
    print("At least one condition is True")

# Nested If
# You can have if statements inside if statements, this is called nested if statements
x = 40
if x > 10:
    print("Above 10,")
    if x > 20:
        print("and also above 20!")
    else:
        print(" but not above 20.")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
    pass  # having an empty if statement like this, would raise an error without the pass statement



# The WHILE LOOP- With the while loop we can execute a set of statements as long as a condition is true.
# Print i as long as i is less than 6
i = 1
while i < 6:
    print(i)
    i += 1   # Note: remember to increment i, or else the loop will continue forever.

# The break Statement-With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue Statement-With the continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer leas than 6")  # Print a message once the condition is false:



# FOR LOOP -A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# BREAK Statement- With the break statement we can stop the loop before it has looped through all the items
# Example- Exit the loop when x is "banana":
for x in fruits:
    print(x)
    if x == "banana":
        break
# Example-2 Exit the loop when x is "banana", but this time the break comes before the print
for x in fruits:
    if x == "banana":
        break
    print(x)

# The continue Statement- With the continue statement we can stop the current iteration of the loop, and continue with the next:

for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function - The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.

for x in range(6):   # Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
    print(x)


# it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)
for x in range(2, 6):
    print(x)

# it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
for x in range(2, 20, 2):
    print(x)


# Else in For Loop - The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
    print(x)
else:
    print("Finally Finished")


# Nested Loops-A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop"
greetings = ["Good Morning", "Good Afternoon", "Good Evening"]
users = ["Yogesh!", "Somesh!", "Rakesh!" ]

for x in greetings:
    for y in users:
        print(x, y)


# The pass Statement
for x in [0, 1, 2]:
  pass


# -------------------------------------ASSIGNMENT---------------------------------------------------------------------

# Example 1
for x in range(3):

    for i in range(0, 10):
        print(x, end=" ")
    print()

# Example 2- Pattern for rectangle
rows = int(input("Enter the value of rows"))
columns = int(input("Enter the value of columns"))
symbol = input("Enter the symbol")
for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()


