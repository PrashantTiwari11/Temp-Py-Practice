"""216 - Folder File Search. Usage: python 216_folder_file_search.py [folder]"""
from pathlib import Path
import sys

def main():
    root = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path(".")
    if not root.is_dir():
        print("Not a folder:", root)
        return
    term = input("Text to find in file/folder names: ").strip().lower()
    if not term:
        print("Search text cannot be empty.")
        return
    matches = [path for path in root.rglob("*") if term in path.name.lower()]
    for path in matches:
        print(path)
    print(f"Found {len(matches)} matching item(s).")

if __name__ == "__main__":
    main()
