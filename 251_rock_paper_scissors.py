"""Play Rock, Paper, Scissors against the computer."""
import random

CHOICES = ("rock", "paper", "scissors")

def main():
    print("Rock, Paper, Scissors")
    while True:
        player = input("Choose rock, paper, scissors (or q to quit): ").strip().lower()
        if player == "q":
            print("Thanks for playing!")
            break
        if player not in CHOICES:
            print("Invalid choice. Try again.")
            continue
        computer = random.choice(CHOICES)
        print(f"Computer chose: {computer}")
        if player == computer:
            print("It's a tie!")
        elif (player, computer) in {
            ("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")
        }:
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
    main()
