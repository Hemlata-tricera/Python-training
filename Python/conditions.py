# If statement:
a = 10
b = 20

if b > a:
    print("b is greater than a")

# Elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 10
b = 10

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b  are equal")

# Else
# The else keyword catches anything which isn't caught by the preceding conditions.


a = 200
b = 30

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b  are equal")
else:
    print("a is greater than b")

# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
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
    print("i is no longer leass than 6")  # Print a message once the condition is false:

