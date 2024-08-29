# Python String
a = "Hello"   # Assign String to a Variable
print(a)

#Multiline Strings
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


