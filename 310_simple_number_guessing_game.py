# Simple Number Guessing Game

import random

secret_number = random.randint(1, 20)
attempts = 0

print("Guess the number between 1 and 20!")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    attempts += 1

    if not 1 <= guess <= 20:
        print("Your guess must be between 1 and 20.")
    elif guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempt(s).")
        break
