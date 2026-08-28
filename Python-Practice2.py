#🔵 Level 4: For Loop Practice
#Q10. "Python" 5 baar print karo
for i in range(5):
    print("Python")
#Q11. 1 se 10 tak numbers print karo
for i in range(1, 11):
    print(i)
#Q12. 1 se 20 tak even numbers print karo
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
#Q13. 1 se 20 tak odd numbers print karo
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
#Q14. Kisi number ka table print karo
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Example agar num = 5:

# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50
# 🔥 Level 5: Loop + Logic
# Q15. 1 se 10 tak numbers ka sum
total = 0

for i in range(1, 11):
    total = total + i

print("Sum =", total)

#Output:

Sum = 55
#Q16. 1 se 100 tak even numbers ka sum
total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total = total + i

print(total)
#Q17. List ke saare elements print karo
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)
#Q18. List ke numbers ka sum karo
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

print(total)
#Q19. List mein largest number find karo
numbers = [10, 45, 23, 78, 12]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number =", largest)
#Q20. List mein kitne even numbers hain
numbers = [10, 15, 20, 25, 30, 35]

count = 0

for num in numbers:
    if num % 2 == 0:
        count = count + 1

print("Even numbers =", count)