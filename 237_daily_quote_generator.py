import random

QUOTES = [
    "Small steps every day lead to big results.",
    "Learning never exhausts the mind.",
    "Consistency is more important than perfection.",
    "Your future is created by what you do today.",
    "Every expert was once a beginner."
]

if __name__ == "__main__":
    print("Your daily quote:")
    print(random.choice(QUOTES))
