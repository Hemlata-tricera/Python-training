# Python String
a = "Hello"   # Assign String to a Variable
print(a)

# Multiline Strings
a = """Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!"""
print(a)

a = "Hello, World!"
print(a[1]) # Get the character at position 1 (remember that the first character has the position 0)

# Looping Through a String
for x in "banana":
  print(x)

#String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)
# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
if "expensive" not in txt:    # Use it in an if statement
  print("No, 'expensive' is NOT present.")

# SLICING STRING -You can return a range of characters by using the slice syntax.

b = "Hello, World!"
print(b[2:5])  # Get the characters from position 2 to position 5 (not included)

b = "Hello, World!"
print(b[:5])  # Slice From the Start
print(b[2:])  # Slice From the END

b = "Hello, World!"
print(b[-5:-2]) # Negative indexing

#     MODIFY STRING
s1 = "hemlata"
print(s1.upper())

print(s1.lower())

# Remove Whitespace
s2 = " Hemlata  "
print(s2)
print(s2.strip())

# Replace String
s3 = "Hello world"
print(s3.replace("H", "J"))
print(s3.split(","))  # Split String

# String Concatenation
s4 = "Good"
s5 = "Morning"
s6 = s4 + s5
print(s6)
s6 = s4 + " " + s5  # To add a space between them, add a " "
print(s6)

# Format - Strings
age = 31
txt = f"Hello, I am {age} year old"  # Placeholder contains variable
print(txt)

price = 57
txt = f"The price is {price:.2f} dollars"  # here placeholder include a modifier to format the value.
print(txt)

txt = f"The price is {10 * 20} dollars"  # Here placeholder contain math python code(math operation)
print(txt)

# Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "For new line please insert \\n "
print(txt)

txt = "Hello\nWorld!"
print(txt)
txt = "Hello\tWorld!"
print(txt)
# This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)
# A backslash followed by three integers will result in a octal value
txt = "\110\145\154\154\157"
print(txt)
# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

# STRING METHODS
# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

# The upper() method returns a string where all characters are in upper case.
x = txt.upper()
print(x)

# The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
txt = "Welcome to my 2nd world"
x = txt.title()
print(x)

#The casefold() method returns a string where all the characters are lower case.
x = txt.casefold()
print(x)

# The lower() method returns a string where all characters are lower case.
s1 = "HelLOO"
x = s1.lower()
print(x)

# The islower() method returns True if all the characters are in lower case, otherwise False.
print(x.islower())

# The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

# The center() method will center align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.center(20)
print(x)
x = txt.center(20, "H")
print(x)
x = txt.center(20, "P")
print(x)

# The count() method returns the number of times a specified value appears in the string.
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
txt = "My name is Ståle"
x = txt.encode()
print(x)

print(txt.encode(encoding="ascii",errors="backslashreplace"))  # uses a backslash instead of the character that could not be encoded
print(txt.encode(encoding="ascii",errors="ignore"))  # ignores the characters that cannot be encoded
print(txt.encode(encoding="ascii",errors="namereplace"))  # replaces the character with a text explaining the character
print(txt.encode(encoding="ascii",errors="replace"))  # - replaces the character with a questionmark
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))  # - replaces the character with an xml character

# Python String endswith() Method
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
x = txt.endswith("my world.")  # Check if the string ends with the phrase "my world."
print(x)
x = txt.endswith("my world.", 5, 11)  # Check if position 5 to 11 ends with the phrase "my world."
print(x)

# The expandtabs() method sets the tab size to the specified number of whitespaces.
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())  # Default tabsize is 8
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# find() Method finds the first occurrence of the specified value.
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)



# ************************************ASSIGNMENT******************************************************************
# STRING FORMATTING
# To specify a string as an f-string, simply put an f in front of the string literal,
# and add curly brackets {} as placeholders for variables and other operations.

name = "Hemlata"
S1 = f"My name is { name }."  # Placeholder contains variable(variable contain string)
print(S1)

current_age = 31
txt = f"Hello, I am {current_age} year old"  # Placeholder contains variable
print(txt)

product_price = 50
txt = f"The price is {product_price:.2f} dollars"  # here placeholder include a modifier to format the value.
print(txt)

price = 49
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}" # Here placeholder contain math python code(math operation)
print(txt)


# STRING OPERATIONS
# 1. Changing Case
# upper(): Converts all characters to uppercase.
text = "Hello World"
print("upper() method converts all characters to uppercase.", text.upper())

