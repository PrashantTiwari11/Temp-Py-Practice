import time

def countdown(seconds):
    if seconds < 0:
        raise ValueError("Time cannot be negative.")
    try:
        while seconds:
            mins, secs = divmod(seconds, 60)
            print(f"\\rTime left: {mins:02d}:{secs:02d}", end="", flush=True)
            time.sleep(1)
            seconds -= 1
        print("\\rTime is up!          ")
    except KeyboardInterrupt:
        print("\\nCountdown cancelled.")

def main():
    try:
        seconds = int(input("Countdown time in seconds: "))
        countdown(seconds)
    except ValueError as error:
        print("Enter a non-negative whole number.", error)

if __name__ == "__main__":
    main()
