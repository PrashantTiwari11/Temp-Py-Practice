# 128_python_mini_file_extension_report.py
# Mini File Extension Report - 10 practical features
# Uses sample filenames only; does not access your actual files.

from pathlib import PurePath

filenames = [
    "assignment.docx", "main.py", "notes.txt", "photo.png", "report.pdf",
    "script.py", "logo.svg", "data.csv", "backup.zip", "README.md"
]

print("1. Filenames:", filenames)
print("2. File count:", len(filenames))
extensions = [PurePath(name).suffix.lower() for name in filenames]
print("3. Extensions:", extensions)
extension_counts = {}
for ext in extensions:
    key = ext or "(no extension)"
    extension_counts[key] = extension_counts.get(key, 0) + 1
print("4. Extension counts:", extension_counts)
print("5. Python files:", [n for n in filenames if n.lower().endswith(".py")])
image_exts = {".png", ".jpg", ".jpeg", ".gif", ".svg"}
print("6. Image files:", [n for n in filenames if PurePath(n).suffix.lower() in image_exts])
doc_exts = {".pdf", ".doc", ".docx", ".txt"}
print("7. Document files:", [n for n in filenames if PurePath(n).suffix.lower() in doc_exts])
print("8. Sorted filenames:", sorted(filenames, key=str.lower))
keyword = "report"
print("9. Search results:", [n for n in filenames if keyword in n.lower()])
print("10. No extension:", [n for n in filenames if not PurePath(n).suffix])
