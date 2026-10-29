import random

def main():
    secret=random.randint(1,100); attempts=0
    print("Guess a number from 1 to 100; type q to quit.")
    while True:
        raw=input("Your guess: ").strip().lower()
        if raw=="q": print("The number was",secret); return
        try: guess=int(raw)
        except ValueError: print("Enter a whole number."); continue
        if not 1<=guess<=100: print("Choose 1 to 100."); continue
        attempts+=1
        if guess<secret: print("Too low!")
        elif guess>secret: print("Too high!")
        else: print(f"Correct in {attempts} attempt(s)!"); return

if __name__ == "__main__": main()
