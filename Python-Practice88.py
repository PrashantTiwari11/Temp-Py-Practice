# 83_python_text_processing_nlp.py
# Text Processing and Basic NLP - 10 practical programs/features
import re
from collections import Counter

text = """Python is easy to learn. Python is powerful and useful.
Learning Python helps with automation, data science, and web development."""

lower = text.lower()
print("1. Lowercase:", lower)

words = re.findall(r"[a-zA-Z]+", lower)
print("2. Words:", words)
print("3. Word count:", len(words))

unique = sorted(set(words))
print("4. Unique words:", unique)

frequency = Counter(words)
print("5. Word frequency:", frequency)
print("6. Most common:", frequency.most_common(5))

sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
print("7. Sentence count:", len(sentences))

clean = re.sub(r"[^a-zA-Z0-9\s]", "", text)
print("8. Without punctuation:", clean)

stop_words = {"is", "to", "and", "with", "the", "for"}
filtered = [word for word in words if word not in stop_words]
print("9. Stop words removed:", filtered)

keyword = "python"
print("10. Keyword occurrences:", frequency[keyword])
