# Simple Vowel and Consonant Counter

text = input("Enter a word or sentence: ").lower()
vowels = 0
consonants = 0

for character in text:
    if character.isalpha():
        if character in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("\nText analysis:")
print("Vowels:", vowels)
print("Consonants:", consonants)
