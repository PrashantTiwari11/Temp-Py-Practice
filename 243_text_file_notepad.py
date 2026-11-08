from pathlib import Path

def read_multiline():
    print("Type text. Enter END on a separate line to finish.")
    lines = []
    while True:
        line = input()
        if line == "END":
            return lines
        lines.append(line)

def main():
    filename = input("Text file name (e.g. notes.txt): ").strip()
    if not filename:
        print("A file name is required.")
        return
    path = Path(filename)
    while True:
        print("\\n1. Write/replace  2. Read  3. Append  4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            path.write_text("\\n".join(read_multiline()) + "\\n", encoding="utf-8")
            print("File saved.")
        elif choice == "2":
            if path.exists():
                print(path.read_text(encoding="utf-8"))
            else:
                print("File does not exist yet.")
        elif choice == "3":
            lines = read_multiline()
            if lines:
                with path.open("a", encoding="utf-8") as file:
                    file.write("\\n".join(lines) + "\\n")
            print("Text appended.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
