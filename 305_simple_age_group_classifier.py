# Simple Age Group Classifier

age = int(input("Enter your age: "))

if age < 0:
    print("Age cannot be negative.")
elif age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
