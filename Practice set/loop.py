# Exercise 1: Print first 10 natural numbers using while loop
count = 1
while count < 11:
    print(count)
    count += 1

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Solution-1

for i in range(1, 6):
    for j in range(0,i):
        print(j+1, end=' ')
    print()

# Solution-2
for i in range(2, 7):
    for j in range(1, i):
        print(j, end=' ')
    print()