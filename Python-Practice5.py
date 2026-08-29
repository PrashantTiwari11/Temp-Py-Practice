# 🔥 Level 10: Logic Building Practice
# 41. Check whether a number is divisible by 5
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
#42. Find factorial of a number

#Example: 5! = 5 × 4 × 3 × 2 × 1

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)
#43. Check whether a number is a palindrome

#Example: 121 → Palindrome

num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#44. Find the sum of digits

#Example: 123 → 1 + 2 + 3 = 6

num = input("Enter a number: ")

total = 0

for digit in num:
    total = total + int(digit)

print("Sum =", total)
#45. Print multiplication tables from 1 to 5
for num in range(1, 6):

    print("\nTable of", num)

    for i in range(1, 11):
        print(num, "x", i, "=", num * i)