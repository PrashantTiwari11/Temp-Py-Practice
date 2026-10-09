# 146 - Mini Quiz Game: 10 practical features
questions = [
 {"question":"Which keyword defines a function in Python?","options":["A. func","B. def","C. function","D. define"],"answer":"B"},
 {"question":"Which type stores key-value pairs?","options":["A. list","B. tuple","C. dict","D. set"],"answer":"C"},
 {"question":"What does len([1, 2, 3]) return?","options":["A. 2","B. 3","C. 4","D. 6"],"answer":"B"},
 {"question":"Which symbol starts a comment?","options":["A. //","B. <!--","C. #","D. **"],"answer":"C"}]
score_history = []
# 1. Show questions
def show_questions():
    for i, q in enumerate(questions, 1): print(f"{i}. {q['question']}")
# 2. Count questions
def question_count(): return len(questions)
# 3. Add a question
def add_question(question, options, answer):
    if len(options) != 4 or answer.upper() not in {"A","B","C","D"}: raise ValueError("Use four options and answer A-D.")
    questions.append({"question":question,"options":options,"answer":answer.upper()})
# 4. Check answer
def check_answer(index, answer): return questions[index]["answer"] == answer.strip().upper()
# 5. Calculate percentage
def percentage(score, total): return round(score / total * 100, 1) if total else 0
# 6. Grade a result
def grade_label(percent):
    if percent >= 90: return "Excellent"
    if percent >= 70: return "Good"
    if percent >= 50: return "Keep practicing"
    return "Needs more practice"
# 7. Run the quiz
def run_quiz():
    score = 0
    for i, q in enumerate(questions):
        print("\n" + q["question"])
        for option in q["options"]: print(option)
        answer = input("Answer (A/B/C/D): ")
        if check_answer(i, answer): print("Correct!"); score += 1
        else: print("Incorrect. Correct answer:", q["answer"])
    score_history.append(score)
    pct = percentage(score, len(questions))
    print(f"Score: {score}/{len(questions)} ({pct}%) - {grade_label(pct)}")
# 8. Best score
def best_score(): return max(score_history, default=0)
# 9. Average score
def average_score(): return round(sum(score_history) / len(score_history), 2) if score_history else 0
# 10. Show score history
def show_score_history(): print("Scores:", score_history, "| Best:", best_score(), "| Average:", average_score())
if __name__ == "__main__":
    run_quiz()
    show_score_history()
