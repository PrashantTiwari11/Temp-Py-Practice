"""212 - Duplicate File Finder. Reports duplicates but never deletes files.
Usage: python 212_duplicate_file_finder.py [folder_path]
"""
from pathlib import Path
import hashlib
import sys

def file_hash(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def main():
    root = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path(".")
    if not root.is_dir():
        print("Not a folder:", root)
        return
    sizes = {}
    for path in root.rglob("*"):
        if path.is_file():
            try:
                sizes.setdefault(path.stat().st_size, []).append(path)
            except OSError as error:
                print(f"Skipped {path}: {error}")
    hashes = {}
    for paths in sizes.values():
        if len(paths) < 2:
            continue
        for path in paths:
            try:
                hashes.setdefault(file_hash(path), []).append(path)
            except OSError as error:
                print(f"Could not read {path}: {error}")
    duplicates = [paths for paths in hashes.values() if len(paths) > 1]
    if not duplicates:
        print("No duplicate files found.")
        return
    for index, paths in enumerate(duplicates, 1):
        print(f"\nDuplicate group {index}:")
        for path in paths:
            print(" ", path)
    print(f"\nFound {len(duplicates)} duplicate group(s). No files were changed.")

if __name__ == "__main__":
    main()
