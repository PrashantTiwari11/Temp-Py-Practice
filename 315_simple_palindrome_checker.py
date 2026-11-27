# Simple Palindrome Checker
text = input("Enter a word or phrase: ")
normalized = "".join(character.lower() for character in text if character.isalnum())
if normalized == normalized[::-1]:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
