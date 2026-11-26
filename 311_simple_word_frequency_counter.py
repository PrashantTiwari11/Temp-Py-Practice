# Simple Word Frequency Counter

import string

sentence = input("Enter a sentence: ").lower()
clean_sentence = sentence.translate(str.maketrans("", "", string.punctuation))
words = clean_sentence.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

if not frequency:
    print("No words found.")
else:
    print("\nWord frequencies:")
    for word, count in sorted(frequency.items()):
        print(f"{word}: {count}")
