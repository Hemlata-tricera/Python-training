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

