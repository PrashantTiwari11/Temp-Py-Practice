# Simple Password Character Counter

password = input("Enter a password: ")

letters = 0
digits = 0
special = 0
spaces = 0

for character in password:
    if character.isalpha():
        letters += 1
    elif character.isdigit():
        digits += 1
    elif character.isspace():
        spaces += 1
    else:
        special += 1

print("\nPassword character summary:")
print("Total characters:", len(password))
print("Letters:", letters)
print("Digits:", digits)
print("Special characters:", special)
print("Spaces:", spaces)
