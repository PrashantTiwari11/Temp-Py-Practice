"""Display a random quote from a small built-in collection."""
import random

QUOTES = [
    "The secret of getting ahead is getting started.",
    "It always seems impossible until it is done.",
    "Learning never exhausts the mind.",
    "Great things are done by a series of small things brought together.",
    "Success is the sum of small efforts repeated day in and day out.",
]

def main():
    print("Your Random Quote")
    print(random.choice(QUOTES))

if __name__ == "__main__":
    main()
