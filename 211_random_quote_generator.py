"""211 - Random Quote Generator"""
import random

QUOTES = [
    ("Small steps every day lead to big changes.", "Unknown"),
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Learning never exhausts the mind.", "Leonardo da Vinci"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("Success is the sum of small efforts, repeated day in and day out.", "Robert Collier"),
]

def main():
    while True:
        quote, author = random.choice(QUOTES)
        print(f"\n“{quote}”\n— {author}")
        if input("Another quote? (y/n): ").strip().lower() != "y":
            break

if __name__ == "__main__":
    main()
