# Creating a Function
# In Python a function is defined using the def keyword:

def my_function():
  print("Hello from a function")

# Calling a Function
# To call a function, use the function name followed by parenthesis:

def my_function():
  print("Hello from a function")

my_function()

# Arguments
def full_name(fname):
  print(f"Fullname of { fname } is { fname } Pawar")

full_name("Jayesh")
full_name("Suresh")
full_name("Mangesh")

# Numbers of argument
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")   # This function expects 2 arguments, and gets 2 arguments:


# Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Suresh")


# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass
