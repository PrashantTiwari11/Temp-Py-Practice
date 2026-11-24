"""Project 304: Multiplication Practice Quiz"""
import random

def main():
    try:
        questions = int(input("How many questions would you like? "))
    except ValueError:
        print("Please enter a whole number.")
        return
    if questions <= 0:
        print("Please choose at least one question.")
        return

    score = 0
    for index in range(1, questions + 1):
        a, b = random.randint(1, 12), random.randint(1, 12)
        try:
            answer = int(input(f"Question {index}: {a} x {b} = "))
        except ValueError:
            print(f"Please use a whole-number answer. Correct answer: {a * b}")
            continue
        if answer == a * b:
            print("Correct!")
            score += 1
        else:
            print(f"Not quite. The correct answer is {a * b}.")
    print(f"Final score: {score}/{questions}")

if __name__ == "__main__":
    main()
