# Step 2:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Step 3:
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def get_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val < 0:
                print("Please enter a positive integer.")
            else:
                return val
        except ValueError:
            print("That's not a valid number. Try again.")

def main():
    print("Welcome to the Recursive Artistry Program!")

    while True:
        print("\nChoose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Exit")
        choice = input("> ")

        if choice == "1":
            num = get_positive_int("Enter a number to find its factorial: ")
            print(f"The factorial of {num} is {factorial(num)}.")

        elif choice == "2":
            num = get_positive_int("Enter the position of the Fibonacci number: ")
            print(f"The {num}th Fibonacci number is {fibonacci(num)}.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
