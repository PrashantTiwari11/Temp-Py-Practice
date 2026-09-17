# 70_python_data_structures.py
# Advanced Data Structures - 10 practical programs/features
from collections import Counter, deque, defaultdict

stack = []
stack.append("A")
stack.append("B")
print("1. Stack:", stack, "pop =", stack.pop())

queue = deque(["A", "B", "C"])
queue.append("D")
print("2. Queue:", queue, "dequeue =", queue.popleft())

words = ["python", "java", "python", "sql", "python", "java"]
print("3. Word frequency:", Counter(words))

print("4. Most common:", Counter(words).most_common(2))

groups = defaultdict(list)
for name, branch in [("Prashant", "CE"), ("Aman", "CE"), ("Riya", "IT")]:
    groups[branch].append(name)
print("5. Grouped students:", dict(groups))

a, b = {1, 2, 3, 4}, {3, 4, 5, 6}
print("6. Union:", a | b)
print("7. Intersection:", a & b)
print("8. Difference:", a - b)

marks = {"Aman": 72, "Riya": 91, "Prashant": 85}
print("9. Sorted by marks:", sorted(marks.items(), key=lambda x: x[1], reverse=True))

numbers = range(1, 11)
print("10. Even number squares:", [n * n for n in numbers if n % 2 == 0])
