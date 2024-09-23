# Exercise 1: Accept numbers from a user

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

mul = num1 * num2
print(f"Multiplication of {num1} and {num2} is", mul)


# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
print('My', 'Name', 'Is', 'James', sep="**")

# Exercise 3: Convert Decimal number to octal using print() output formatting
num = 9
print('%o' % num)

# Exercise 4: Display float number with 2 decimal places using print()
num = 458.541315
print('%.2f' % num)


# Exercise 5: Accept a list of 5 float numbers as an input from the user
num = []

for i in range(0, 5):
    print("Enter number at location", i, ":")

    item = float(input())
    num.append(item)
print("User List", num)

# Exercise 6: Write all content of a given file into a new file by skipping line number 5






# Exercise 7: Accept any three string from one input() call

s1, s2, s3 = input("Enter three string"). split()
print('Name1', s1)
print('Name2', s2)
print('Name3', s3)


# Exercise 8: Format variables using a string.format() method.
totalMoney = 1000
quantity = 3
price = 450

print(f"I have {totalMoney} dollars so I can buy {quantity} football for {price} dollars.")

# Exercise 9: Check file is empty or not
import os
size = os.stat('test.txt').st_size
if size == 0:
    print("File is empty")


# Exercise 10: Read line number 4 from the following file

f = open('test.txt', 'r')

lines = f.readlines()
print(lines[3])

f.close()