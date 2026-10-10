"""151 File Statistics: 10 practical features."""
from pathlib import Path
from collections import Counter
import string
def read_text(path): return Path(path).read_text(encoding="utf-8")
def lines(text): return len(text.splitlines())
def words(text): return len(text.split())
def characters(text): return len(text)
def non_whitespace(text): return sum(not c.isspace() for c in text)
def frequency(text):
    items = [w.strip(string.punctuation).lower() for w in text.split()]
    return Counter(w for w in items if w)
def longest_word(text):
    items = [w.strip(string.punctuation) for w in text.split()]
    return max((w for w in items if w), key=len, default="")
def top_words(text, limit=5): return frequency(text).most_common(limit)
def extension_report(folder="."):
    return dict(Counter(x.suffix.lower() or "[no extension]" for x in Path(folder).iterdir() if x.is_file()))
def save_report(text, path="file_statistics.txt"):
    report = f"Lines: {lines(text)}\nWords: {words(text)}\nCharacters: {characters(text)}\nNon-whitespace: {non_whitespace(text)}\nLongest word: {longest_word(text)}\nTop words: {top_words(text)}\n"
    Path(path).write_text(report, encoding="utf-8"); return report
if __name__ == "__main__":
    sample = "Python makes automation easy. Python is readable, practical, and powerful!"
    print("1 Sample:", sample)
    print("2 Lines:", lines(sample))
    print("3 Words:", words(sample))
    print("4 Characters:", characters(sample))
    print("5 Non-whitespace:", non_whitespace(sample))
    print("6 Word frequency:", frequency(sample))
    print("7 Longest word:", longest_word(sample))
    print("8 Top words:", top_words(sample, 3))
    print("9 Extensions in current folder:", extension_report())
    print("10 Save report with save_report(sample)")
