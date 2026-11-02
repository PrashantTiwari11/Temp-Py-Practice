"""222 - Multiple Choice Python Quiz"""
QUESTIONS = [
    ("Which keyword defines a function?", ["A. func", "B. def", "C. function", "D. define"], "B"),
    ("Which type stores key-value pairs?", ["A. list", "B. tuple", "C. dictionary", "D. set"], "C"),
    ("What is 3 ** 2?", ["A. 6", "B. 8", "C. 9", "D. 32"], "C"),
    ("Which function returns a list's length?", ["A. size()", "B. count()", "C. len()", "D. length()"], "C"),
]

def main():
    score = 0
    for number, (question, options, correct) in enumerate(QUESTIONS, 1):
        print(f"\n{number}. {question}")
        for option in options:
            print(option)
        answer = input("Answer (A/B/C/D): ").strip().upper()
        if answer == correct:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Correct answer:", correct)
    print(f"\nFinal score: {score}/{len(QUESTIONS)}")

if __name__ == "__main__":
    main()
