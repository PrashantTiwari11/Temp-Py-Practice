#✅ Challenge 1: List mein Largest aur Smallest Number Find Karo
numbers = [45, 12, 78, 3, 56, 90, 23]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest number =", largest)
print("Smallest number =", smallest)
#Output
# Largest number = 90
# Smallest number = 3
#✅ Challenge 2: Prime Number Check Karo

#Prime number woh hota hai jo sirf 1 aur khud se divide hota hai.

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")

else:
    is_prime = True

    for i in range(2, num):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
# Example
# Enter a number: 7
# Prime Number
# ✅ Challenge 3: String mein Vowels Count Karo

# Vowels:

# a, e, i, o, u
text = input("Enter a string: ")

count = 0

for char in text.lower():

    if char in "aeiou":
        count = count + 1

print("Total vowels =", count)
# Example
# Enter a string: Python Programming
# Total vowels = 4
# ✅ Challenge 4: List se Duplicate Elements Remove Karo
# Method 1: Using Loop
numbers = [10, 20, 30, 20, 40, 10, 50]

unique_numbers = []

for num in numbers:

    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)
#Output
[10, 20, 30, 40, 50]
#✅ Challenge 5: Numbers Divisible by Both 3 and 5
for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print(i)
#Output
15
30
45
60
75
90

#💡 Logic:

# i % 3 == 0

# AND

# i % 5 == 0

# Dono conditions true honi chahiye.

#✅ Challenge 6: Reverse a Number Without Using [::-1]

#Example:

#1234 → 4321
num = int(input("Enter a number: "))

reverse = 0

while num > 0:

    digit = num % 10

    reverse = reverse * 10 + digit

    num = num // 10

print("Reverse =", reverse)