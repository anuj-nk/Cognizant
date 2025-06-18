# Task 1
# All I'm doing here is declaring the variables and printing them with the correct data types and concatenation
name = "Anuj"
age = 21
height = 6.3

print("Yo, what's up my name's " + name + "! I'm " + str(age) + " years old and " + str(height) + " feet tall.")

# Task 2
# Here is the same thing except using mathematical formulas inside the print statements
num1 = 12
num2 = 8
print("The sum of " + str(num1) + " and " + str(num2) + " is", num1 + num2)
print("The subtraction of " + str(num1) + " and " + str(num2) + " is", num1 - num2)
print("The multiplication of " + str(num1) + " and " + str(num2) + " is", num1 * num2)
print("The division of " + str(num1) + " and " + str(num2) + " is", num1 / num2)

# Task 3
# Utilizing conditionals to create the desired result based on input
num = int(input("Please enter a number: "))
if num > 0:
    print("This number is positive. Awesome!")
elif num < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")