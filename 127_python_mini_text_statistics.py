# 127_python_mini_text_statistics.py
# Mini Text Statistics Tool - 10 practical features

text = """Python is a popular programming language.
Python supports automation, data analysis, and web development.
Learning Python takes practice."""

print("1. Text:\n", text)
print("2. Character count:", len(text))
print("3. Characters without whitespace:", len("".join(text.split())))
words = text.split()
print("4. Word count:", len(words))
lines = text.splitlines()
print("5. Line count:", len(lines))
sentences = [s for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
print("6. Sentence count:", len(sentences))
clean_words = [w.strip(".,!?;:\"'()") for w in words]
longest = max(clean_words, key=len)
print("7. Longest word:", longest)
target = "python"
count = sum(w.strip(".,!?;:").lower() == target for w in words)
print("8. Count of Python:", count)
unique_words = sorted({w.strip(".,!?;:").lower() for w in words})
print("9. Unique word count:", len(unique_words))
frequency = {}
for word in clean_words:
    key = word.lower()
    if key:
        frequency[key] = frequency.get(key, 0) + 1
print("10. Word frequency:", frequency)
