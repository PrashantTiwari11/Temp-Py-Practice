# 86_python_functional_programming.py
# Functional Programming - 10 practical programs/features
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
print("1. Map:", list(map(lambda x: x * 2, numbers)))
print("2. Filter:", list(filter(lambda x: x % 2 == 0, numbers)))
print("3. Reduce sum:", reduce(lambda a, b: a + b, numbers))

students = [("Aman", 72), ("Riya", 91), ("Prashant", 85)]
print("4. Lambda sorting:", sorted(students, key=lambda x: x[1], reverse=True))
print("5. List comprehension:", [x ** 2 for x in numbers])
print("6. Conditional comprehension:", [x ** 2 for x in numbers if x % 2 == 0])
print("7. Generator expression:", sum(x ** 2 for x in numbers))
print("8. Any/all:", any(x % 2 == 0 for x in numbers), all(x > 0 for x in numbers))
print("9. Zip:", dict(zip(["Aman", "Riya", "Raj"], [75, 88, 69])))

def add_one(x): return x + 1
def square(x): return x * x
print("10. Function composition:", square(add_one(4)))
