# 76_python_project_file_organizer.py
# Practical File Organizer Project - 10 features
# Uses a temporary folder so existing files are not changed.

from pathlib import Path
import tempfile
import shutil

with tempfile.TemporaryDirectory() as temp:
    base = Path(temp)

    folders = ["Images", "Documents", "Python", "Other"]
    for folder in folders:
        (base / folder).mkdir()
    print("1. Created folders:", folders)

    samples = {
        "photo.jpg": "image",
        "notes.txt": "notes",
        "report.pdf": "report",
        "program.py": "print('Hello')",
        "data.csv": "name,marks"
    }
    for filename, content in samples.items():
        (base / filename).write_text(content)
    print("2. Sample files:", list(samples))

    def extension(path):
        return path.suffix.lower()

    print("3. Extension:", extension(base / "photo.jpg"))

    def category(path):
        ext = extension(path)
        if ext in {".jpg", ".jpeg", ".png", ".gif"}:
            return "Images"
        if ext in {".txt", ".pdf", ".docx"}:
            return "Documents"
        if ext == ".py":
            return "Python"
        return "Other"

    print("4. Categories:")
    for file in base.iterdir():
        if file.is_file():
            print("  ", file.name, "->", category(file))

    for file in list(base.iterdir()):
        if file.is_file():
            shutil.move(str(file), str(base / category(file) / file.name))
    print("5. Files organized.")

    counts = {
        folder: len(list((base / folder).iterdir()))
        for folder in folders
    }
    print("6. File counts:", counts)

    python_files = [p.name for p in (base / "Python").glob("*.py")]
    print("7. Python files:", python_files)

    text_file = base / "Documents" / "notes.txt"
    print("8. Read notes:", text_file.read_text())

    print("9. Total organized files:", sum(counts.values()))
    print("10. File organizer demo completed safely.")
