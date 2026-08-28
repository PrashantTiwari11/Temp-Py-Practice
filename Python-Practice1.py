#🟢 Level 1: Print & Variables
#Q1. Apna naam print karo
name = "Prashant"

print(name)

#Output:

#Prashant
#Q2. Do numbers ka addition karo
num1 = 10
num2 = 20

sum = num1 + num2

print(sum)

# Output:

# 30
# Q3. User ki age store karke print karo
age = 21

print("My age is:", age)

# 🟡 Level 2: Input Practice
# Q4. User se naam lekar greeting print karo
name = input("Enter your name: ")

print("Hello", name)
#Q5. Do numbers lekar addition karo
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2

print("Sum =", result)
#Q6. Rectangle ka area calculate karo

#Formula:

#Area = length × width
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area =", area)
#🟠 Level 3: If-Else Practice
#Q7. Number even hai ya odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#Q8. Check karo number positive, negative ya zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")

elif num < 0:
    print("Negative")

else:
    print("Zero")
#Q9. Student pass hai ya fail
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")