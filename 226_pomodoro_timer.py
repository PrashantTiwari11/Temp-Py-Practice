import time

def countdown(minutes, label):
    seconds = minutes * 60
    print(f"\n{label} started for {minutes} minute(s). Press Ctrl+C to stop.")
    try:
        while seconds:
            mins, secs = divmod(seconds, 60)
            print(f"\rTime remaining: {mins:02d}:{secs:02d}", end="", flush=True)
            time.sleep(1)
            seconds -= 1
        print(f"\n{label} complete!")
    except KeyboardInterrupt:
        print("\nTimer stopped.")

def main():
    try:
        work = int(input("Work duration in minutes [25]: ") or "25")
        pause = int(input("Break duration in minutes [5]: ") or "5")
        if work <= 0 or pause <= 0:
            raise ValueError
    except ValueError:
        print("Please enter positive whole numbers.")
        return
    while True:
        countdown(work, "Focus session")
        if input("Take a break? (y/n): ").strip().lower() != "y":
            break
        countdown(pause, "Break")

if __name__ == "__main__":
    main()
