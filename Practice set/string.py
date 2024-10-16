# Exercise 3: Print characters present at an even index number
# Solution-1
print("Orginal String is  PYnative")
print("Printing only even index chars")
str = "PYnative"
x = list(str)
for i in x[0::2]:
    print(i)

#Solution-2
def print_even_index_char():
    word = input("Enter word")
    print("Original String:", word)
    size = len(word)
    print("Printing only even index chars")
    for i in range(0, size, 2):
        print("index[", i, "]", word[i])

res = print_even_index_char()

# Exercise 4: Remove first n characters from a string
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("Python Excercise", 5))
print(remove_chars("Python Exercise", 2))

