# 126_python_mini_quiz_leaderboard.py
# Mini Quiz Leaderboard - 10 practical features

scores = {"Aman": 8, "Riya": 10, "Karan": 6, "Neha": 9}
print("1. Scores:", scores)
print("2. Player count:", len(scores))
print("3. Total points:", sum(scores.values()))
print("4. Average score:", round(sum(scores.values()) / len(scores), 2))
winner = max(scores, key=scores.get)
print("5. Winner:", winner, scores[winner])
lowest = min(scores, key=scores.get)
print("6. Lowest score:", lowest, scores[lowest])
leaderboard = sorted(scores.items(), key=lambda item: item[1], reverse=True)
print("7. Leaderboard:", leaderboard)
print("8. Scores >= 8:", [n for n, s in scores.items() if s >= 8])
scores["Priya"] = 7
print("9. Added player:", "Priya", scores["Priya"])
ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
print("10. Rankings:")
for rank, (name, score) in enumerate(ranked, start=1):
    print(rank, name, score)
