# 104_python_text_file_manager.py
# Text File Manager - 10 practical features

from pathlib import Path
import tempfile

with tempfile.TemporaryDirectory() as folder:
    file = Path(folder) / "notes.txt"

    file.write_text(
        "Python is easy to learn.\nPython is powerful.\n",
        encoding="utf-8"
    )
    print("1. File created:", file.exists())

    text = file.read_text(encoding="utf-8")
    print("2. Content:", text)
    print("3. Character count:", len(text))
    print("4. Word count:", len(text.split()))
    print("5. Line count:", len(text.splitlines()))

    keyword = "Python"
    print("6. Keyword found:", keyword in text)
    print("7. Python occurrences:", text.lower().count("python"))

    with file.open("a", encoding="utf-8") as f:
        f.write("Python supports automation.\n")
    print("8. File updated:", file.read_text(encoding="utf-8"))

    updated = file.read_text(encoding="utf-8").replace("easy", "simple")
    file.write_text(updated, encoding="utf-8")
    print("9. Replacement done:", "simple" in updated)

    summary = {
        "name": file.name,
        "size": file.stat().st_size,
        "lines": len(file.read_text(encoding="utf-8").splitlines())
    }
    print("10. Summary:", summary)
