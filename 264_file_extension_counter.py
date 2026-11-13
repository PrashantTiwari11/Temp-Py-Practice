"""Count file extensions in a selected folder."""
from pathlib import Path
from collections import Counter

def main():
    folder = Path(input("Enter folder path: ").strip().strip('"')).expanduser()
    if not folder.is_dir():
        print("Folder not found. Check the path and try again.")
        return
    counts = Counter(
        item.suffix.lower() or "[no extension]"
        for item in folder.iterdir()
        if item.is_file()
    )
    if not counts:
        print("No files found in this folder.")
        return
    print(f"\nFile extension counts in {folder}:")
    for extension, count in sorted(counts.items()):
        print(f"{extension}: {count}")

if __name__ == "__main__":
    main()