# lower(): Converts all characters to lowercase.
print("lower(): Converts all characters to lowercase.", text.lower())

# capitalize(): Capitalizes the first character of the string.
print("capitalize(): Capitalizes the first character of the string.", text.capitalize())

# title(): Capitalizes the first character of each word in the string.
print("title(): Capitalizes the first character of each word in the string.", text.title())

# swapcase(): Swaps the case of all characters.
print("swapcase(): Swaps the case of all characters.", text.swapcase())

# casefold(): Converts the string to lowercase and is more aggressive than lower() for case-insensitive comparisons.
print("casefold(): Converts the string to lowercase and is more aggressive than lower() for case-insensitive comparisons.", text.casefold())


# 2.Whitespace Management
# strip(): Removes leading(beginning) and trailing (end) whitespace.
S = "   banana   "
X = S.strip()
print("of all fruits", X, "is my favorite")
# strip(chars): Removes leading and trailing characters specified in chars.
S1 = ",,,,,rrttgg.....banana....rrr"
x = S1.strip(",.grt")
print(x)

# lstrip(): Removes leading whitespace.
print("lstrip(): Removes leading whitespace.", S.lstrip())

#lstrip(chars): Removes leading characters specified in chars.
S1 = ",,,,,rrttgg.....banana....rrr"
print("lstrip(chars): Removes leading characters specified in chars", S1.lstrip(".,tgr"))

#rstrip(): Removes trailing whitespace.
print("rstrip(): Removes trailing whitespace.", S.rstrip())

# rstrip(chars): Removes trailing characters specified in chars.
print("rstrip(chars): Removes trailing characters specified in chars.", S1.rstrip(".r"))

# 3. Padding and Alignment:
S2 = "Hello"
# ljust(width, fillchar): Left-justifies the string in a field of the given width, padding with fillchar.
print("ljust(20, '*'):", S2.ljust(20, '*'))
print("ljust(20):", S2.ljust(20))  # A character to fill the missing space (to the right of the string). Default is " " (space).

# rjust(width, fillchar): Right-justifies the string in a field of the given width, padding with fillchar.
print("rjust(20, '*'):", S2.rjust(20, '*'))
print("rjust(20):", S2.rjust(20))  # A character to fill the missing space (to the left of the string). Default is " " (space).

# center(width, fillchar): Centers the string in a field of the given width, padding with fillchar.
print("center(20, '*'):", S2.center(20, '*'))
print("center(20):", S2.center(20))  # Default parameter is space

# zfill(width): Pads the string with zeros on the left, ensuring the string is at least width characters long.
print("zfill(20):", S2.zfill(20))


# 4.Searching
S3 = "This is Python tutorial"
# find(substring): Returns the lowest index where substring is found. Returns -1 if not found.
print("find('python')", S3.find("Python"))
# string.find(value, start, end): start(default is 0) and end(Default is to the end of the string) parameter are optional
print("find('i')", S3.find("i", 3,7))  # find with parameter

# rfind(substring): Returns the highest index where substring is found. Returns -1 if not found.
print("rfind('o')", S3.rfind("o"))
print("rfind('i')", S3.rfind("i", 1, 10))  # rfind with parameter[string.rfind(value, start, end)]

# index(substring): Like find(), but raises ValueError if substring is not found.
print("index('python')", S3.index("Python"))
print("index('i')", S3.index("i", 1, 10)) # index with parameter[string.index(value, start, end)]

# rindex(substring): Like rfind(), but raises ValueError if substring is not found.
print("rindex('i')", S3.rindex("i"))

# startswith(prefix): Checks if the string starts with prefix.
print('startwith("This")', S3.startswith("This"))
print('startwith("Python", 8, 15)', S3.startswith("Python", 8, 15)) # Startswith with parameter

# endswith(suffix): Checks if the string ends with suffix.
print('endswith("tutorial")', S3.endswith("tutorial"))
print('endswith("tutorial", 15, 25)', S3.endswith("tutorial", 15, 25))  # endswith with parameter


# 5. Replacing
S3 = "This is Python tutorial"
# replace(old, new): Replaces all occurrences of old with new.
print("replace('tutorial', 'Learning')", S3.replace("tutorial", "Learning") )
# replace(old, new, count): Replaces up to count occurrences of old with new.
print("replace('i', 'I', 2)", S3.replace("i", "I", 2) )  # with parameter















