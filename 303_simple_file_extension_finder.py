"""Project 303: Find a File's Extension"""
from pathlib import Path

def main():
    filename = input("Enter a file name or path: ").strip()
    if not filename:
        print("Please enter a file name.")
        return
    extension = Path(filename).suffix
    print("File extension:", extension if extension else "No extension found.")

if __name__ == "__main__":
    main()
