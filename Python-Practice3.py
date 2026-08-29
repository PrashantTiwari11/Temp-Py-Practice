# 🟢 Level 6: While Loop
# 21. Print numbers from 1 to 10
i = 1

while i <= 10:
    print(i)
    i = i + 1
#22. Print even numbers from 1 to 20
i = 1

while i <= 20:
    if i % 2 == 0:
        print(i)

    i = i + 1
#23. Print numbers from 10 to 1
i = 10

while i >= 1:
    print(i)
    i = i - 1
#24. Find the sum from 1 to 10
i = 1
total = 0

while i <= 10:
    total = total + i
    i = i + 1

print("Sum =", total)

# 🟡 Level 7: String Practice
# 25. Print every character of a string
name = "Python"

for char in name:
    print(char)
#26. Count the length of a string
name = input("Enter your name: ")

print("Length =", len(name))
#27. Check whether a character exists in a string
text = "Python Programming"

if "P" in text:
    print("Character found")
else:
    print("Character not found")
#28. Convert string into uppercase
name = input("Enter your name: ")

print(name.upper())
#29. Convert string into lowercase
name = input("Enter your name: ")

print(name.lower())
#30. Reverse a string
text = input("Enter a string: ")

reverse_text = text[::-1]

print("Reverse =", reverse_text)