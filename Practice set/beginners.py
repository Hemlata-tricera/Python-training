def product_of_number_or_sum(n1,n2):
    product = n1 * n2
    if product <= 1000:
        return product
    else:
        return n1 + n2


result = product_of_number_or_sum(20, 30)
print("The result is", result)


result = product_of_number_or_sum(40, 30)
print("The result is", result)


# Exercise 2: Print the Sum of a Current Number and a Previous number
def sum_of_current_and_previous_num():
    print("Printing current and previous number and their sum in a range(10)")
    previous_num = 0
    for i in range(0,10):
        sum = previous_num + i
        print("current number", i, "Previous number", previous_num, "Sum: ", sum)
        previous_num = i


result = sum_of_current_and_previous_num()

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

# Exercise 5: Check if the first and last numbers of a list are the same
def first_last_same(numberList):
    print("Given List is:", numberList)

    first_num = numberList[0]
    last_num = numberList[-1]
    print("First and last number of list are same?")

    if first_num == last_num:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

# Exercise 6: Display numbers divisible by 5
def divisible_by_five(num_list):
    print("Given List", num_list)
    print("Divisible by 5:")
    for num in num_list:
        if num % 5 == 0:
            print(num)
list = [10, 20, 33, 35, 44, 40]
r = divisible_by_five(list)


# Exercise 7: Find the number of occurrences of a substring in a string
# Solution-1
str_x = "Emma is good developer. Emma is a writer"
# use count method of a str class
cnt = str_x.count("Emma")
print(cnt)

# Solution-2
def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")


# Exercise 8: Print the following pattern

for num in range(10):
    for i in range(num):
        print(num, end=" ")
    print("\n")


# Exercise 9: Check Palindrome Number
def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")


palindrome(121)
palindrome(125)

# Exercise 10: Merge two lists using the following condition
def merge_list(list1, list2):
    list3 = []
    for i in list1:
        if i % 2 != 0:
            list3.append(i)


    for i in list2:
        if i % 2 == 0:
            list3.append(i)

    return list3

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print("List 3:", merge_list(list1, list2))

# Exercise 11: Get each digit from a number in the reverse order.
def reverse_num(number):
    print("Given number is", number)
    while number > 0:
        digit = number % 10
        number = number // 10
        print(digit, end=" ")


reverse_num(123)


# Exercise 12: Calculate income tax
income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)








# Exercise 13: Print multiplication table from 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")


# Exercise 14: Print a downward half-pyramid pattern of stars

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")




