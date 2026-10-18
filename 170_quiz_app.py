"""170 Quiz App: Python multiple-choice quiz with saved result history."""
import json
from datetime import datetime
from pathlib import Path
DB = Path("quiz_results.json")
QUESTIONS = [
("Which keyword defines a function?", ["A. func","B. def","C. function","D. define"], "B", "Python uses def."),
("Which type stores key-value pairs?", ["A. list","B. tuple","C. dictionary","D. set"], "C", "Dictionaries map keys to values."),
("What is len([4,5,6])?", ["A. 2","B. 3","C. 4","D. 15"], "B", "There are three items."),
("Which symbol begins a Python comment?", ["A. //","B. <!--","C. #","D. **"], "C", "A comment starts with #."),
("What is 7 // 2?", ["A. 3.5","B. 4","C. 3","D. 1"], "C", "// is floor division."),
("Which collection is immutable?", ["A. list","B. dict","C. set","D. tuple"], "D", "Tuples cannot be changed in place."),
("Which list method adds one item?", ["A. append()","B. push()","C. add_item()","D. extend_one()"], "A", "append adds one item."),
("What does input() return by default?", ["A. int","B. str","C. bool","D. float"], "B", "input returns a string."),
("Which keyword handles exceptions?", ["A. if","B. loop","C. except","D. final"], "C", "except handles exceptions."),
("Which file mode appends?", ["A. r","B. w","C. x","D. a"], "D", "Mode a appends or creates a file.")
]
def load():
    try: return json.loads(DB.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError): return []
def main():
    while True:
        print("\nPYTHON QUIZ\n1 Start quiz\n2 Result history\n0 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Name: ").strip() or "Guest"; score = 0; review = []
            for i, (q, options, correct, explanation) in enumerate(QUESTIONS, 1):
                print(f"\n{i}/{len(QUESTIONS)}. {q}")
                print("  " + "  ".join(options))
                ans = input("Answer A/B/C/D: ").strip().upper()
                while ans not in "ABCD" or len(ans) != 1:
                    ans = input("Enter A, B, C, or D: ").strip().upper()
                ok = ans == correct; score += int(ok)
                review.append((i, ok, ans, correct, explanation))
            result = {"name": name, "date": datetime.now().isoformat(timespec="seconds"),
                      "score": score, "total": len(QUESTIONS), "percent": round(score/len(QUESTIONS)*100,1)}
            history = load(); history.append(result)
            DB.write_text(json.dumps(history, indent=2), encoding="utf-8")
            print(f'\nScore: {score}/{len(QUESTIONS)} ({result["percent"]}%)')
            for i, ok, ans, correct, explanation in review:
                print(f'{i}. {"Correct" if ok else "Incorrect"}; your answer {ans}; correct {correct}. {explanation}')
        elif choice == "2":
            history = load()
            for r in history: print(f'{r["date"]} | {r["name"]} | {r["score"]}/{r["total"]} | {r["percent"]}%')
            if not history: print("No results yet.")
        elif choice == "0": break
        else: print("Invalid choice.")
if __name__ == "__main__": main()
