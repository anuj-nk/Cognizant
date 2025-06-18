# Task 1
start = int(input("Enter the starting number: "))
while start > 0:
    print(str(start), end=" ")
    start -= 1
print("Blast off! 🚀")

# Task 2
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(str(num) + " x " + str(i) + " = " + str(num * i))

# Task 3
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("The factorial of " + str(n) +  " is " + str(factorial) + ".")
