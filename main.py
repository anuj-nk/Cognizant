# Task 1
while True:
    try:
        num = int(input("Enter a number: "))
        result = 100 / num
        print(f"100 divided by {num} is {result}.")
        break
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Task 2
# Index Error
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("IndexError occurred! List index out of range.")

# KeyError
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# TypeError
try:
    result = "age" + 5
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

# Task 3
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")
