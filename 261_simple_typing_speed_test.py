"""Measure typing speed using a sample sentence."""
import time

SAMPLE = "Python makes it easier to solve problems with simple code."

def main():
    print("Typing Speed Test\n")
    print("Type this sentence as quickly and accurately as you can:")
    print(SAMPLE)
    input("\nPress Enter when ready...")
    start = time.time()
    typed = input("Start typing: ")
    elapsed = max(time.time() - start, 0.01)
    wpm = len(typed.split()) / (elapsed / 60)
    correct = sum(a == b for a, b in zip(SAMPLE, typed))
    accuracy = correct / max(len(SAMPLE), len(typed), 1) * 100
    print(f"\nTime: {elapsed:.1f} seconds")
    print(f"Speed: {wpm:.1f} words per minute")
    print(f"Character accuracy: {accuracy:.1f}%")

if __name__ == "__main__":
    main()
