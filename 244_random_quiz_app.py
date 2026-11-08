import random

QUESTIONS = [
    ("Which language is commonly used for data analysis?",
     ["A) Python", "B) HTML", "C) CSS", "D) XML"], "A"),
    ("What does CPU stand for?",
     ["A) Central Program Unit", "B) Central Processing Unit",
      "C) Computer Personal Unit", "D) Control Processing Utility"], "B"),
    ("Which data structure follows FIFO?",
     ["A) Stack", "B) Tree", "C) Queue", "D) Graph"], "C"),
    ("Which SQL command retrieves data?",
     ["A) SELECT", "B) UPDATE", "C) DELETE", "D) INSERT"], "A"),
    ("What is the extension of a Python file?",
     ["A) .java", "B) .py", "C) .html", "D) .sql"], "B"),
]

def main():
    questions = QUESTIONS.copy()
    random.shuffle(questions)
    score = 0
    print("Python & Computer Basics Quiz")
    for index, (question, options, correct) in enumerate(questions, 1):
        print(f"\\nQ{index}. {question}")
        for option in options:
            print(option)
        answer = input("Answer (A/B/C/D): ").strip().upper()
        if answer == correct:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {correct}")
    print(f"\\nFinal score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
