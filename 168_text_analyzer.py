#!/usr/bin/env python3
"""Text Analyzer — word counts, common words, sentence counts, and replacement.

Run: python 168_text_analyzer.py
Uses only the Python standard library.
"""
import re
from collections import Counter
from pathlib import Path

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "is", "are", "was", "were",
    "to", "of", "in", "on", "for", "with", "it", "this", "that", "as",
    "at", "by", "be", "from", "i", "you", "he", "she", "we", "they",
}

def analyze(text):
    words = re.findall(r"\b[\w'-]+\b", text.lower())
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    paragraphs = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    letters = sum(ch.isalpha() for ch in text)
    common = Counter(w for w in words if w not in STOP_WORDS)
    return {
        "characters": len(text),
        "characters_without_spaces": sum(not ch.isspace() for ch in text),
        "letters": letters,
        "words": len(words),
        "unique_words": len(set(words)),
        "sentences": len(sentences),
        "paragraphs": len(paragraphs),
        "average_word_length": (sum(map(len, words)) / len(words)) if words else 0,
        "reading_minutes": len(words) / 200,
        "common_words": common.most_common(10),
    }

def main():
    print("=== TEXT ANALYZER ===")
    print("1. Type/paste text\n2. Analyze a text file\n3. Replace text in a string")
    choice = input("Choose: ").strip()
    if choice == "1":
        print("Enter/paste text. Finish with a line containing only END:")
        lines = []
        while True:
            line = input()
            if line == "END": break
            lines.append(line)
        text = "\n".join(lines)
        stats = analyze(text)
        for key, value in stats.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    elif choice == "2":
        path = Path(input("Text file path: ").strip())
        try: content = path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"Could not read file: {exc}"); return
        for key, value in analyze(content).items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    elif choice == "3":
        original = input("Original text: ")
        old = input("Text to find: ")
        if not old:
            print("Find text cannot be empty."); return
        new = input("Replace with: ")
        count = original.count(old)
        print(f"Replacements made: {count}")
        print(original.replace(old, new))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
