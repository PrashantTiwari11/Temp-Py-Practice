# 94_python_file_backup_tool.py
# File Backup Utility - 10 practical features
from pathlib import Path
import shutil
import tempfile

with tempfile.TemporaryDirectory() as temp:
    root = Path(temp)
    source = root / "source"
    backup = root / "backup"
    source.mkdir()
    backup.mkdir()

    # Create sample files
    (source / "notes.txt").write_text("Python notes", encoding="utf-8")
    (source / "data.txt").write_text("Student data", encoding="utf-8")
    (source / "readme.md").write_text("# Project", encoding="utf-8")

    # 1. List source files
    print("1. Source files:", [p.name for p in source.iterdir()])

    # 2. Count files
    print("2. File count:", len(list(source.iterdir())))

    # 3. Create backup directory
    backup.mkdir(exist_ok=True)
    print("3. Backup directory ready:", backup.exists())

    # 4. Copy one file
    shutil.copy2(source / "notes.txt", backup / "notes.txt")
    print("4. Copied notes.txt")

    # 5. Copy all files
    for file in source.iterdir():
        if file.is_file():
            shutil.copy2(file, backup / file.name)
    print("5. Full backup:", [p.name for p in backup.iterdir()])

    # 6. Check backup file
    print("6. Backup exists:", (backup / "data.txt").exists())

    # 7. Compare file contents
    same = (source / "data.txt").read_text(encoding="utf-8") ==            (backup / "data.txt").read_text(encoding="utf-8")
    print("7. Content match:", same)

    # 8. Backup size
    size = sum(p.stat().st_size for p in backup.iterdir())
    print("8. Backup size:", size, "bytes")

    # 9. Restore a file
    restore = root / "restored.txt"
    shutil.copy2(backup / "notes.txt", restore)
    print("9. Restored file:", restore.read_text(encoding="utf-8"))

    # 10. Backup summary
    print("10. Backup completed safely in temporary workspace.")
