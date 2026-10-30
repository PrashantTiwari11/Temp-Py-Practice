"""209 - Word Guessing Game"""
import random

WORDS = ["python", "notebook", "variable", "function", "keyboard", "database", "analysis", "program"]

def main():
    word = random.choice(WORDS)
    guessed = set()
    mistakes = 0
    while mistakes < 6:
        print("\nWord:", " ".join(c if c in guessed else "_" for c in word), f"| Mistakes: {mistakes}/6")
        if all(c in guessed for c in word):
            print("You won!")
            return
        guess = input("Enter one letter (or q to quit): ").strip().lower()
        if guess == "q":
            print("The word was:", word)
            return
        if len(guess) != 1 or not guess.isalpha():
            print("Enter exactly one letter.")
            continue
        if guess in guessed:
            print("You already tried that letter.")
            continue
        guessed.add(guess)
        if guess not in word:
            mistakes += 1
            print("Not in the word.")
    print("Game over. The word was:", word)

if __name__ == "__main__":
    main()
