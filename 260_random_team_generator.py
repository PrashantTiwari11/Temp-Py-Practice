"""Shuffle names and distribute them across random teams."""
import random

def main():
    raw = input("Enter names separated by commas: ")
    names = [part.strip() for part in raw.split(",") if part.strip()]
    if len(names) < 2:
        print("Enter at least two names.")
        return
    try:
        count = int(input("Number of teams: "))
        if not 1 <= count <= len(names):
            print(f"Choose a number from 1 to {len(names)}.")
            return
    except ValueError:
        print("Enter a valid whole number.")
        return

    random.shuffle(names)
    teams = [[] for _ in range(count)]
    for index, name in enumerate(names):
        teams[index % count].append(name)
    for number, team in enumerate(teams, start=1):
        print(f"Team {number}: {', '.join(team)}")

if __name__ == "__main__":
    main()
