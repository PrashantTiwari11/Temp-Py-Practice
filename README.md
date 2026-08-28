# 🐍 Python Practice Questions with Code

A beginner-friendly collection of Python practice questions with solutions.

This repository is designed for beginners who want to improve their Python programming skills by practicing concepts step by step.

---

## 📚 Topics Covered

* Print Statements
* Variables
* User Input
* Arithmetic Operations
* Conditional Statements
* `if`
* `if-else`
* `if-elif-else`
* `for` Loops
* `range()`
* Lists
* Loop with Lists
* Basic Problem Solving

---

# 🟢 Level 1: Print & Variables

## 1. Print Your Name

```python
name = "Prashant"

print(name)
```

### Output

```text
Prashant
```

---

## 2. Add Two Numbers

```python
num1 = 10
num2 = 20

sum = num1 + num2

print(sum)
```

### Output

```text
30
```

---

## 3. Store and Print Age

```python
age = 21

print("My age is:", age)
```

---

# 🟡 Level 2: User Input

## 4. Take Name as Input

```python
name = input("Enter your name: ")

print("Hello", name)
```

---

## 5. Add Two Numbers Using Input

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2

print("Sum =", result)
```

---

## 6. Calculate Area of Rectangle

### Formula

```text
Area = Length × Width
```

### Code

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area =", area)
```

---

# 🟠 Level 3: If-Else Practice

## 7. Check Even or Odd

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## 8. Check Positive, Negative or Zero

```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")

elif num < 0:
    print("Negative")

else:
    print("Zero")
```

---

## 9. Check Pass or Fail

```python
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

---

# 🔵 Level 4: For Loop Practice

## 10. Print Python 5 Times

```python
for i in range(5):
    print("Python")
```

---

## 11. Print Numbers from 1 to 10

```python
for i in range(1, 11):
    print(i)
```

---

## 12. Print Even Numbers from 1 to 20

```python
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
```

---

## 13. Print Odd Numbers from 1 to 20

```python
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
```

---

## 14. Print Multiplication Table

```python
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```

### Example Output

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

# 🔥 Level 5: Loop + Logic Practice

## 15. Find Sum from 1 to 10

```python
total = 0

for i in range(1, 11):
    total = total + i

print("Sum =", total)
```

### Output

```text
Sum = 55
```

---

## 16. Find Sum of Even Numbers from 1 to 100

```python
total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total = total + i

print(total)
```

---

## 17. Print All Elements of a List

```python
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)
```

---

## 18. Find Sum of List Elements

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

print(total)
```

---

## 19. Find the Largest Number in a List

```python
numbers = [10, 45, 23, 78, 12]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number =", largest)
```

---

## 20. Count Even Numbers in a List

```python
numbers = [10, 15, 20, 25, 30, 35]

count = 0

for num in numbers:
    if num % 2 == 0:
        count = count + 1

print("Even numbers =", count)
```

---

# 🎯 Practice Challenges

Try solving these questions without looking at any solution.

### Challenge 1

Take a number from the user and print its square.

### Challenge 2

Print all odd numbers from 1 to 50.

### Challenge 3

Find the sum of numbers from 1 to 100.

### Challenge 4

Find the smallest number in a list.

Example:

```python
numbers = [45, 12, 78, 3, 56]
```

---

### Challenge 5

Count positive and negative numbers in a list.

Example:

```python
numbers = [10, -5, 20, -15, 30, -8]
```

---

# 🚀 How to Run the Code

### 1. Clone the Repository

```bash
git clone <your-repository-link>
```

### 2. Open the Project Folder

```bash
cd python-practice
```

### 3. Run a Python File

```bash
python filename.py
```

---

# 🎯 Learning Goal

The goal of this repository is to build strong Python fundamentals through regular practice.

The practice questions are arranged from basic to intermediate level:

```text
Level 1 → Variables & Print
        ↓
Level 2 → User Input
        ↓
Level 3 → If-Else
        ↓
Level 4 → Loops
        ↓
Level 5 → Loops + Logic
        ↓
Next → Functions, Strings, Lists, Tuples, Dictionaries and more
```

---

## 🛠️ Technologies Used

* Python
* VS Code
* Git & GitHub

---

## 📌 Future Topics

* [ ] While Loops
* [ ] Functions
* [ ] Strings
* [ ] Lists
* [ ] Tuples
* [ ] Sets
* [ ] Dictionaries
* [ ] Pattern Problems
* [ ] File Handling
* [ ] Object-Oriented Programming
* [ ] Python Mini Projects

---

## ⭐ Keep Practicing

> "Programming is not about memorizing code. It is about understanding logic and solving problems."

Happy Coding! 🐍🚀
