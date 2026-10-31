"""215 - Reading Time Estimator"""
import re

def estimate_reading_time(text, words_per_minute=200):
    words = re.findall(r"\b[\w'-]+\b", text)
    return len(words), len(words) / words_per_minute

def main():
    print("Enter/paste text. Submit a blank line to finish:")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    count, minutes = estimate_reading_time("\n".join(lines))
    print("Word count:", count)
    print(f"Estimated reading time: {minutes:.1f} minute(s) at 200 words/minute.")

if __name__ == "__main__":
    main()
