# 136 - Mini Customer Feedback Analyzer: 10 practical features
# This simple keyword method is a demo, not a trained sentiment model.
feedback = [
    "The delivery was fast and the product is excellent.",
    "Support was helpful, but the package arrived late.",
    "Great quality and friendly service.",
    "The item was damaged and the response was disappointing.",
    "Easy ordering and good value.",
]
positive_words = {"fast", "excellent", "helpful", "great", "friendly", "good", "easy", "quality"}
negative_words = {"late", "damaged", "disappointing", "slow", "poor", "bad", "broken"}

# 1. Count feedback entries
def feedback_count():
    return len(feedback)

# 2. Normalize text
def normalize(comment):
    return "".join(c.lower() if c.isalnum() or c.isspace() else " " for c in comment)

# 3. Count words
def word_count(comment):
    return len(normalize(comment).split())

# 4. Positive keyword matches
def positive_matches(comment):
    return sorted(set(normalize(comment).split()) & positive_words)

# 5. Negative keyword matches
def negative_matches(comment):
    return sorted(set(normalize(comment).split()) & negative_words)

# 6. Assign a basic sentiment
def sentiment(comment):
    score = len(positive_matches(comment)) - len(negative_matches(comment))
    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"

# 7. Filter feedback by sentiment
def filter_sentiment(label):
    return [c for c in feedback if sentiment(c).lower() == label.lower()]

# 8. Average comment length
def average_words():
    return round(sum(word_count(c) for c in feedback) / len(feedback), 2) if feedback else 0

# 9. Most common words longer than three letters
def common_words(limit=5):
    counts = {}
    for comment in feedback:
        for word in normalize(comment).split():
            if len(word) > 3:
                counts[word] = counts.get(word, 0) + 1
    return sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))[:limit]

# 10. Print analysis report
def report():
    for comment in feedback:
        print(f"[{sentiment(comment)}] {comment}")
    print("Feedback count:", feedback_count())
    print("Average words per comment:", average_words())
    print("Common words:", common_words())

if __name__ == "__main__":
    print("CUSTOMER FEEDBACK REPORT")
    report()
