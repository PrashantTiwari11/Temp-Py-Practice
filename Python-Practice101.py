# 99_python_mini_quiz_app.py
# Mini Quiz Application - 10 practical features

questions = [
    {"q": "Which keyword defines a function?", "a": "def"},
    {"q": "Which data type stores key-value pairs?", "a": "dict"},
    {"q": "Which symbol starts a comment?", "a": "#"},
    {"q": "What is 2 + 3?", "a": "5"},
    {"q": "Which collection does not allow duplicate elements?", "a": "set"},
]

for i, item in enumerate(questions, 1):
    print(f"1. Q{i}: {item['q']}")

print("2. Question count:", len(questions))

answers = ["def", "dict", "#", "5", "set"]
print("3. First answer correct:", answers[0].lower() == questions[0]["a"])

score = sum(
    user.lower() == item["a"].lower()
    for user, item in zip(answers, questions)
)
print("4. Score:", score)

percentage = score / len(questions) * 100
print("5. Percentage:", percentage)

grade = "A" if percentage >= 80 else "B" if percentage >= 60 else "C"
print("6. Grade:", grade)

correct = [item["a"] for item in questions]
print("7. Correct answers:", correct)

print("8. Result:", "PASS" if percentage >= 40 else "FAIL")
print("9. Summary:", f"{score}/{len(questions)} correct")
print("10. Quiz completed successfully.")
