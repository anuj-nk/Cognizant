import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")
print("Can you guess it within 10 attempts? Let's do it!\n")

number_to_guess = random.randint(1, 100)
attempts = 0

while attempts < 10:
    try:
        guess = int(input(f"Attempt {attempts + 1}: Guess the number (1-100): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    attempts += 1

    if guess < 1 or guess > 100:
        print("Your guess is out of range. Try a number between 1 and 100.")
    elif guess < number_to_guess:
        print("Too low! Try again.\n")
    elif guess > number_to_guess:
        print("Too high! Try again.\n")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempt(s)!")
        break
else:
    print(f"Game over! The number was {number_to_guess}. Better luck next time! :(")

print("Thank you for playing!")
