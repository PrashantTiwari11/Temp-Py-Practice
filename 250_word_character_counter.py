"""Count words, characters, and lines in text."""
def main():
    print("Enter text. Submit an empty line to finish:")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    text = "\n".join(lines)
    print("\nText statistics")
    print(f"Characters (including spaces): {len(text)}")
    print(f"Characters (excluding whitespace): {len(''.join(text.split()))}")
    print(f"Words: {len(text.split())}")
    print(f"Lines: {len(lines)}")

if __name__ == "__main__":
    main()
