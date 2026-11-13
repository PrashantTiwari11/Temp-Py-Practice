"""Practice basic Python concepts with flashcards."""
def main():
    cards = {
        "What keyword defines a function in Python?": "def",
        "Which type stores True or False?": "bool",
        "What symbol starts a Python comment?": "#",
        "Which function displays output?": "print",
    }
    score = 0
    print("Python Flashcard Quiz")
    for question, answer in cards.items():
        response = input(question + " ").strip()
        if response.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The answer is: {answer}")
    print(f"\nFinal score: {score}/{len(cards)}")

if __name__ == "__main__":
    main()
