# 🔵 Level 8: List Practice
# 31. Print all elements
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)
#32. Find the smallest number
numbers = [45, 12, 78, 3, 56]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest =", smallest)
#33. Count positive numbers
numbers = [10, -5, 20, -15, 30, -8]

count = 0

for num in numbers:
    if num > 0:
        count = count + 1

print("Positive numbers =", count)
#34. Count negative numbers
numbers = [10, -5, 20, -15, 30, -8]

count = 0

for num in numbers:
    if num < 0:
        count = count + 1

print("Negative numbers =", count)
#35. Find the average of numbers
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)

print("Average =", average)
# 🟠 Level 9: Functions Practice
# 36. Create a simple function
def greet():
    print("Hello Prashant")


greet()
#37. Function to add two numbers
def add(num1, num2):
    result = num1 + num2
    print("Sum =", result)


add(10, 20)
#38. Function to check even or odd
def check_number(num):

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


check_number(10)
#39. Function to find square
def square(num):
    return num * num


result = square(5)

print(result)
#40. Function to find largest number
def find_largest(numbers):

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


numbers = [10, 45, 23, 78, 12]

print("Largest =", find_largest(numbers))